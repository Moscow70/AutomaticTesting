from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_part(driver, part):

    # 等待系统管理菜单项加载完成并点击
    system_management_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='系统管理']"))
    )
    system_management_link.click()

    target_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//span[text()='{part}']"))
    )

    # 滚动到用户管理元素的位置
    driver.execute_script("arguments[0].scrollIntoView();", target_link)

    # 使用 JavaScript 执行点击，避免点击拦截
    driver.execute_script("arguments[0].click();", target_link)