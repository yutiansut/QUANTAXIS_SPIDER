#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import choice
import time
def selenium_request(url):
    print("using selenium_request")
    ua_list = [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36"
    ]

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.resourceTimeout"] = 15
    dcap["phantomjs.page.settings.loadImages"] = False
    dcap["phantomjs.page.settings.userAgent"] = choice(ua_list)
    # driver = webdriver.PhantomJS(executable_path='/home/icgoo/pywork/spider/phantomjs',desired_capabilities=dcap)
    # driver = webdriver.PhantomJS(executable_path=u'/home/fank/pywork/spider/phantomjs',desired_capabilities=dcap)
    driver = webdriver.PhantomJS(executable_path='D:/Projects/Projects/craw/childprocess/phantomjs.exe',desired_capabilities=dcap)
    # driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(3)
    time.sleep(5)
    true_page = driver.page_source  # .decode('utf-8','ignore')
    driver.close()
    return true_page
