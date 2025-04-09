from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import Open_website
import Login
import Find_part

def save_rendered_html(url, filename):
    driver = Open_website.open_website(url)

    Login.login(driver)

    WebDriverWait(driver, 10).until(
        EC.url_changes('http://127.0.0.1:9011')
    )

    welcome_url = driver.current_url

    Find_part.find_part(driver, '用户管理')
    WebDriverWait(driver, 10).until(
        EC.url_changes(welcome_url)
    )
    print("New URL after clicking 'User Management':", driver.current_url)

    time.sleep(10)


    html_content = driver.page_source
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"已成功保存渲染后的HTML为 {filename}")


# 示例：保存某个网页的渲染后HTML代码
url = 'http://127.0.0.1:9011'
filename = "rendered_example.txt"
save_rendered_html(url, filename)