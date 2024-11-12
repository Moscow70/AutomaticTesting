from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
# 该类用于解析和验证大模型输出，它使用pydantic库来定义输出的结构，并确保输出符合这个结构
from langchain_core.output_parsers import PydanticOutputParser
# basemodel类是pydantic的核心，它允许定义数据模型的结构和验证过则，同时提供了数据的序列化和反序列化功能；Field用于设置字段的额外信息
from pydantic import BaseModel, Field
from typing import List
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override= True)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")


llm = OpenAI(model= 'text-davinci-003')

# 定义BaseModel的样式
class CustomerInteraction(BaseModel):
    question: str = Field(description="客户的问题")
    response: str = Field(description="AI的响应")

# 将解析器结构化为已经定义好的数据对象
parser = PydanticOutputParser(pydantic_object=CustomerInteraction)

prompt = PromptTemplate(
    template= "响应用户的查询，中文输出。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

customer_query = "怎样查询我的订单状态？"
input = prompt.format_prompt(query = customer_query)
output = llm.invoke(input.to_string())

print(output)