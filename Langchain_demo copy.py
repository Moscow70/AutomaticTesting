import os
from dotenv import load_dotenv
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.language_models.chat_models import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts.chat import ChatMessagePromptTemplate

load_dotenv(dotenv_path=".env", override=True)

QIANFAN_ACCESS_KEY = os.environ.get("QIANFAN_ACCESS_KEY")
QIANFAN_SECRET_KEY = os.environ.get("QIANFAN_SECRET_KEY")

llm = QianfanChatEndpoint(model = "ERNIE-Lite-8K")

template = """
你作为一个经验丰富的客服代表，请为以下客户问题提供解答：
{Query}
"""

chat_message_prompt = ChatMessagePromptTemplate.from_template(role = "技术支持", template = template)

formatted_prompt = chat_message_prompt.format(Query = "产品如何使用？")

prompts = str(formatted_prompt)

response = llm.invoke(prompts)
print(f"大模型的响应：{response}")