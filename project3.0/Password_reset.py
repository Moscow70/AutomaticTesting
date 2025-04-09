from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def password_reset(driver):
    # 点击重置密码按钮
    more_button = driver.find_element(By.XPATH, "//tr[td[text()='测试用户']]//a[text()=' 更多 ']")
    driver.execute_script("arguments[0].click();", more_button)

    reset_password = driver.find_element(By.XPATH, "//li[@data-v-ee68653c and contains(@class, 'ant-dropdown-menu-item') and ./a[text()='密码重置']]")

    actions = ActionChains(driver)
    actions.move_to_element(reset_password).click().perform()

    password_modal_input = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-modal-content')]//input[@placeholder='请输入登录密码']")
    password_modal_input.send_keys('123456.b')

    time.sleep(1)

    password_modal_reassure_input = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-modal-content')]//input[@placeholder='请重新输入登录密码']")
    password_modal_reassure_input.send_keys('123456.b')

    time.sleep(3)

    # 点击关闭
    cancel_button = driver.find_element(By.XPATH, "//span[text()='关 闭']")
    driver.execute_script("arguments[0].click();", cancel_button)

    time.sleep(1)

    # 点击重置密码按钮
    more_button = driver.find_element(By.XPATH, "//tr[td[text()='测试用户']]//a[text()=' 更多 ']")
    driver.execute_script("arguments[0].click();", more_button)

    reset_password = driver.find_element(By.XPATH, "//li[@data-v-ee68653c and contains(@class, 'ant-dropdown-menu-item') and ./a[text()='密码重置']]")

    actions = ActionChains(driver)
    actions.move_to_element(reset_password).click().perform()

    password_modal_input = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-modal-content')]//input[@placeholder='请输入登录密码']")
    password_modal_input.send_keys('123456.b')

    time.sleep(1)

    password_modal_reassure_input = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-modal-content')]//input[@placeholder='请重新输入登录密码']")
    password_modal_reassure_input.send_keys('123456.b')

    time.sleep(3)

    # 点击确定
    # assure_button = driver.find_element(By.XPATH, "//span[text()='确 定']")

    assure_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='确 定']"))
    )
    driver.execute_script("arguments[0].click();", assure_button)