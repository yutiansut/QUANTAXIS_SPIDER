# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
        self.driver = webdriver.PhantomJS(executable_path='D:/Projects/Projects/craw/resource/phantomjs.exe', desired_capabilities=dcap)
        self.driver.implicitly_wait(30)
        self.base_url = "https://xueqiu.com/user/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        # open | https://xueqiu.com/1257229315 | 
        driver.get("https://xueqiu.com/1257229315")
        # assertTitle 
        # self.assertEqual(u"我的首页 - 雪球", driver.title)
        # type | id=pop_username | 13382753152
        driver.find_element_by_id("pop_username").clear()
        driver.find_element_by_id("pop_username").send_keys("13382753152")
        # type | id=pop_password | Yutiansut940809
        driver.find_element_by_id("pop_password").clear()
        driver.find_element_by_id("pop_password").send_keys("Yutiansut940809")
        # click | link=精华 | 
        driver.find_element_by_link_text(u"精华").click()
        # click | link=找人 | 
        driver.find_element_by_link_text(u"找人").click()
        # assertTitle | 找人 - 雪球 | 
        self.assertEqual(u"找人 - 雪球", driver.title)
        # click | css=span.screen_name | 
        driver.find_element_by_css_selector("span.screen_name").click()
        # type | id=pop_username | 13382753152
        driver.find_element_by_id("pop_username").clear()
        driver.find_element_by_id("pop_username").send_keys("13382753152")
        # type | id=pop_password | Yutiansut940809
        driver.find_element_by_id("pop_password").clear()
        driver.find_element_by_id("pop_password").send_keys("Yutiansut940809")
        # type | id=remark | s
        driver.find_element_by_id("remark").clear()
        driver.find_element_by_id("remark").send_keys("s")
        # click | css=p.submit > input.submit | 
        driver.find_element_by_css_selector("p.submit > input.submit").click()
        # click | css=b.caret | 
        driver.find_element_by_css_selector("b.caret").click()
        # click | link=找人 | 

    
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