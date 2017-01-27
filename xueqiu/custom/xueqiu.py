# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
        self.driver = webdriver.PhantomJS(executable_path='D:/Projects/Projects/craw/resource/phantomjs.exe', desired_capabilities=dcap)
        self.driver.implicitly_wait(30)
        self.base_url = "https://xueqiu.com/people"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        # open | https://xueqiu.com/people | 
        driver.get("https://xueqiu.com/people")
        # assertTitle | 找人 - 雪球 | 
        self.assertEqual(u"找人 - 雪球", driver.title)
        # click | link=雪球官方 | 
        driver.find_element_by_link_text(u"雪球官方").click()
        # click | link=美股达人 | 
        driver.find_element_by_link_text(u"美股达人").click()
        # click | link=港股达人 | 
        driver.find_element_by_link_text(u"港股达人").click()
        # click | link=基金达人 | 
        driver.find_element_by_link_text(u"基金达人").click()
        # click | link=房地产 | 
        driver.find_element_by_link_text(u"房地产").click()
        # click | link=银行业 | 
        driver.find_element_by_link_text(u"银行业").click()
        # click | link=医药业 | 
        driver.find_element_by_link_text(u"医药业").click()
        # click | link=TMT | 
        driver.find_element_by_link_text("TMT").click()
        # click | link=能源环保 | 
        driver.find_element_by_link_text(u"能源环保").click()
        # click | link=A股投资达人 | 
        driver.find_element_by_link_text(u"A股投资达人").click()
        # click | link=滚雪球小帮手 | 
        driver.find_element_by_link_text(u"滚雪球小帮手").click()
        # click | link=雪球达人秀 | 
        driver.find_element_by_link_text(u"雪球达人秀").click()
        # click | link=雪球新兴实力派 | 
        driver.find_element_by_link_text(u"雪球新兴实力派").click()
        # click | link=ETF与公募基金 | 
        driver.find_element_by_link_text(u"ETF与公募基金").click()
        # click | link=私募达人 | 
        driver.find_element_by_link_text(u"私募达人").click()
        # click | link=中小盘成长股 | 
        driver.find_element_by_link_text(u"中小盘成长股").click()
        # click | link=低风险投资 | 
        driver.find_element_by_link_text(u"低风险投资").click()
        # click | link=技术趋势派 | 
        driver.find_element_by_link_text(u"技术趋势派").click()
        # click | link=分级基金达人 | 
        driver.find_element_by_link_text(u"分级基金达人").click()
        # click | link=并购重组 | 
        driver.find_element_by_link_text(u"并购重组").click()
        # click | link=主题投资 | 
        driver.find_element_by_link_text(u"主题投资").click()
        # click | link=财务分析达人 | 
        driver.find_element_by_link_text(u"财务分析达人").click()
        # click | link=投资新秀 | 
        driver.find_element_by_link_text(u"投资新秀").click()
        # click | link=公募/私募 | 
        driver.find_element_by_link_text(u"公募/私募").click()
        # click | link=分析师/研究员 | 
        driver.find_element_by_link_text(u"分析师/研究员").click()
        # click | link=策略/宏观 | 
        driver.find_element_by_link_text(u"策略/宏观").click()
        # click | link=软件与互联网服务 | 
        driver.find_element_by_link_text(u"软件与互联网服务").click()
        # click | link=电子设备及服务 | 
        driver.find_element_by_link_text(u"电子设备及服务").click()
        # click | link=通信设备与服务 | 
        driver.find_element_by_link_text(u"通信设备与服务").click()
        # click | link=银证保信托 | 
        driver.find_element_by_link_text(u"银证保信托").click()
        # click | link=食品饮料 | 
        driver.find_element_by_link_text(u"食品饮料").click()
        # click | link=电商零售 | 
        driver.find_element_by_link_text(u"电商零售").click()
        # click | link=纺织服装 | 
        driver.find_element_by_link_text(u"纺织服装").click()
        # click | link=旅游餐饮 | 
        driver.find_element_by_link_text(u"旅游餐饮").click()
        # click | link=家电家居日化 | 
        driver.find_element_by_link_text(u"家电家居日化").click()
        # click | link=农林牧渔 | 
        driver.find_element_by_link_text(u"农林牧渔").click()
        # click | link=交运与汽车 | 
        driver.find_element_by_link_text(u"交运与汽车").click()
        # click | link=采掘 | 
        driver.find_element_by_link_text(u"采掘").click()
        # click | link=化工 | 
        driver.find_element_by_link_text(u"化工").click()
        # click | link=金属新材料 | 
        driver.find_element_by_link_text(u"金属新材料").click()
        # click | link=建筑建材 | 
        driver.find_element_by_link_text(u"建筑建材").click()
        # click | link=LED节能环保 | 
        driver.find_element_by_link_text(u"LED节能环保").click()
        # click | link=文体娱乐 | 
        driver.find_element_by_link_text(u"文体娱乐").click()
        # click | link=量化投资 | 
        driver.find_element_by_link_text(u"量化投资").click()
        # click | link=可转债 | 
        driver.find_element_by_link_text(u"可转债").click()
        # click | link=期货股指对冲 | 
        driver.find_element_by_link_text(u"期货股指对冲").click()
        # click | link=军工国防 | 
        driver.find_element_by_link_text(u"军工国防").click()
        # click | link=资产配置 | 
        driver.find_element_by_link_text(u"资产配置").click()
        # click | link=商业逻辑 | 
        driver.find_element_by_link_text(u"商业逻辑").click()
        # click | link=蓝筹股投资者 | 
        driver.find_element_by_link_text(u"蓝筹股投资者").click()
        # click | link=投资顾问 | 
        driver.find_element_by_link_text(u"投资顾问").click()
        # click | link=媒体/研报 | 
        driver.find_element_by_link_text(u"媒体/研报").click()
        # click | id=userRecommend | 
        driver.find_element_by_id("userRecommend").click()
        # click | //div[@id='center']/div/div[2]/div/div/div[2]/ul/li/div/div/a[2]/span | 
        driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div/div/div[2]/ul/li/div/div/a[2]/span").click()
        # type | id=pop_username | 13382753152
        driver.find_element_by_id("pop_username").clear()
        driver.find_element_by_id("pop_username").send_keys("13382753152")
        # type | id=pop_password | Yutiansut940809
        driver.find_element_by_id("pop_password").clear()
        driver.find_element_by_id("pop_password").send_keys("Yutiansut940809")
        # click | link=阿里高管解读财报：数字媒体和娱乐业务亏损率将收窄 | 
        driver.find_element_by_link_text(u"阿里高管解读财报：数字媒体和娱乐业务亏损率将收窄").click()
        # type | id=pop_username | 13382753152
        driver.find_element_by_id("pop_username").clear()
        driver.find_element_by_id("pop_username").send_keys("13382753152")
        # type | id=pop_password | Yutiansut940809
        driver.find_element_by_id("pop_password").clear()
        driver.find_element_by_id("pop_password").send_keys("Yutiansut940809")
        # type | id=remark | S
        driver.find_element_by_id("remark").clear()
        driver.find_element_by_id("remark").send_keys("S")
        # click | css=p.submit > input.submit | 
        driver.find_element_by_css_selector("p.submit > input.submit").click()
        # click | link=精华 | 
        driver.find_element_by_link_text(u"精华").click()
        # click | link=找人 | 
        driver.find_element_by_link_text(u"找人").click()
        # assertTitle | 找人 - 雪球 | 
        self.assertEqual(u"找人 - 雪球", driver.title)
        # click | //div[@id='center']/div/div[2]/div/div/div[2]/ul/li[2]/div/div/a[2]/span | 
        driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div/div/div[2]/ul/li[2]/div/div/a[2]/span").click()
        # type | id=pop_username | 13382753152
        driver.find_element_by_id("pop_username").clear()
        driver.find_element_by_id("pop_username").send_keys("13382753152")
        # type | id=pop_password | Yutiansut940809
        driver.find_element_by_id("pop_password").clear()
        driver.find_element_by_id("pop_password").send_keys("Yutiansut940809")
        # click | css=table.cubes > tbody > tr > td > a | 
        driver.find_element_by_css_selector("table.cubes > tbody > tr > td > a").click()
        # type | id=pop_username | 13382753152
        driver.find_element_by_id("pop_username").clear()
        driver.find_element_by_id("pop_username").send_keys("13382753152")
        # type | id=pop_password | Yutiansut940809
        driver.find_element_by_id("pop_password").clear()
        driver.find_element_by_id("pop_password").send_keys("Yutiansut940809")
        # click | //div[@id='cube-weight']/div[2]/div[2]/div[4] | 
        driver.find_element_by_xpath("//div[@id='cube-weight']/div[2]/div[2]/div[4]").click()
        # click | link=全部 | 
        driver.find_element_by_link_text(u"全部").click()
        # click | link=共同关注 | 
        driver.find_element_by_link_text(u"共同关注").click()
        # click | link=沪深 | 
        driver.find_element_by_link_text(u"沪深").click()
        # click | link=全部 | 
        driver.find_element_by_link_text(u"全部").click()
        # click | css=div.more.showMore | 
        driver.find_element_by_css_selector("div.more.showMore").click()
        # click | //div[@id='center']/div/div[2]/div[5]/div/ul/li[5]/a/small | 
        driver.find_element_by_xpath("//div[@id='center']/div/div[2]/div[5]/div/ul/li[5]/a/small").click()
        # click | css=div.name > a > span | 
        driver.find_element_by_css_selector("div.name > a > span").click()
        # type | id=pop_username | 13382753152
        driver.find_element_by_id("pop_username").clear()
        driver.find_element_by_id("pop_username").send_keys("13382753152")
        # type | id=pop_password | Yutiansut940809
        driver.find_element_by_id("pop_password").clear()
        driver.find_element_by_id("pop_password").send_keys("Yutiansut940809")
    
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