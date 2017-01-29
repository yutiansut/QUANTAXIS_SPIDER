# -*- coding: utf-8 -*-

import scrapy
from wallstreetcn.items import WallstreetcnItem
from wallstreetcn.phantomjs import selenium_request
from lxml import etree
from bs4 import BeautifulSoup 
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector  


class WscSpider(scrapy.Spider):
    name = "wsc"
    allowed_domains = ["http://wallstreetcn.com/"]
    start_urls = ['http://http://wallstreetcn.com//']

    def parse(self, response):
        pass
