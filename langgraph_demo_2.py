from typing import Annotated, Literal, TypedDict

from langchain_core.messages import HumanMessage
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph, MessagesState
from langgraph.prebuilt import ToolNode
from openai import OpenAI
from dotenv import load_dotenv
import os
import langsmith

load_dotenv(dotenv_path=".env", override=True)

LANGSMITH_API_KEY = os.environ.get("LANGSMITH_API_KEY")

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")




# 定义一个工具节点，让agent使用
@tool
def search(query:str):
    """ Call to surf the web."""
    if "T72" in query.lower() or "T80" in query.lower() or "T90" in query.lower():
        return "It's a Russian tank"
    return "It's not a Russian tank"

# 将search放进工具箱里
tools = [search]

# 构建一个工具节点，工具节点里存放tools工具箱
tool_node = ToolNode(tools)

# model = OpenAI(api_key=OPENAI_API_KEY, base_url = "https://api.agicto.cn/v1")

model = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0, api_key=ANTHROPIC_API_KEY).bind_tools(tools)

# 写一个条件边的条件
def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state['messages']
    last_message = messages[-1]
    # 如果进行了工具调用，则将其导向工具节点
    if last_message.tool_calls:
        return "tools"
    # 否则停止（返回给用户）
    return END

# 写一个调用大模型的函数
# def call_model(state : MessagesState):
#     messages = state['messages']
#     response = model.chat.completions.create(
#         model = "gpt-3.5-turbo",
#         messages = messages,
#         temperature=0
#         tools= tools
#     )
#     return {"messages": [response]}

def call_model(state: MessagesState):
    messages = state['messages']
    response = model.invoke(messages)
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}

# 定义一个新的图
work_flow = StateGraph(MessagesState)

# 定义两个节点
work_flow.add_node("agent", call_model)
work_flow.add_node("tools", tool_node)

# 设置入点
work_flow.set_entry_point("agent")

# 添加一条条件边
work_flow.add_conditional_edges("agent", should_continue)

# 添加一条普通边。在tools被调用后，再调用agent
work_flow.add_edge("tools", "agent")

# 实现记忆能力，创建一个线程，保存线程状态数据
checkpointer = MemorySaver()

# 编译为langchain runnable
app = work_flow.compile(checkpointer=checkpointer)

final_state = app.invoke(
    {"messages" : [HumanMessage(content= "What is the nationality of T90")]},
    config={"configurable": {"thread_id" : 42}}
)

print(final_state["messages"][-1].content)