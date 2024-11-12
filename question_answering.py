from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA
import json

embedding = OpenAIEmbeddings()

vectorstore = Chroma(
    persist_directory="D:/workspace/chroma",
    embedding_function=embedding,
    collection_name="embedding_data"
)

llm = ChatOpenAI(temperature=0)

template = """使用以下上下文来回答最后的问题。 \
如果你不知道答案，就说你不知道，不要试图编造答案。 \
回答要尽可能详尽，不要遗漏内容。在回答的最后一定要说“谢谢你的提问” \
回答要尽量采用原文的说法，并且要分点回答，每点占据一行
{context}
问题: {question}
有用的回答:"""

QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever = vectorstore.as_retriever(),
    return_source_documents = True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)


question = "本文提到的所有的测试目的及其测试内容有哪些？"

result = qa_chain.invoke({"query":question})
print(result["result"])