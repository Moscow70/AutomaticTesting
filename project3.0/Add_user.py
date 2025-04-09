from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def add_user(driver):
    # 定位新增按钮并点击
    add_button = driver.find_element(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary .anticon-plus')
    driver.execute_script("arguments[0].click();", add_button)

    time.sleep(1)

    useraccount_drawer_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请输入用户账号']"))
    )
    useraccount_drawer_input.send_keys('testuser')

    username_drawer_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请输入用户姓名']"))
    )
    username_drawer_input.send_keys('测试用户')

    password_drawer_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请输入登录密码']"))
    )
    password_drawer_input.send_keys('123456.a')

    password_reassure_drawer_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请重新输入登录密码']"))
    )
    password_reassure_drawer_input.send_keys('123456.a')

    phonenumber_drawer_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请输入手机号码']"))
    )
    phonenumber_drawer_input.send_keys('13000000000')

    charactor_select = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-selection__rendered') and div[text()='请选择角色']]")
    driver.execute_script("arguments[0].click();", charactor_select)

    option_laborator = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@role='option' and span[@title='实验员']]"))
    )
    option_laborator.click()

    worknumber_drawer_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请输入工号']"))
    )
    worknumber_drawer_input.send_keys('123456')

    # 选择“男”
    male_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='1']")
    male_radio.click()

    time.sleep(1)

    # 选择“女”
    female_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='2']")
    female_radio.click()

    # 点击取消
    cancel_button = driver.find_element(By.XPATH, "//span[text()='取 消']")
    driver.execute_script("arguments[0].click();", cancel_button)

    time.sleep(1)

    # 取消返回
    cancel_sm_button = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-popover-buttons')]//button/span[text()='取 消']")
    driver.execute_script("arguments[0].click();", cancel_sm_button)

    # 确定取消
    # 点击取消
    cancel_button = driver.find_element(By.XPATH, "//span[text()='取 消']")
    driver.execute_script("arguments[0].click();", cancel_button)

    assure_sm_button = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-popover-buttons')]//button/span[text()='确 定']")
    driver.execute_script("arguments[0].click();", assure_sm_button)

    new_user = input("是否需要新建用户？").strip().lower()
    if new_user == 'y':
        # 新增一个测试账号
        add_button = driver.find_element(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary .anticon-plus')
        driver.execute_script("arguments[0].click();", add_button)

        useraccount_drawer_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请输入用户账号']"))
        )
        useraccount_drawer_input.send_keys('testuser')

        username_drawer_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请输入用户姓名']"))
        )
        username_drawer_input.send_keys('测试用户')

        password_drawer_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请输入登录密码']"))
        )
        password_drawer_input.send_keys('123456.a')

        password_reassure_drawer_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请重新输入登录密码']"))
        )
        password_reassure_drawer_input.send_keys('123456.a')

        phonenumber_drawer_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请输入手机号码']"))
        )
        phonenumber_drawer_input.send_keys('13000000000')


        charactor_select = driver.find_element(By.XPATH, "//div[contains(@class, 'ant-select-selection__rendered') and div[text()='请选择角色']]")
        driver.execute_script("arguments[0].click();", charactor_select)

        option_laborator = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@role='option' and span[@title='实验员']]"))
        )
        option_laborator.click()

        worknumber_drawer_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-drawer') and contains(@class, 'ant-drawer-right') and contains(@class, 'ant-drawer-open')]//input[@placeholder='请输入工号']"))
        )
        worknumber_drawer_input.send_keys('123456')

        # 选择“女”
        female_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='2']")
        female_radio.click()

        time.sleep(1)

        # 点击提交
        submit_button = driver.find_element(By.XPATH, "//span[text()='提 交']")
        driver.execute_script("arguments[0].click();", submit_button)