from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain.text_splitter import TokenTextSplitter
# from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")

loader = PyPDFLoader(
    file_path= "D:/workspace/RA3比赛章程v1.0.pdf",
    extract_images=True
)

pages = loader.load()

print(len(pages))

# for page in pages:
#     print(page.page_content)
#     print("----------------------")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 150,
    chunk_overlap = 0
)


# token_splitter = TokenTextSplitter(
#     chunk_size = 100,
#     chunk_overlap = 0
# )

# headers_to_split_on = [
#     ("#", "Header 1"),
#     ("##", "Header 2"),
#     ("###", "Header 3")
# ]

# markdown_splitter = MarkdownHeaderTextSplitter(
#     headers_to_split_on=headers_to_split_on
# )

docs = text_splitter.split_documents(pages)

print(len(docs))


# for doc in docs:
#     print(doc.page_content)
#     print("------------------------")

embedding = OpenAIEmbeddings()

persistant_directory = 'D:/vscodeproject/python/chroma'

vectordb = Chroma.from_documents(
    documents= docs,
    embedding=embedding,
    persist_directory= persistant_directory,
    collection_name="embedding_data"
)

print(vectordb._collection.count())