# QUANTAXIS_SPIDER 爬虫
### QUANTAXIS 3.5 重构版本的爬虫部分
![build](https://img.shields.io/badge/Build-passing-green.svg)
![author](https://img.shields.io/badge/Powered%20by-%20%20yutiansut-red.svg)
![license](https://img.shields.io/badge/License-%20MIT-brightgreen.svg)


## 功能剥离与逻辑优化

### 功能剥离(我们为什么要把可视化部分剥离)
从dev-pure版本,我们即将剥离原有的架构模式
```
backend
frontend
childprocess
```
改为纯粹的爬虫模式,我们将开发并维护两个版本的爬虫python/scrapy,以及nodejs爬虫
之所以去剥离可视化部分,我们主要认为可视化和我们的主要功能有了冲突,把他继续放在爬虫底下影响了开发效率.
剥离后的可视化部分(包括网页,后台以及exe),我们将移入quantaxis_DATACENTER部分进行进一步的开发

### 开发逻辑
python的爬虫部分已经完善,而问题在于我们之前所构想的逻辑框架并不成立.及
*python爬虫负责后端,nodejs负责前端
*使用express框架打包REST API,vue框架负责前端页面逻辑,使用axios进行ajax请求部分刷新可视化模块.
*不同用户可以通过可视化页面去读取爬虫的结果并且控制爬虫的行为

前两个已经实现,而问题出现在nodejs和python的热刷新问题上,并未找到较好的解决方案去处理热更新爬虫的问题
我们现在更加倾向于纯JavaScript进行爬取,后台,以及前端网站框架




-------------
## Stack
```
nodejs
express
webpack
vue.js
vue-blu
python-scrapy-selenium-webdriver
mongodb

```
## Usage
* 安装python,nodejs,python-pip
* 安装Quantaxis_Spider
```
git clone https://github.com/yutiansut/QUANTAXIS_SPIDER.git
cd QUANTAXIS_SPIDER
cd backend
npm install
cd ../frontend/quantaxisSpider
npm install
cd ../../childprocess
python -m pip install -r requirements.txt
```
* 安装mongodb-启动Mongo服务
```
windows
linux
```

## Features

## Todolists
### 热刷新问题
ajax去请求数据异步刷新模块这些没问题,下一步是反向注入json任务给运行中的python和matlab核心去做热刷新
在前端和爬虫和分析核中间也构建一个MVVM

### 一键部署/安装  使用powershell

### 技术栈
![技术栈](https://github.com/yutiansut/QUANTAXIS_SPIDER/blob/dev-visualCraw/todo.png)
### Start页面
![Start页面](https://github.com/yutiansut/QUANTAXIS_SPIDER/blob/dev-front/pic/start.gif)
### 前端设计
![前端设计](https://github.com/yutiansut/QUANTAXIS_SPIDER/blob/dev-front/pic/HomePage-design.png)
### 爬取到的数据
![爬到的数据](https://github.com/yutiansut/QUANTAXIS_SPIDER/blob/dev-front-back-Craw/pic/craw.png)
## 数据库查重
![数据库查重](https://github.com/yutiansut/QUANTAXIS_SPIDER/blob/dev-front-back-Craw/pic/findsame.png)
### 从数据库索引中爬取
![从数据库文章索引爬取](https://github.com/yutiansut/QUANTAXIS_SPIDER/blob/dev-front-back-Craw/pic/getfromdatabase.png)
## 后端api做restful
![后端api做restful](https://github.com/yutiansut/QUANTAXIS_SPIDER/blob/dev-front-back-Craw/pic/backend-restful.png)
### 前端拿到api
![前端拿到api](https://github.com/yutiansut/QUANTAXIS_SPIDER/blob/dev-front-back-Craw/pic/front-getapi.png)