var fs = require('fs');
var request = require('superagent');
var cheerio = require('cheerio');
var axios = require('axios');
var http = require('http'); 
request
    .get('https://api.wallstreetcn.com/v2/pcarticles?page=3&limit=20') 
    .set({
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
    })
    .set({
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    })
    .set({
        'accept-encoding' : 'gzip, deflate, sdch, br'
    })
    .set({
        'Accept-Language':'zh-CN,zh;q=0.8,Cache-Control:max-age=0',
        'connection' : 'keep-alive'
    })
    .end(function(err,res){
        if(err)throw err;
        console.log(res.body.posts[1].resource.summary)
        console.log(res.body.posts[1].resource.tags[1])
    })



