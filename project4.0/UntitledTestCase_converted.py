# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        # 设置ChromeOptions，防止浏览器自动关闭
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://cn.bing.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://127.0.0.1:9011/")
        driver.find_element(By.XPATH, "//input[@type='text']").click()
        driver.find_element(By.XPATH, "//input[@type='text']").clear()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys("admin")
        driver.find_element(By.XPATH, "//input[@type='password']").click()
        driver.find_element(By.XPATH, "//input[@type='password']").clear()
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456.aA")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//div[@id='app']/section/aside/div/ul/li[2]/div").click()
        driver.find_element(By.LINK_TEXT, "用户管理").click()
        driver.find_element(By.XPATH, "//input[@type='text']").click()
        driver.find_element(By.XPATH, "//input[@type='text']").clear()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys("testuser")
        driver.find_element(By.XPATH, "//button[@type='button']").click()
        driver.find_element(By.XPATH, "//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[6]/span/button[2]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
