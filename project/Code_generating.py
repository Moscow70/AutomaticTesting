from langchain.prompts import PromptTemplate
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai import OpenAI
import os


class codes_generator:

    def __init__(self, vectordb, file_path) :
        self.vectordb = vectordb
        self.file_path = file_path


    def generating_codes(self, template, request):
        if os.path.isdir(self.file_path):
            print("File already exists!")
            return None
        else:
            llm = OpenAI(
                model= "gpt-3.5-turbo-instruct",
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