import os
from langchain_core.tools import tool
@tool
def multiply(first_int:int, second_int:int) -> int :
    '''两个整数相乘'''
    return first_int * second_int

@tool
def add(first_add:int, second_add:int) -> int:
    '''两个整数相加'''
    return first_add + second_add

tools = [multiply, add]

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.messages import HumanMessage, ToolMessage
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

QIANFAN_ACCESS_KEY = os.environ.get("QIANFAN_ACCESS_KEY")
QIANFAN_SECRET_KEY = os.environ.get("QIANFAN_SECRET_KEY")

llm = QianfanChatEndpoint(
    streaming = True,
    model = "ERNIE-Lite-8K"
)

llm_with_tools = llm.bind_tools(tools)

prompt = "一共有3个人，每个人有15个苹果，桌上还有10个梨，一共有多少水果？"

messageLC = [
    HumanMessage(prompt)
]

response = llm_with_tools.invoke(messageLC)
messageLC.append(response)

print(response.content)