from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import OpenAI
import json

embedding = OpenAIEmbeddings()

vectorstore = Chroma(
    persist_directory="D:/workspace/chroma",
    embedding_function=embedding,
    collection_name="embedding_data"
)

llm = OpenAI(temperature=0)
compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectorstore.as_retriever()
)

def pretty_print_docs(docs):
    print(f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]))


question = "What is Patch Shift？"


compressed_docs = compression_retriever.invoke(question)
pretty_print_docs(compressed_docs)

# results = vectorstore.similarity_search(question, k = 3)
# for result in results:
#     print(result)
#     print("--------------")

# client = chromadb.PersistentClient(path="D:/vscodeproject/python/chroma")

# collection = client.get_collection(name="embedding_data")

# all_data = collection.get(include=["documents"])


# # 将数据转换为 JSON 格式
# all_data_json = json.dumps(all_data, indent=4)

# print(all_data)

# with open('D:/workspace/result.txt', 'w') as f1:
#     f1.write(all_data_json)