# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://xueqiu.com/user/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        # open | https://xueqiu.com/user/login | 
        driver.get("https://xueqiu.com/user/login")
        # assertTitle | 登录 - 雪球 | 
        self.assertEqual(u"登录 - 雪球", driver.title)
        # type | name=username | 13382753152
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("13382753152")
        # type | name=password | Yutiansut940809
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("Yutiansut940809")
        # click | name=remember_me | 
        driver.find_element_by_name("remember_me").click()
        # click | css=button.button | 
        driver.find_element_by_css_selector("button.button").click()
        # assertTitle | 我的首页 - 雪球 | 
        self.assertEqual(u"我的首页 - 雪球", driver.title)
        # type | id=pop_username | 13382753152
        driver.find_element_by_id("pop_username").clear()
        driver.find_element_by_id("pop_username").send_keys("13382753152")
        # type | id=pop_password | Yutiansut940809
        driver.find_element_by_id("pop_password").clear()
        driver.find_element_by_id("pop_password").send_keys("Yutiansut940809")
        # click | id=head | 
        driver.find_element_by_id("head").click()
    
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
