# -*- coding:utf-8 -*-
from WindPy import *
w.start()   
from datetime import datetime
from pymongo import MongoClient  
import talib
#先搞上期
#数据库
client = MongoClient('localhost', 27017)  
db = client.wind
coll = db.future


