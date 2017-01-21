# -*- coding: utf-8 -*-
import scrapy
from influenceSpider.items import InfluencespiderItem

class IpspiderSpider(scrapy.Spider):
    name = "IPSpider"
    allowed_domains = ["xueqiu.com"]
    start_urls = ['http://xueqiu.com/people/']
    item = [ ]
    def parse(self, response):
        
        pass
