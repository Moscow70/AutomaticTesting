import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")

from langchain_community.document_loaders import PyPDFLoader

loaders = [
    PyPDFLoader("D:/vscodeproject/python/competition_method.pdf")
]

docs = []

for loader in loaders:
    docs.extend(loader.load())

from langchain.text_splitter import RecursiveCharacterTextSplitter

textsplitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    # chunk_overlap = 50
)

splits = textsplitter.split_documents(docs)

print(len(splits))

from langchain_openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings()



from langchain_community.vectorstores import Chroma

persist_directory = 'D:/workspace/chroma'


vectordb = Chroma.from_documents(
    documents=splits,
    embedding=embedding,
    persist_directory=persist_directory
)


print(vectordb._collection.count())

question = "学校认定哪些比赛是有效的？"

docs = vectordb.similarity_search(question, k = 3)

print(len(docs))

print("最接近的结果：")
print(docs[0].page_content)
print("------------------------")
print("其它结果")
print(docs[1].page_content)