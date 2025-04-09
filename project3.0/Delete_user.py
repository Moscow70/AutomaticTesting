from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def delete_user(driver):
    more_button = driver.find_element(By.XPATH, "//tr[td[text()='测试用户']]//a[text()=' 更多 ']")
    driver.execute_script("arguments[0].click();", more_button)

    delete = driver.find_element(By.XPATH, "//li[@data-v-ee68653c and contains(@class, 'ant-dropdown-menu-item') and ./a[text()='删除']]")

    actions = ActionChains(driver)
    actions.move_to_element(delete).click().perform()

    # 首先，定位到包含“确定删除吗？”文本的ant-popover-message元素
    message_div = driver.find_element(By.XPATH,  "//div[contains(@class, 'ant-popover-message') and .//div[contains(@class, 'ant-popover-message-title') and contains(., '确定删除吗?')]]")
    actions = ActionChains(driver)
    actions.move_to_element(message_div).perform()


    # 然后，从这个元素定位到它的兄弟元素ant-popover-buttons
    buttons_div = message_div.find_element(By.XPATH, "./following-sibling::div[contains(@class, 'ant-popover-buttons')]")

    actions = ActionChains(driver)
    actions.move_to_element(buttons_div).perform()

    # 最后，在这个buttons_div中定位“取消”按钮
    cancel_popover_button = buttons_div.find_element(By.XPATH, ".//button[span[text()='取 消']]")
    actions = ActionChains(driver)

    time.sleep(1)
    actions.move_to_element(cancel_popover_button).click().perform()

    time.sleep(3)

    # 测试确定删除
    more_button = driver.find_element(By.XPATH, "//tr[td[text()='测试用户']]//a[text()=' 更多 ']")
    driver.execute_script("arguments[0].click();", more_button)

    delete = driver.find_element(By.XPATH, "//li[@data-v-ee68653c and contains(@class, 'ant-dropdown-menu-item') and ./a[text()='删除']]")

    actions = ActionChains(driver)
    actions.move_to_element(delete).click().perform()

    # 首先，定位到包含“确定删除吗？”文本的ant-popover-message元素
    message_div = driver.find_element(By.XPATH,  "//div[contains(@class, 'ant-popover-message') and .//div[contains(@class, 'ant-popover-message-title') and contains(., '确定删除吗?')]]")
    actions = ActionChains(driver)
    actions.move_to_element(message_div).perform()


    # 然后，从这个元素定位到它的兄弟元素ant-popover-buttons
    buttons_div = message_div.find_element(By.XPATH, "./following-sibling::div[contains(@class, 'ant-popover-buttons')]")

    actions = ActionChains(driver)
    actions.move_to_element(buttons_div).perform()

    # 最后，在这个buttons_div中定位“确定”按钮
    assure_popover_button = buttons_div.find_element(By.XPATH, ".//button[span[text()='确 定']]")
    actions = ActionChains(driver)

    time.sleep(1)
    actions.move_to_element(assure_popover_button).click().perform()
