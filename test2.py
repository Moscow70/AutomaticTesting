from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

class Book(BaseModel):
    name: str
    author: str
    date: str

class Address(BaseModel):
    state: str
    city: str
    street: str

class Books(BaseModel):
    publisher: str
    address: Address
    books: list[Book]



def ask_gpt(prompt, response_format):

    load_dotenv(dotenv_path=".env", override=True)

    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_API_BASE")
    client = OpenAI(api_key=api_key, base_url=base_url)

    messages = [{
            "role": "user",
            "content": prompt
        }]
    completion = client.beta.chat.completions.parse(
        model="gpt-3.5-turbo",
        messages=messages,
        response_format=response_format
    )
    msg = None
    message = completion.choices[0].message
    if message.parsed:
        msg = message.content
    else:
        msg = message.refusal
    return msg

msg = ask_gpt("随机生成三个书籍信息", Books)

print(msg)