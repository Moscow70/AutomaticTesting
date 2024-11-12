from openai import OpenAI
from pathlib import Path
import json
import os
from dotenv import load_dotenv

# 调用本地函数

# api_key = str(os.getenv('OPENAI_API_KEY'))
# print(api_key)

def get_completion(messages, model, tools_arr = None) :
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = 0,
        max_tokens = 1024,
        tools = tools_arr
    )
    return response.choices[0].message

tools_arr = [
    {
        "type": "function",
        "function": {
            "name": "sum",
            "description": "sum函数可以用来计算一组数据的和",
            "parameters": {
                "type": "object",
                "properties": {
                    "numbers": {
                        "type": "array",
                        "items":{
                            "type":"number"
                        }
                    }
                }
            }
        }
    }
]

load_dotenv(dotenv_path=".env", override=True)

api_key = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_API_BASE")
client = OpenAI(api_key=api_key, base_url=base_url)

MODEL = "gpt-3.5-turbo"


prompt = "桌上有2个苹果，四个桃子和 3 本书，一共有几个水果？"

messages = [
    {"role": "system", "content": "你是一个数学家，你可以计算任何算式。"},
    {"role": "user", "content": prompt}
]

# 不使用tools进行第一次模型调用
response = get_completion(messages, MODEL)
print(response)

# 使用工具进行第二次调用
response = get_completion(messages, MODEL, tools_arr)
print(response)

# 返回需要调用的名称和参数之后，我们可以通过本地代码解析出来，然后再去调用相应函数
messages.append(response)

if (response.tool_calls is not None):
    for tool_call in response.tool_calls :
        print(f"调用{tool_call.function.name}函数，参数是{tool_call.function.arguments}")
        if tool_call.function.name == "sum":
            
            # 调用sum函数
            args = json.loads(tool_call.function.arguments)
            result = sum(args["numbers"])

            print("==函数返回==")
            print('函数返回值为：', result)

            # 把函数调用结果加入到对话历史中
            messages.append(
                {
                    "tool_call_id" : tool_call.id,
                    "role": "tool",
                    "name": "sum",
                    "content" : str(result)
                }
            )

            # 再次调用大模型，获取最终回复
            print('messages:\n', messages)
            print(get_completion(messages, MODEL).content)


