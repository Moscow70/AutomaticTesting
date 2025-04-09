from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def edit_user(driver):

    edit_button = driver.find_element(By.XPATH, "//tr[td[text()='测试用户']]//a[text()='编辑']")
    driver.execute_script("arguments[0].click();", edit_button)

    charactor_select = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-selection__rendered') and div[text()='请选择角色']]")
    driver.execute_script("arguments[0].click();", charactor_select)
    option_laborator = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@role='option' and span[@title='合同管理员']]"))
    )
    option_laborator.click()

    time.sleep(3)

    # 点击提交
    submit_button = driver.find_element(By.XPATH, "//span[text()='提 交']")
    driver.execute_script("arguments[0].click();", submit_button)