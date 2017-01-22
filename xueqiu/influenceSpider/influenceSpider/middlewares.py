# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
import time  
import random
import base64
#雪球的防封机制 bt




class InfluencespiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

  
    def process_request(self, request, spider):
        if spider.name =="IPSpider":
            print "PhantomJS is starting..."
            
           
            headers = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                "Host": "xueqiu.com",
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                'Connection': 'keep-alive',
                "Accept-Encoding": "gzip, deflate, sdch, br",
                "Referer": "https://xueqiu.com/people",
                'X-Requested-With': 'XMLHttpRequest'
            }

            for key in headers:
                webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]
           # dcap = dict(DesiredCapabilities.PHANTOMJS)
        #    dcap["phantomjs.page.settings.userAgent"] = (
          #  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
        #    )
            service_args = [
            '--proxy-type=https',
            '--ignore-ssl-errors=true'
            ]
            driver = webdriver.PhantomJS(service_args=service_args)
#
        # driver = webdriver.Firefox()
           # driver.settings.userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER 1.1"  
            driver.get(request.url)
            time.sleep(1)
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。
            time.sleep(3)
            body = driver.page_source
            print("访问"+request.url)
            driver.get_cookies();
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return
