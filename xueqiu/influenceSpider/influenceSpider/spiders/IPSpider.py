# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider  
from scrapy.http import Request  
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
    headers={
        'Host': "xueqiu.com",
        'Connection': "keep-alive",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'cookies': cookies
    }
    def start_requests(self):
        urls = [
            'https://xueqiu.com',
            "https://xueqiu.com/people",
        ]
        for url in urls:
            yield scrapy.Request(url=url,encoding='utf-8', callback=self.parse,method='GET',headers=self.headers)
    
    
    print '===start requests==='
    print start_urls
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
