from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def open_website(url):

    # 设置ChromeOptions，防止浏览器自动关闭
    options = Options()
    options.add_experimental_option('detach', True)

    # 创建WebDriver实例
    driver = webdriver.Chrome(options=options)

    # 打开指定地址
    driver.get(url)
    return driver