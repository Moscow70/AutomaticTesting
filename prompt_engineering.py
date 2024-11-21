from openai import OpenAI
from pydantic import BaseModel, ValidationError
import os
import json
import httpx
from dotenv import load_dotenv


class Book(BaseModel):
    name : str
    author : str

class Books(BaseModel) :
    publiser :str
    books : list[Book]


# 通过key和url调用OpenAI方法创建一个对象
load_dotenv(dotenv_path=".env", override=True)

api_key = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_API_BASE")


client = OpenAI(
    api_key = api_key,
    base_url = base_url
)

output_format = """
{
    "publisher": "string",
    "books": [
        {"name": "string","author": "string"},
        {"name": "string","author": "string"}
    ]
}
"""

ai_answer_prompt_1 = """
{
    "publisher": "清华大学出版社", 
    "books": [
        {
            "name": "《人工智能：现代方法》",
            "author": "斯图尔特·罗素、彼得·诺维格"
        }, 
        {
            "name": "《深度学习》", 
            "author": "伊恩·古德费洛、约书亚·本吉奥"
        }
    ]
}
"""

ai_answer_prompt_2 = """
{

    "publisher": "清华大学出版社",
    "books": [
        {
            "name": "《深度学习》",
            "author": "伊恩·古德费洛、约书亚·本吉奥"
        }
    ]
}
"""

ai_answer_prompt_3 = """
{
    "publisher": "None
    "books": [
        {
            "name": "None",
            "author": "None"
        }
    ]
}
"""


prompt_template = """
```markdown
**system:**
- 你是一个图书管理员，负责管理图书的信息。
- 你的回答必须以JSON格式提供，包含`publisher`和`books`两个字段。
- `books`字段必须是一个数组，每个元素是一个包含`name`和`author`字段的对象。
- 不要编造内容，只回答书籍相关问题。

**user:**
- 目标：负责接收用户的需求，并根据需求提供书籍的相关信息。
- 输出格式：按照JSON格式输出，输出的格式需要包含以下几个字段：
  - `publisher`：字符串类型，表示书籍的出版社名称。
  - `books`：数组类型，表示书籍的详细信息。每个元素是一个对象，包含以下字段：
    - `name`：字符串类型，表示书籍的名称。
    - `author`：字符串类型，表示书籍的作者。
- 以下是输出的格式，请严格按照此格式输出：
{output_format}

**示例：**
- 输入：帮我找两本人工智能相关书籍。
- AI：{ai_answer_prompt_1}

 - 输入：告诉我关于《深度学习》的书籍信息。
- AI：{ai_answer_prompt_2}

- 输入：帮我查找本周羽毛球比赛的相关信息。
- AI：{ai_answer_prompt_3}

**对话历史**：{dialog_history}


用户问题：{user_question}
"""

def get_books(question, dialog_history = ""):
    prompt = prompt_template.format(
        output_format = output_format,
        ai_answer_prompt_1 = ai_answer_prompt_1,
        ai_answer_prompt_2 = ai_answer_prompt_2,
        user_question = question,
        dialog_history = dialog_history
        )
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages= [
            {"role": "system", "content": prompt},
            {"role": "user", "content": question}

        ]
    )
    response_content = chat_completion.choices[0].message.content
    print("AI的回答：")
    print(response_content)

dialog_history = ""

while True:
    user_question = input("请输入你的问题，输入exit结束对话：")

    if user_question.lower() == "exit":
        print("对话结束")
        break
    
    response = get_books(user_question, dialog_history)
    dialog_history = dialog_history + f"- 用户：{user_question}\n- AI：{response}\n"