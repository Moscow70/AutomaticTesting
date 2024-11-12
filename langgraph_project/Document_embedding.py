from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def load_pdf(state: MyState):
    loader = PyPDFLoader(
        file_path= state['file_path'],
        extract_images= False
    )
    
    pages = list(loader.load())
    print("Document loading Complete!")
    return {"pages": pages}

def embedding_processing(state: MyState, pages):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 0 
    )
    splits = text_splitter.split_documents(pages)
    print("Document splittering Complete!")
    embedding = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(
        documents= splits,
        embedding=embedding,
        persist_directory=state['persist_directory'],
        collection_name=state['collection_name']
    )
    print("Vector database has been created!")
    return {"vectordb": vectordb}