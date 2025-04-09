from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

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