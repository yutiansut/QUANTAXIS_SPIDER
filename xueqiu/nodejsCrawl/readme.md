# 使用selenium-Mongodb搭建后台

爬虫思路:
> 首先进入登录页面,https://xueqiu.com/user/login,select 用户名框和密码框,勾选一直登录


突然改主意了....准备做成一个前后端分离的,可以热更新的,分布式爬虫

前端UI 用vue-blu,前端vue.js, axios/vue-resource 做ajax,前端路由 vue-router, webpack 做中间件,express做后端api.
child-process控制子进程,子进程用python-selenium-scrapy爬虫和部分nodejs DHT,分布式用redis控制进度,数据流走mongodb

QUANTAXIS_SPIDER STACK 
