from openai import OpenAI
import os
from dotenv import load_dotenv
import Document_splitting
import Document_embedding
import Question_answering

load_dotenv(dotenv_path="../.env", override=True)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")

def get_response(system_prompt, user_prompt):
    """调用OpenAI API获取响应"""
    client = OpenAI(
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )
    return response.choices[0].message.content

def process_document_parts(system_prompt, parts, html_code_vectordb, code_directory):
    """处理长文档并获取响应"""
    responses = []
    i = 0
    nums = len(parts)

    template_for_searching_code = """
    根据切割的文档片段搜索网页代码数据库中与之相关的片段。\
    不可以对读取出的代码作任何的修改，必须直接输出读取到的代码部分。\
    {context}
    问题：{question}
    有用的回答：
    """
    question_for_searching_code = "根据读取到的文档片段搜索数据库中的网页代码。"

    generated_code = ""
    responses = []

    for i, part in enumerate(parts, start=1):
        # 找到当前代码对应的网页代码
        code_chatbot = Question_answering.question_answering(html_code_vectordb, code_directory)
        code_part = code_chatbot.question_answering(template_for_searching_code, question_for_searching_code)

        print(code_part)
        # 构建完整的用户提示
        user_prompt = prompt_template.format(
            output_format=output_format,
            input=input,
            ai_answer_1=ai_answer_1,
            question=question,
            document=part,
            code=code_part,
            generated_code = generated_code
        )
        # i = i + 1
        response = get_response(system_prompt, user_prompt)
        generated_code += response + "\n"

        print(f"{i}/{nums}")
    responses = generated_code.strip()
    return responses

if __name__ == "__main__":
    # 指定文件路径
    file_path = "D:/workspace/originalfiles/CASC-STEC-PT011能力验证统软件需求规格说明_用户管理.pdf"

    system_prompt = """
    - 你是一个软件测试工程师，你需要根据读入的文档生成对应的接口测试代码，要全面地覆盖文档中出现的情况。
    - 你的回答必须以python语言的格式，如果需要文字解释的部分，要以注释的形式，也就是每一行前面加上#出现。
    - 你必须使用selenium插件来进行测试。
    - 在每个测试功能完成后，使用time.sleep(3)来等待3秒。
    - 对于每一个测试用例，都需要使用一个测试方法来表现。
    - 头文件、打开主页面和登录管理员账号、main函数本身以及调用打开主页面和登录管理员账号两个方法的部分在完整代码中均只出现一次。
    - 不要每次都从头文件开始生成整个代码文件，而是仅生成新的方法代码，并插入现有的代码中。
    - 在整个文档读取结束前，生成的代码会被重新传回大模型，新的代码就插入这份被传回的代码中。
    - 'main'函数负责调用所有已定义的方法，生成的所有方法都要在main函数里按顺序进行正确的调用。
    - 不要在生成的代码前后添加额外的标记，如```python```。
    """
    output_format = """
    from selenium import webdriver \
    from selenium.webdriver.common.by import By \
    from selenium.webdriver.common.keys import Keys \
    from selenium.webdriver.chrome.options import Options \
    from selenium.webdriver.support.ui import WebDriverWait \
    from selenium.webdriver.support import expected_conditions as EC \
    from selenium.webdriver.common.action_chains import ActionChains \
    import time \
    
    
    # 定义接口的基本URL
    base_url = 'http://127.0.0.1:9011'

    # 打开主页面
    def open_website(url): \
        # 设置ChromeOptions，防止浏览器自动关闭 \
        options = Options() \
        options.add_experimental_option('detach', True) \
        # 创建WebDriver实例 \
        driver = webdriver.Chrome(options=options) \
        # 打开指定地址 \
        driver.get(url) \
        return driver \
        
    # 登录管理员账号
    def login(driver): \
        # 等待用户名输入框加载完成 \
        username_input = WebDriverWait(driver, 10).until( \
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请输入用户名"]')) \
        ) \
        # 输入用户名 \
        username_input.send_keys('admin') \
        # 等待密码输入框加载完成 \
        password_input = WebDriverWait(driver, 10).until( \
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请输入密码"]')) \
        ) \
        # 输入密码 \
        password_input.send_keys('123456.aA') \
        # 等待登录按钮加载完成并点击 \
        login_button = WebDriverWait(driver, 10).until( \
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.login-button')) \
        ) \
        login_button.click() \

    # 测试某一功能
    def {function_name}(driver): \
        if __name__ == "__main__": \
        driver = open_website(base_url) \
        
        login(driver) \
        
        WebDriverWait(driver, 10).until( \
            EC.url_changes(base_url) \
        ) \

        time.sleep(3) \
        
        new_url = driver.current_url \

        # 调用测试方法        
        {function_name}(driver) \
        \
    """

    input = """
    根据用户账号、性别、用户姓名、手机号码和状态模糊查询符合条件的用户。 \
    """

    ai_answer_1 = """
    # 测试查询用户
    def click_search(driver):
        # 点击查询按钮
        search_button = driver.find_element(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary .anticon-search')
        driver.execute_script("arguments[0].click();", search_button)

    def click_reload(driver):
        # 点击重置按钮
        reload_button = driver.find_element(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary .anticon-reload')
        driver.execute_script("arguments[0].click();", reload_button)


    def search_user(driver):
        # 通过用户账号查询用户
        useraccount_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="请输入用户账号"]'))
        )
        useraccount_input.send_keys('kcgly')

        click_search(driver)

        time.sleep(2)

        click_reload(driver)

        # 通过手机号查询用户
        phonenumber_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="请输入手机号码"]'))
        )
        phonenumber_input.send_keys('15234252654')

        click_search(driver)

        time.sleep(2)

        click_reload(driver)

        # 通过用户姓名查询用户
        username_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="请输入用户姓名"]'))
        )
        username_input.send_keys('实验管理员')

        click_search(driver)

        time.sleep(2)

        click_reload(driver)

        # 通过性别筛选用户
        # 等待性别选择框加载完成并点击以展开下拉菜单
        # 定位到下拉菜单

        gender_select = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-selection__rendered') and div[text()='请选择性别']]")
        driver.execute_script("arguments[0].click();", gender_select)

        option_male = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), '男')]"))
        )
        option_male.click()

        click_search(driver)

        time.sleep(2)

        click_reload(driver)

        gender_select = driver.find_element(By.CLASS_NAME, 'ant-select-selection__rendered')
        driver.execute_script("arguments[0].click();", gender_select)

        option_female = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), '女')]"))
        )
        option_female.click()

        click_search(driver)

        time.sleep(2)

        click_reload(driver)


        # 通过状态筛选用户
        # 等待状态选择框加载完成并点击以展开下拉菜单
        # 定位到下拉菜单

        status_select = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-selection__rendered') and div[text()='请选择状态']]")
        driver.execute_script("arguments[0].click();", status_select)

        status_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), '正常')]"))
        )
        status_option.click()

        click_search(driver)

        time.sleep(2)

        click_reload(driver)

        status_select = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-selection__rendered') and div[text()='请选择状态']]")
        driver.execute_script("arguments[0].click();", status_select)

        status_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), '冻结')]"))
        )
        status_option.click()

        click_search(driver)

        time.sleep(2)

        click_reload(driver)
    if __name__ == "__main__": \    
        search_user(driver) \
        
        time.sleep(3) \
    \
    """    
    question = "根据以下文档内容，按照格式生成对应的接口测试代码。需求在文档中集中在用户管理部分，并已经按点分好，每一点对应一个需求，所以请按点分割文档，其它部分仅为补充说明。"

    with open('D:/vscodeproject/python/project2.0/rendered_example.txt', 'r', encoding='utf-8') as file:
        code = file.read()

    prompt_template = """
    - 目标：负责接收一个测试文档，生成对应的接口测试代码。
    - 输出格式：以一个可以直接运行的python脚本的格式输出。
    - 以下是输出的格式，请严格按照此格式输出：
    {output_format}

    **示例：**
    - 输入：{input}
    - 输出：{ai_answer_1}

    **用户问题**：{question}
    **用户文档**：{document}
    **网页代码**：{code}
    **已生成的代码**：{generated_code}

    """

    # 构建网页代码知识库
    code_directory = 'D:/vscodeproject/python/project2.0/rendered_example.txt'
    code_database_directory = "D:/workspace/database/html_code"
    database_name = "html_code"
    embedding_part = Document_embedding.document_embedding(code_directory, code_database_directory)
    vectordb = embedding_part.embedding_processing(database_name)

    # 创建DocumentProcessor实例
    processor = Document_splitting.DocumentProcessor(max_length=1500, overlap_length=0)

    # 处理文档并获取切割后的部分
    parts = processor.process_document(file_path)

    for part in parts:
        print(part)
        print("-------------------")


    # 处理文档并获取响应
    responses = process_document_parts(system_prompt, parts, vectordb, code_directory)

    code_path = "D:/vscodeproject/python/project2.0/code_2.py"

    # 打印所有响应
    with open(code_path, 'w') as code_content:
        for i, response in enumerate(responses):
            # print(f"Part {i + 1} Response: {response}")
            code_content.write(response)