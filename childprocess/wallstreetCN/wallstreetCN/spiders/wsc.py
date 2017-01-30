# -*- coding: utf-8 -*-

import scrapy
from wallstreetCN.items import WallstreetcnItem
from wallstreetCN.phantomjs import selenium_request
from lxml import etree
from bs4 import BeautifulSoup 
from scrapy.spiders import Spider  
from scrapy.selector import Selector  


class WscSpider(scrapy.Spider):
    name = "wsc"
    
    def start_requests(self):
        link = 'http://wallstreetcn.com/news'
        print(link)
        #yield scrapy.Request(link, cookies=self.cookies,headers=self.headers,callback=self.parse_url_list)
        yield scrapy.Request(link,self.parse_url_list)

    def parse_url_list(self, response):
        sel = scrapy.Selector(response)
        print(sel)
        # first_url_list = sel.xpath('//title[1]//text()').extract()
        # print(first_url_list)
        
        fligint_title = ".//*[@id='news']/ul/li[1]/div/a[1]" 
        print(fligint_title)
        first_url_list = sel.xpath(fligint_title).extract()
        content = selenium_request(first_url_list)
        print(content)
            
       # first_url = first_url_list[0]
       # list_content = selenium_request(first_url)
       # soup = BeautifulSoup(list_content,'lxml')
       # h4_list = soup.find_all('h4')
       # if h4_list:
       #     for href in h4_list:
       #         url = 'http://mp.weixin.qq.com%s' % href.get('hrefs')
       #         #print(url)
       #         yield self.parse_item(url)
       # else:
       #     print('yanzheng')
                            #yield scrapy.Request(first_url, callback=self.parse)


    def parse_item(self,url):
        result = XiciItem()
        body = selenium_request(url)
        soup = BeautifulSoup(body, "lxml")
        title = soup.find("h2", id="activity-name").get_text()
        #content = soup.find("div", id="js_content")
        #print(title)
        result['title'] = title.strip()
        result['url'] = url
        return result
        return XiciItem
