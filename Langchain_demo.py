import os
# from openai import OpenAI
from langchain_openai import OpenAI
import qianfan
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.language_models.chat_models import HumanMessage
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

QIANFAN_ACCESS_KEY = os.environ.get("QIANFAN_ACCESS_KEY")
QIANFAN_SECRET_KEY = os.environ.get("QIANFAN_SECRET_KEY")

chat = QianfanChatEndpoint(
    streaming = True,
    model = "ERNIE-Lite-8K"
)
messages = [HumanMessage(content="写一首关于秋天的诗")]
response = chat.invoke(messages)

print(response.content)

