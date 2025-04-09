from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 定义接口的基本URL
base_url = 'http://127.0.0.1:9011'

# 打开主页面
def open_website(url):
    # 设置ChromeOptions，防止浏览器自动关闭
    options = Options()
    options.add_experimental_option('detach', True)
    # 创建WebDriver实例
    driver = webdriver.Chrome(options=options)
    # 打开指定地址
    driver.get(url)
    return driver     

# 登录管理员账号
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

# 测试新增用户
def Add_user(driver):
    # 定位新增按钮并点击
    add_button = driver.find_element(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary .anticon-plus')
    driver.execute_script("arguments[0].click();", add_button)

    # 定位输入框并输入
    useraccount_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请输入用户账号"]'))
    )
    useraccount_input.send_keys('testuser')

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请输入用户姓名"]'))
    )
    username_input.send_keys('测试用户')

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请输入用户密码"]'))
    )
    password_input.send_keys('123456.aA')

    gender_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请选择用户性别"]'))
    )
    gender_input.send_keys('男')

    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请输入用户手机号码"]'))
    )
    phone_input.send_keys('13088888888')

    status_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="请选择用户状态"]'))
    )
    status_input.send_keys('正常')

    # 提交按钮操作
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    driver.execute_script("arguments[0].click();", submit_button)

    time.sleep(3)

# 执行测试方法
if __name__ == "__main__":
    driver = open_website(base_url)
    login(driver)
    WebDriverWait(driver, 10).until(
        EC.url_changes(base_url)
    )
    time.sleep(3)
    new_url = driver.current_url
    Add_user(driver)
    time.sleep(3)
    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 定义接口的基本URL
base_url = 'http://127.0.0.1:9011'

# 打开主页面
def open_website(url):
    # 设置ChromeOptions，防止浏览器自动关闭
    options = Options()
    options.add_experimental_option('detach', True)
    # 创建WebDriver实例
    driver = webdriver.Chrome(options=options)
    # 打开指定地址
    driver.get(url)
    return driver

# 登录管理员账号
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

# 测试用户角色查看功能
def role_view(driver):
    # 等待角色查看按钮加载完成并点击
    role_view_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="查看角色详情"]'))
    )
    role_view_button.click()

if __name__ == "__main__":
    driver = open_website(base_url)

    login(driver)

    WebDriverWait(driver, 10).until(
        EC.url_changes(base_url)
    )

    time.sleep(3)

    new_url = driver.current_url

    role_view(driver)

    time.sleep(3)