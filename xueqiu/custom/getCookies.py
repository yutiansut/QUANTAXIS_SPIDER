from selenium import webdriver  
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

class getCookies:
    def getCookiesFromXueqiu(self,name):
        global cookies
        print name
        print '===Using Python V2.7.11 X64==='
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
        driver = webdriver.PhantomJS(executable_path='D:/Projects/Projects/craw/resource/phantomjs.exe', desired_capabilities=dcap)
        driver.get("https://xueqiu.com/user/login")
        print '===getCookies==='
        loginname=driver.find_element_by_xpath(".//*[@id='mod-login-email']/label/input")
        loginname.send_keys("13382753152")
        password=driver.find_element_by_xpath(".//*[@id='mod-login-form']/div[2]/label/input")
        password.send_keys("Yutiansut940809")
        form=driver.find_element_by_xpath(".//*[@id='mod-login-form']/div[4]/button")
        form.submit()
        cookies=driver.get_cookies();
        #print 'cookies',cookies

        driver.get("https://xueqiu.com/people")
        print '====Start Crawling====='
        allNames=driver.find_element_by_class_name('screen_name')
        print allNames.get_attribute('innerHTML')
        print driver.find_element_by_xpath(".//*[@id='center']/div/div[2]/div[1]/div/div[1]/ul/li[1]/div/div/a[2]/span").get_attribute("innerHTML")        
        for i in range(2,4):
           # print 'i=',i
            xpathStr = ".//*[@id='center']/div/div[2]/div[1]/div/div[1]/ul/li[%s]/div/div/a[2]/span" %(i)
           # print xpathStr
          #  x=         './/*[@id='center']/div/div[2]/div[1]/div/div[1]/ul/li[2]/div/div/a[2]/span'
                       #'.//*[@id='center']/div/div[2]/div[1]/div/div[1]/ul/li[6]/div/div/a/span'
           # xpathSTR = ".//*[@id='center']/div/div[2]/div[1]/div/div[1]/ul/li[1]/div/div/a[2]/span"
           # print xpathSTR
           # print driver.find_element_by_xpath(xpathSTR).get_attribute("innerHTML")
            print driver.find_element_by_xpath(xpathStr).get_attribute("innerHTML")
                  #for i in range(1,100):
        #    print driver.find_element_by_class_name("screen_name").innerHTML
        #.//*[@id='center']/div/div[2]/div[1]/div/div[1]/ul/li[1]/div/div/a[2]/span
        #.//*[@id='center']/div/div[2]/div[1]/div/div[1]/ul/li[2]/div/div/a[2]/span
        #.//*[@id='center']/div/div[2]/div[1]/div/div[2]/ul/li[4]/div/div/a/span