import os
# from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from spire.pdf.common import *
from spire.pdf import *
from langchain_community.document_loaders.text import TextLoader
import shutil


class document_embedding:
    def __init__(self, file_path, database_persist_directory):
        self.file_path = file_path
        self.dabase_persist_directory = database_persist_directory
        self.file_type = self.get_file_type()

    def get_file_type(self):
        _, file_extension = os.path.splitext(self.file_path)
        file_extension = file_extension.lower()
        if file_extension == '.pdf':
            return 'pdf'
        elif file_extension in ['.doc', '.docx']:
            return 'word'
        elif file_extension == '.txt':
            return 'txt'
        else :
            return 'unknown'

    def load_file(self):
        if self.get_file_type() == 'pdf':
            print("Document Type: PDF!")
            loader = PyPDFLoader(
                file_path=self.file_path,
                extract_images=True
            )
        elif self.get_file_type() == 'word':
            print("Document Type: Word!")
            loader = UnstructuredWordDocumentLoader(
                file_path=self.file_path,
            )
        elif self.get_file_type() == 'txt':
            print("Document Type: TXT!")
            loader = TextLoader(
                file_path=self.file_path,
            )
        else:
            print("File Type Error!")
            return False

        pages = []

        for page in loader.load():
            pages.append(page)

        print("Document loading Complete!")
        return pages        

    def embedding_processing(self, database_name):
        if os.path.isdir(self.dabase_persist_directory):
            print("Do you want to delete the old database? (y/n)")
            user_input = input()
            if user_input.lower() == 'y':
                shutil.rmtree(self.dabase_persist_directory)
                if (os.path.isfile(self.result_directory)):
                    os.remove(self.result_directory)
                print("Database and result files has been deleted!")

        if os.path.isdir(self.dabase_persist_directory):
            collection_name = database_name
            print("Database already exists!")
            vectordb = Chroma(
                persist_directory=self.dabase_persist_directory,
                collection_name=collection_name,
                embedding_function=OpenAIEmbeddings()
            )
        else :
            # if self.get_file_type() == 'pdf':
            #     print("Document Type : PDF")
            #     pages = self.load_pdf()
            # elif self.get_file_type() == 'word':
            #     print("Document Type : Word")
            #     pages = self.load_word()
            # elif self.get_file_type() == 'txt':
            #     print("Document Type : TXT")
            #     pages = self.load_txt()
            # else:
            #     print("File Type Error!")
            #     return False

            pages = self.load_file()
            textsplitter = RecursiveCharacterTextSplitter(
                chunk_size =150,
                chunk_overlap = 30,
                separators=["\n\n", "\n", "(?<=\.)", ",", "========"]
            )
            splits = textsplitter.split_documents(pages)

            if not splits:
                print("No valid text chunks found for embedding.")
                return False
            
            # if embedding is None:
            #     print("Embedding function is not initialized.")
            #     return False
            
            if pages is None:
                print("Failed to load document pages.")
                return False
            else:
                print("Document splitting Complete!")
                # for split in splits:
                #     print(split)
                #     print("--------------------")
                # print(len(splits))
                embedding = OpenAIEmbeddings()
                # persistant_directory = 'D:/workspace/chroma'
                database_persistant_directory = self.dabase_persist_directory

                # print(splits)
                # print(embedding)
                # print(database_persistant_directory) 
                # print(database_name)



                vectordb = Chroma.from_documents(
                    documents= splits,
                    embedding=embedding,
                    persist_directory= database_persistant_directory,
                    collection_name= database_name
                )
                print("Vector database has been created!")
                with open('database_name.txt', 'w') as file:
                    file.write(vectordb._collection_name)
        return vectordb

