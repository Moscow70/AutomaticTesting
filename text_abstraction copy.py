import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from spire.pdf.common import *
from spire.pdf import *
import pytesseract
from PIL import Image
import asyncio
from langchain_openai import OpenAI
from ratelimit import limits, sleep_and_retry

load_dotenv(dotenv_path=".env", override=True)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")

# 定义速率限制装饰器，每分钟最多3个请求
@sleep_and_retry
@limits(calls=1, period=180)
def rate_limited_openai_call(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

class RateLimitedOpenAIEmbeddings(OpenAIEmbeddings):
    @rate_limited_openai_call
    def embed_text(self, text):
        return super().embed_text(text)

class RateLimitedOpenAI(OpenAI):
    @rate_limited_openai_call
    def call(self, **kwargs):
        return super().call(**kwargs)

@rate_limited_openai_call
def perform_retriever_operations(question, llm, vectordb):
    # 创建速率限制的LLMChainExtractor实例
    compressor = LLMChainExtractor.from_llm(llm)
    
    # 创建速率限制的ContextualCompressionRetriever实例
    compressor_retriever = ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=vectordb.as_retriever()
    )
    
    # 执行查询并返回结果
    return compressor_retriever.invoke(question)

def load_pdf():
    loader = PyPDFLoader(
        file_path= "D:/workspace/T20241014_YC01_测试用例V2.1.pdf",
        extract_images=True
    )    

    pages = []

    for page in loader.load():
        pages.append(page)

    return pages

def main():
    pages = load_pdf()
    textsplitter = RecursiveCharacterTextSplitter(
        chunk_size =300,
        chunk_overlap = 30
    )
    splits = textsplitter.split_documents(pages)

    # for split in splits:
    #     print(split)
    #     print("--------------------")
    # print(len(splits))
    embedding = RateLimitedOpenAIEmbeddings()
    persistant_directory = 'D:/vscodeproject/python/chroma'
    vectordb = Chroma.from_documents(
        documents= splits,
        embedding=embedding,
        persist_directory= persistant_directory,
        collection_name="embedding_data"
    )
    # print(vectordb._collection.count())

    llm = RateLimitedOpenAI(temperature=0)
    # compressor = LLMChainExtractor.from_llm(llm)
    # compressor_retriever = ContextualCompressionRetriever(
    #     base_compressor=compressor,
    #     base_retriever=vectordb.as_retriever()
    # )
    def pretty_print_docs(docs):
        print(f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]))


    question = "该篇文章的测试内容有哪些？给出全部的测试内容，不要重复"

    # res = vectordb.similarity_search(question, k = 3)
    # MMR效果很差
    # res = vectordb.max_marginal_relevance_search(question, k = 3)
    res = perform_retriever_operations(question, llm, vectordb)
    # res = compressor_retriever.invoke(question)
    pretty_print_docs(res)
    # print(res[0].page_content)

if __name__ == "__main__":
    main()