# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider  
# from scrapy.http import Request  
from scrapy.selector import Selector  
from influenceSpider.items import InfluencespiderItem
from influenceSpider.middlewares import InfluencespiderSpiderMiddleware
import json
import base64
import requests
from selenium import webdriver  
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import getCookies as cok

class IpspiderSpider(Spider):
    #
    name = "IPSpider"
    allowed_domains = ["xueqiu.com"] 
    item = [ ]
    start_urls = "https://xueqiu.com/people"
    t = cok.getCookies()
    cookies = t.getCookiesFromXueqiu('xueqiu');
    print cookies
    print '===start requests==='
    print start_urls
    def parse(self, response):
        print self.start_urls
        print self.cookies
        spider = Spider(self,name="IPSpider")
        InfluencespiderSpiderMiddleware.process_request(self,self.start_urls,spider,self.cookies)