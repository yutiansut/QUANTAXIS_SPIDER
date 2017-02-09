# -*- coding: utf-8 -*-
import scrapy


class QuantaxisSpider(scrapy.Spider):
    name = "quantaxis"
    allowed_domains = ["quantaxis.com"]
    start_urls = ['http://quantaxis.com/']

    def parse(self, response):
        pass
