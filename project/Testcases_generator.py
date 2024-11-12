from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA
import os

class testcases_generator:

    def __init__(self, vectordb, file_path) :
        self.file_path = file_path
        self.vectordb = vectordb

    def generating_testcases(self, template, request):
        if os.path.isdir(self.file_path):
            print("File already exists!")
            return None
        else:
            llm = ChatOpenAI(
                model= "gpt-4o-mini",
                temperature=0
            )

            final_template = template

            QA_CHAIN_PROMPT = PromptTemplate.from_template(final_template)

            qa_chain = RetrievalQA.from_chain_type(
                llm,
                retriever = self.vectordb.as_retriever(),
                return_source_documents = True,
                chain_type_kwargs= {"prompt": QA_CHAIN_PROMPT}
            )

            final_request = request

            result = qa_chain.invoke({"query": final_request})

            return result["result"]