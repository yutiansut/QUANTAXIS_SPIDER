# -*- coding: utf-8 -*-
import scrapy


class QuantaxisspiderSpider(scrapy.Spider):
    name = "quantaxisSpider"
    allowed_domains = ["quantaxis.com"]
    start_urls = ['http://quantaxis.com/']

    def parse(self, response):
        pass
