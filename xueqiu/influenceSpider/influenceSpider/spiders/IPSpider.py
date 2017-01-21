# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector  
from influenceSpider.items import InfluencespiderItem
import json
import base64
import requests
import cookies

with open('influenceSpider/spiders/setting.json', 'r') as f:
    user = json.load(f)
    user.mail = user['mail']
    user.telephone=user['phone']
    user.psw = user['psw']
    #

class IpspiderSpider(scrapy.Spider):
    name = "IPSpider"
    allowed_domains = ["xueqiu.com"]
    start_urls = ['https://xueqiu.com/user/login']
    item = [ ]
    cookies = []
    def login(self,response):
        loginurls="https://xueqiu.com/user/login"
        formdata= {
            "areacode":"86",
            "password":base64.b64encode(user.psw.encode('utf-8')).decode('utf-8'),
            "remember_me":"on",
            "telephone":user.telephone
        }
        session = requests.Session()
        r = session.post(loginurls, data=formdata)
        jsonStr = r.content.decode('gbk')
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            print "Get Cookie Success!( Account:%s )" % user.telephone
            cookie = session.cookies.get_dict()
            cookies.append(cookie)
        else:
            print "Failed!( Reason:%s )" % info['reason']

    print cookies
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

