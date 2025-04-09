from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def user_detail(driver):
    more_button = driver.find_element(By.XPATH, "//tr[td[text()='测试用户']]//a[text()=' 更多 ']")
    driver.execute_script("arguments[0].click();", more_button)

    detail = driver.find_element(By.XPATH, "//li[@data-v-ee68653c and contains(@class, 'ant-dropdown-menu-item') and ./a[text()='详情']]")

    actions = ActionChains(driver)
    actions.move_to_element(detail).click().perform()

    time.sleep(3)

    # 定位关闭按钮并点击
    close_button = driver.find_element(By.CSS_SELECTOR, 'button.ant-drawer-close .anticon-close')
    driver.execute_script("arguments[0].click();", close_button)