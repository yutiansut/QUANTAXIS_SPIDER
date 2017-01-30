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
        
        article_xpath = ".//*[@id='news']/ul/li/div/a[1]/@href"
        article_url_list = sel.xpath(article_xpath).extract()

        for article_url in article_url_list:
            print(article_url)
            yield scrapy.Request(article_url,self.parse_article)
            

            #yield self.parse_article(url)

        #content = selenium_request(article_url_list)
        #print(content)
    def parse_article(self, response):
        storageItem=WallstreetcnItem()
        sel = scrapy.Selector(response)
        #title
        article_title_xpath=".//*[@id='main']/div[1]/div[1]/div[1]"
        article_title = sel.xpath(article_title_xpath).extract()
        print(article_title)
        #url
        article_url_xpath=".//*[@id='user-modal']/@data-currenturl"
        article_url = sel.xpath(article_url_xpath).extract()
        print(article_url)
        #content
        article_content_xpath=".//*[@id='main']/div[1]/div[2]/p"
        article_content = sel.xpath(article_content_xpath).extract()
        print(article_content)
        #tag
        article_tag_xpath = ".//*[@id='article-leftbar']/ul/li[1]/div[2]/div"
        article_tag = sel.xpath(article_tag_xpath).extract()
        print(article_tag)
        #poster
        article_poster_xpath = ".//*[@id='article-rightbar']/div[1]/div[1]/div[1]/a[2]"
        article_poster = sel.xpath(article_poster_xpath).extract()[0]
        print(article_poster)
        article_time_xpath = ".//*[@id='main']/div[1]/div[1]/div[2]/div[1]"[0]
        article_time = sel.xpath(article_time_xpath).extract()
        print(article_time)
        article_viewNum_xpath = ".//*[@id='js-article-viewCount']"
        article_viewNum = sel.xpath(article_viewNum_xpath).extract()[0] 
        print(article_viewNum)
        #comments
        article_comments_xpath = ".//*[@id='comments']/div/div/div/div/div[2]/p"
        article_comments = sel.xpath(article_comments_xpath).extract()
        print(article_comments)
        storageItem["title"]=article_title
        storageItem["url"]=article_url
        storageItem["content"]=article_content
        storageItem["tag"]=article_tag
        storageItem["poster"]=article_poster
        storageItem["time"]=article_time
        storageItem["viewNum"]=article_viewNum
        return storageItem
        return WallstreetcnItem
            
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
