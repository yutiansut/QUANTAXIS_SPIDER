# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import pymongo
from wallstreetCN.items import WallstreetcnItem
from scrapy.conf import settings


class WallstreetcnPipeline(object):
    def __init__(self):
            # 链接数据库
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["wsc"]
        self.url = db["url"]
        self.title = db['title']
        self.content = db['content']
        self.poster = db['content']

    def process_item(self, item, spider):
        print 'get data'
        self.url.insert(dict(item))

        return item