# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector  
from influenceSpider.items import InfluencespiderItem
import json
import base64
import requests



class IpspiderSpider(Spider):
    with open('influenceSpider/spiders/setting.json', 'r') as f:
        user = json.load(f)
        print user
        #user.mail = user['mail']
        phone=user['phone']
        psw = user['psw']
    #
    name = "IPSpider"
    allowed_domains = ["xueqiu.com"]
    
    item = [ ]
    
    
    start_urls = ['https://xueqiu.com/people']

    
    cookies = [ ]
    loginurls="https://xueqiu.com/user/login"
    formdata= {
        "areacode":"86",
        "password":psw,
        "remember_me":"on",
        "telephone":phone
    }
    r = Request(loginurls)
    print r

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

