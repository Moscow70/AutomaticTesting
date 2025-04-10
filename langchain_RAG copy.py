import os
from openai import OpenAI
import bs4
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

api_key = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_API_BASE")

client = OpenAI(
    api_key = api_key,
    base_url = base_url
)

def store_embedding2chroma():
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

def get_doc_from_retrieved_docs(query):
    # 获取Retriever
    vectorstore = store_embedding2chroma()

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
    query = 'What is patch shift?'
    sim_docs = get_doc_from_retrieved_docs(query = query)

    prompt = f"""
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
            If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
            Context: {sim_docs}
            Question: {query}
            Answer:
    """

    response_content = get_completion(prompt)
    print(response_content)