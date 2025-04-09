# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_new_user(self):
        driver = self.driver
        driver.get("http://127.0.0.1:9011/isystem/user")
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[2]/div/div[2]/div/span/div/div/div/div").click()
        driver.find_element_by_xpath("//div[@id='20e64fd8-b16c-4d1e-b452-37f14060abd4']/ul/li").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[6]/span/button[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[2]/div/div[2]/div/span/div/div/div/div").click()
        driver.find_element_by_xpath("//div[@id='20e64fd8-b16c-4d1e-b452-37f14060abd4']/ul/li[2]").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[6]/span/button[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[5]/div/div[2]/div/span/div/div/div/div").click()
        driver.find_element_by_xpath("//div[@id='6dafb44d-297d-40e2-84b6-c9677b83d12f']/ul/li").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[6]/span/button[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[5]/div/div[2]/div/span/div/div/div/div").click()
        driver.find_element_by_xpath("//div[@id='6dafb44d-297d-40e2-84b6-c9677b83d12f']/ul/li[2]").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[6]/span/button[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[4]/div/div[2]/div/span/input").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[4]/div/div[2]/div/span/input").clear()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[4]/div/div[2]/div/span/input").send_keys("13000000000")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[6]/span/button[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[3]/div/div[2]/div/span/input").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[3]/div/div[2]/div/span/input").clear()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[3]/div/div[2]/div/span/input").send_keys(u"测试用户")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/main/div/div/div/div/div/form/div/div[6]/span/button[2]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
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
