from selenium import webdriver  
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class getCookies:
    def getCookiesFromXueqiu(self,name):
        global cookies
        print name
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
        driver = webdriver.PhantomJS(executable_path='D:/Projects/Projects/craw/xueqiu/influenceSpider/influenceSpider/phantomjs.exe', desired_capabilities=dcap)
        driver.get("https://xueqiu.com/user/login")
        loginname=driver.find_element_by_xpath(".//*[@id='mod-login-email']/label/input")
        loginname.send_keys("13382753152")
        password=driver.find_element_by_xpath(".//*[@id='mod-login-form']/div[2]/label/input")
        password.send_keys("Yutiansut940809")
        form=driver.find_element_by_xpath(".//*[@id='mod-login-form']/div[4]/button")
        form.submit()
        cookies=driver.get_cookies();
        return cookies


