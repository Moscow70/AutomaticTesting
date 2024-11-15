import os
from dotenv import load_dotenv
import Document_embedding
import Question_answering
import Testcases_generator
import Code_generating
import Running_codes
import Image_extraction



if __name__ =='__main__':
    
    load_dotenv(dotenv_path=".env", override=True)

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")

    print("Enviroment Settting Complete!")

    document_directory = "D:/workspace/originalfiles/使用手册.docx"

    database_directory = "D:/workspace/database/documents"

    image_directory = "D:/workspace/images"

    print("Your current document is :" + document_directory)
    print("Your current database is :"+ database_directory)

    print("===Start Document Processing===")

    print("Do you want to extract images from files? (y/n)")
    user_input = input().lower()

    if user_input == 'y':
        print("===Start Extracting Images!===")
        image_extraction_bot = Image_extraction.image_extraction(document_directory, image_directory)
        image_extraction_bot.extracting_image()

    summary_directory = 'D:/workspace/output/summary.txt'
    database_name = "document"
    embedding_part = Document_embedding.document_embedding(document_directory, database_directory, summary_directory)

    res = embedding_part.embedding_processing(database_name)
    if res != False:
        vectordb = res
        
        print(f"Document Database size : {(vectordb._collection.count())}")
        template_for_summary = """使用以下上下文来回答最后的问题。 \
        如果你不知道答案，就说你不知道，不要试图编造答案。 \
        回答要尽可能详尽，不要遗漏内容。在回答的最后一定要说“谢谢你的提问” \
        回答要尽量采用原文的说法，尽量详细，并且要分点回答，每一点之间要分行。
        {context}
        问题: {question}
        有用的回答:"""  

        question_for_summary = "根据本文档设计接口测试需求，不需要设计别的测试需求，并且要分点回答，每一点之间要分行。"

        if os.path.isfile(summary_directory):
            print("Summary file exists!Skip the question answering part!")
        else:
            summary_chatbot = Question_answering.question_answering(vectordb, summary_directory)

            print("===Start Question Answering===")
            print("Your question is:"+ question_for_summary)
            summary = summary_chatbot.question_answering(template_for_summary, question_for_summary)

            if summary != None:       
                with open(summary_directory, 'w') as summary_content:
                    summary_content.write(summary)

                print("The summary document has been generated!")
            # print(summary)

        template_for_textcases_generation = """
        按照以下示例，生成对应的测试用例：\
        1.接口测试用例 \
        用例ID：IT-001 \
        用例名称：用户登录功能测试  \
        前提条件: 用户已注册账户 \
        测试步骤: \
            1.用户输入正确的用户名和密码。 \
            2.点击登录按钮。
        在测试步骤结束之后加上以下内容作为测试用例的结束： \
        ========
        {context}
        问题: {question}
        有用的回答:
        """
        quesion_for_textcases_generation = "根据读取的测试需求，按照模板生成测试用例。"

        print("===Start Summary Processing===")
        summary_database_directory = "D:/workspace/database/summary"

        print("Your current summary is :" + summary_directory)
        print("Your current database is :"+ summary_database_directory)

        summary_database_name = "summary"
        testcases_directory = 'D:/workspace/output/testcases.txt'

        embedding_part = Document_embedding.document_embedding(summary_directory, summary_database_directory, testcases_directory)

        summary_vectordb = embedding_part.embedding_processing(summary_database_name)

        print(f"Summary Database size : {(summary_vectordb._collection.count())}")

        if os.path.isfile(testcases_directory):
            print("Testcases file exists!Skip the testcases generating part!")
        else:
            testcasesgenerator_bot = Testcases_generator.testcases_generator(summary_vectordb, testcases_directory)

            print("===Start Generating Testcases===")

            testcases = testcasesgenerator_bot.generating_testcases(template_for_textcases_generation, quesion_for_textcases_generation)

            if testcases!= None:
                with open(testcases_directory, 'w') as testcases_content:
                    testcases_content.write(testcases)

                print("The testcases has been generated!")

        template_for_codes_generation = """
        以数据库中被========分隔符分割的部分为单元，\
        每个单元生成一个测试方法，最终生成完整的测试代码\
        以下是一个例子，代码按照这种格式生成，其中，username和password可以自己生成  \
        
        import requests \
        import json \

        BASE_URL = "http://127.0.0.1:5000/login" \

        #成功的登录测试 \
        def test_valid_login(): \
            
        
        if __name__ == "__main__": \
            test_valid_login() \
            
        注意： \
        1. 每个单元的测试方法名称要与单元中被========分隔符分割的部分保持一致。 \
        2. 每个单元的测试方法中，要按照单元中被========分隔符分割的部分的内容，生成对应的测试用例。 

        {context}
        问题: {question}
        """

        quesion_for_codes_generation = "根据读取的测试用例，按照模板生成代码。"

        testcases_database_directory = "D:/workspace/database/testcases"
        codes_directory = 'D:/workspace/output/codes.txt'


        print("===Start Testcases Processing!===")

        print("Your current testcases is :" + testcases_directory)
        print("Your current database is :"+ testcases_database_directory)

        testcases_database_name = "testcases"
        embedding_part = Document_embedding.document_embedding(testcases_directory, testcases_database_directory, codes_directory)
        testcases_vectordb = embedding_part.embedding_processing(testcases_database_name)

        print(f"Testcases Database size : {(summary_vectordb._collection.count())}")

        if os.path.isfile(codes_directory):
            print("Codes file exists!Skip the code generating part!")
        else:

            print("Start Generating Codes!")
            codegenerator_bot = Code_generating.codes_generator(testcases_vectordb, codes_directory)

            codes = codegenerator_bot.generating_codes(template_for_codes_generation, quesion_for_codes_generation)

            if codes != None:
                with open(codes_directory, 'w') as codes_content:
                    codes_content.write(codes)

                print("The codes has been generated!")
            
        print("===Start Running Codes!===")

        running_codes_bot = Running_codes.running_codes(codes_directory)

        result = running_codes_bot.code_runner()

        with open('D:/workspace/output/result.txt', 'w') as result_content:
            result_content.write(result.stdout)
            result_content.write(result.stderr)

        print("The codes has been running!")

    else :
        print("No database formed!")


