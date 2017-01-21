# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector  
from influenceSpider.items import InfluencespiderItem
import json

with open('setting.json', 'r') as f:
 user = json.load(f)
 
class IpspiderSpider(scrapy.Spider):
    name = "IPSpider"
    allowed_domains = ["xueqiu.com"]
    start_urls = ['https://xueqiu.com/user/login']
    item = [ ]

    def login(self,response):
        cookies = 1;
        user=[];





        return cookies
    def parse(self, response):
        sel = Selector(response)  
        item=InfluencespiderItem();
        id=response.xpath('//a/@href').extract()
        for i in id:
            url='https://www.xueqiu.com'+i
            print i
            print url
               # item['html']=url;
            yield Request(url, callback=self.parse)

