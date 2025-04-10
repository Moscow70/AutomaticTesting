import os
from openai import OpenAI
import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv(dotenv_path=".env", override=True)

api_key = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_API_BASE")

client = OpenAI(
    api_key = api_key,
    base_url = base_url
)

def store_embedding2chroma_web():
    # 创建一个SoupStrainer对象，用于指定要提取的HTML元素
    bs4_trainer = bs4.SoupStrainer(class_ = ("post-title", "post-header", "post-content"))

    # 创建一个WebBaseLoader对象，加载指定的网页路径，并设置解析参数
    loader = WebBaseLoader(
        web_path = ("https://lilianweng.github.io/posts/2023-06-23-agent/",),
        bs_kwargs = {"parse_only":bs4_trainer},
    )
    docs = loader.load()

    textsplitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        add_start_index = True
    )

    splits = textsplitter.split_documents(docs)

    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=OpenAIEmbeddings(model = "text-embedding-3-small", api_key = api_key,
    base_url = base_url),
    )
    return vectordb

def store_embedding2chroma_PDF():
    pdf_loader = PyPDFLoader(
        file_path = "D:/workspace/SIGGRAPH2014_Bilateral texture filtering_2570.pdf",
        extract_images = True
    )

    docs = []

    for page in pdf_loader.load():
        docs.append(page)

    textsplitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        add_start_index = True
    )

    splits = textsplitter.split_documents(docs)

    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=OpenAIEmbeddings(model = "text-embedding-3-small", api_key = api_key,
    base_url = base_url),
    )
    return vectordb


def get_doc_from_retrieved_docs(vectorstore, query):
    # 获取Retriever
    # vectorstore = store_embedding2chroma_web()

    # 使用相似性搜索，返回前3个文档
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    # 执行检索，返回与查询相关的文档
    retrieved_docs = retriever.invoke(query)

    result_docs = "\n\n".join(doc.page_content for doc in retrieved_docs)

    print("=====result_doc=====")
    print(result_docs)
    print("==========")

    return result_docs

def get_completion(prompt, model = "gpt-3.5-turbo"):
    messages = [
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = 0
    )
    print("===============最终回复===============")
    return response.choices[0].message.content


if __name__ == '__main__':

    print("==================以下为读取网页内容的示例======================")

    vectordb_web = store_embedding2chroma_web()

    query_web = 'What are the approaches to Task Decomposition?'
    sim_docs = get_doc_from_retrieved_docs(vectorstore=vectordb_web, query = query_web)

    prompt_web = f"""
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
            If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
            Context: {sim_docs}
            Question: {query_web}
            Answer:
    """

    response_content = get_completion(prompt_web)
    print(response_content)


    print("==================以下为读取本地PDF内容的示例======================")

    vectordb_pdf = store_embedding2chroma_PDF()

    query_pdf = 'What is patch shift?'
    sim_docs = get_doc_from_retrieved_docs(vectorstore=vectordb_pdf, query = query_pdf)

    prompt_pdf = f"""
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
            If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
            Context: {sim_docs}
            Question: {query_pdf}
            Answer:
    """

    response_content = get_completion(prompt_pdf)
    print(response_content)