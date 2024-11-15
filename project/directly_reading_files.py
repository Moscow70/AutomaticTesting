from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

api_key = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_API_BASE")

llm = OpenAI(
    api_key = api_key,
    base_url = base_url
)

def get_case(question):
    chat_completions = llm.chat.completions.create(
        messages = [
            {"role": "system", "content": "你是一个软件测试工程师，你需要根据读入的文档生成对应的接口测试代码"},
            {"role": "user", "content": question}
        ],
        model="gpt-4o-mini",
    )
    output = chat_completions.choices[0].message.content
    return output

question = "根据提示词，按照格式生成对应的接口测试代码"
file_path = "D:/workspace/output/testcases.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

prompt = content + '\n' + question + '\n'

answer = get_case(prompt)

answer_path = "D:/workspace/output/answer.txt"

with open(answer_path, 'w', encoding='utf-8') as file:
    file.write(answer)




