import os
from dotenv import load_dotenv
from langgraph_definition import run_lanngraph

if __name__ == '__main__':
    load_dotenv(dotenv_path=".env", override= True)

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
    print("Enviroment Setting Complete!")

    document_directory = "D:/workspace/T20241014_YC01_测试用例V2.1.pdf"
    database_directory = "D:/workspace/chroma"
    print(f"Your current document is: {document_directory}")
    print(f"Your current database is: {database_directory}")

    print("===Start Document Processing===")
    run_lanngraph(document_directory, database_directory)