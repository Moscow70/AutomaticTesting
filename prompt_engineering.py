from openai import OpenAI
from pydantic import BaseModel
import os
import json
import httpx
from dotenv import load_dotenv


class book(BaseModel):
    name : str
    author : str
    data : str

class Address(BaseModel):
    state : str
    city : str
    street : str

class books(BaseModel) :
    publiser :str
    address : Address
    books : list[book]


# 通过key和url调用OpenAI方法创建一个对象
load_dotenv(dotenv_path=".env", override=True)

api_key = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_API_BASE")


client = OpenAI(
    api_key = api_key,
    base_url = base_url
)

MODEL = "gpt-3.5-turbo"

prompt = '请你站在一个律师的角度分析用户的提问，并给出专业的回答，以下是用户的提问：'

def get_case(question):

    # 调用chat.completions.create方法来生成文本。传递的参数包括模型名称和消息列表
    chat_completions = client.chat.completions.create(

        # mseeage[...]是消息列表
        messages = [

            # 系统消息，告诉模型所扮演的角色
            {"role": "system", "content": prompt},

            # 用户消息
            {"role": "user", "content": question}
        ],
        model=MODEL,
    )
    # 从生成的结果中获取第一个选择消息的内容
    output = chat_completions.choices[0].message.content
    return output

# 单轮对话
# user_input = input ("请咨询法律问题：")
# answer = get_case(user_input)
# print(f"\n咨询结果：{answer}")


# 多轮对话
# print("您好，我是一个AI法律咨询机器人，现在开始您的提问吧，您可以通过输入【exit】来结束对话：")
# while True:
#     user_input = input("Q:")
#     if user_input.lower() == "exit" :
#         print("Bye")
#         break
#     answer = get_case(user_input + '\n')
#     prompt = prompt + 'A:' + answer + '\n'
#     print(f"A:{answer}")




def format_output(client, question, response_format):
    chat_completion = client.chat.completions.create(
        messages= [
            {"role": "system", "content": "你是一个图书管理员"},
            {"role": "user", "content": question}
        ],
        model = MODEL,
    )

    messages = [
        # {"role": "system", "content": "你是一个图书管理员"},
        {"role": "user", "content": question}
    ]

    completions = client.beta.chat.completions.parse(
        model = MODEL,
        messages= messages,
        response_format= response_format
    )
    print(chat_completion.choices[0].message.content)
    msg = None
    message = completions.choices[0].message
    if message.parsed:
        msg = message.content
    else:
        msg = message.refusal
    return msg

mes = format_output(client, "给我三本书的信息", books)
print(mes)