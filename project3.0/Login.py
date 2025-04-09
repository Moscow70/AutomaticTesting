from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def login(driver):

    # 等待用户名输入框加载完成
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请输入用户名"]'))
    )

    # 输入用户名
    username_input.send_keys('admin')

    # 等待密码输入框加载完成
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请输入密码"]'))
    )

    # 输入密码
    password_input.send_keys('123456.aA')

    # 等待登录按钮加载完成并点击
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.login-button'))
    )
    login_button.click()

# login_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//span[text()='确 定']"))
# )
# login_button.click()