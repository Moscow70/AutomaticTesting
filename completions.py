from openai import OpenAI
import os
import json
import httpx
from dotenv import load_dotenv

# 通过key和url调用OpenAI方法创建一个对象

load_dotenv(dotenv_path=".env", override=True)

api_key = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_API_BASE")
client = OpenAI(
    api_key = api_key,
    base_url = base_url
)

MODEL = "ERNIE-Lite-8K"

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
print("您好，我是一个AI法律咨询机器人，现在开始您的提问吧，您可以通过输入【exit】来结束对话：")
while True:
    user_input = input("Q:")
    if user_input.lower() == "exit" :
        print("Bye")
        break
    answer = get_case(user_input + '\n')
    prompt = prompt + 'A:' + answer + '\n'
    print(f"A:{answer}")