# -*- coding: utf-8 -*-
import scrapy


class IPSpider(scrapy.Spider):
    name = "influencePeople"
    allowed_domains = ["xueqiu.com"]
    start_urls = ['http://xueqiu..com/people']

    def parse(self, response):
        pass
