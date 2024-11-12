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

def extract_images_from_pdf(pdf_path, output_dir):
    """
    从PDF中提取所有图片，并将其保存到指定的输出目录中
    参数：
        pdf_path(str)：输入路径
        output_dir(str): 输出路径
    """
    doc = PdfDocument()
    doc.LoadFromFile(pdf_path)

    image_helper = PdfImageHelper()

    image_count = 1

    for page_index in range(doc.Pages.Count):
        page = doc.Pages[page_index]
        # 获取页面信息
        image_infos = image_helper.GetImagesInfo(page)

        # 提取并保存
        for image_index in range(len(image_infos)):
            # 指定输出文件
            output_file = os.path.join(output_dir, f"Image-{image_count}.png")
            # 保存为图片文件
            image_infos[image_index].Image.Save(output_file)
            image_count += 1
        
    doc.Close()

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




# async def load_pdf():
#     loader = PyPDFLoader(
#         file_path= "D:/workspace/T20241014_YC01_测试用例V2.1.pdf",
#         extract_images=True
#     )    

#     pages = []

#     async for page in loader.alazy_load():
#         pages.append(page)

#     return pages

def load_pdf():
    loader = PyPDFLoader(
        file_path= "D:/workspace/T20241014_YC01_测试用例V2.1.pdf",
        extract_images=True
    )    

    pages = []

    for page in loader.load():
        pages.append(page)

    return pages



# async def main():
#     pages = await load_pdf()
#     textsplitter = RecursiveCharacterTextSplitter(
#         chunk_size =300,
#         chunk_overlap = 30
#     )
#     splits = textsplitter.split_documents(pages)

#     # for split in splits:
#     #     print(split)
#     #     print("--------------------")
#     # print(len(splits))
#     embedding = OpenAIEmbeddings()
#     persistant_directory = 'D:/vscodeproject/python/chroma'
#     vectordb = Chroma.from_documents(
#         documents= splits,
#         embedding=embedding,
#         persist_directory= persistant_directory
#     )
#     # print(vectordb._collection.count())

#     llm = OpenAI(temperature=0)
#     compressor = LLMChainExtractor.from_llm(llm)
#     compressor_retriever = ContextualCompressionRetriever(
#         base_compressor=compressor,
#         base_retriever=vectordb.as_retriever()
#     )
#     def pretty_print_docs(docs):
#         print(f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]))


#     question = "该篇文章的测试内容有哪些？给出全部的测试内容，不要重复"

#     # res = vectordb.similarity_search(question, k = 3)
#     # MMR效果很差
#     # res = vectordb.max_marginal_relevance_search(question, k = 3)

#     res = compressor_retriever.invoke(question)
#     pretty_print_docs(res)


#     # extract_images_from_pdf("D:/workspace/T20241014_YC01_测试用例V2.1.pdf", "D:/workspace/image")
    
#     # try:
#     #     image = Image.open('D:/workspace/image/Image-8.png')
#     #     text = pytesseract.image_to_string(image, lang='chi_sim')

#     #     with open('D:/workspace/output.txt', 'w') as f:
#     #         f.write(text)
#     # except Exception as e:
#     #     print("No image detected")
#     # else :
#     #     print("Image detected")
#     # finally:
#     #     # print(len(splits))
#     #     # print(splits[1])
#     #     with open('D:/workspace/result_1.txt', 'w') as f1:
#     #         f1.write(res[0].page_content)
#     #     with open('D:/workspace/result_2.txt', 'w') as f2:
#     #         f2.write(res[1].page_content)
#     #     with open('D:/workspace/result_3.txt', 'w') as f3:
#     #         f3.write(res[2].page_content)
#     #     # print("-----------------------")
#     #     # print(res[0].page_content)
#     #     # print("-----------------------")
#     #     # print(res[1].page_content)
#     #     # print("-----------------------")
#     #     # print(res[2].page_content)

# asyncio.run(main())


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


extract_images_from_pdf("D:/workspace/T20241014_YC01_测试用例V2.1.pdf", "D:/workspace/image")

try:
    image = Image.open('D:/workspace/image/Image-8.png')
    text = pytesseract.image_to_string(image, lang='chi_sim')

    with open('D:/workspace/output.txt', 'w') as f:
        f.write(text)
except Exception as e:
    print("No image detected")
else :
    print("Image detected")
finally:
    # print(len(splits))
    # print(splits[1])
    with open('D:/workspace/result_1.txt', 'w') as f1:
        f1.write(res[0].page_content)
    with open('D:/workspace/result_2.txt', 'w') as f2:
        f2.write(res[1].page_content)
    with open('D:/workspace/result_3.txt', 'w') as f3:
        f3.write(res[2].page_content)
    # print("-----------------------")
    # print(res[0].page_content)
    # print("-----------------------")
    # print(res[1].page_content)
    # print("-----------------------")
    # print(res[2].page_content)