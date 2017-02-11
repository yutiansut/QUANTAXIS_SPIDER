var spider = require('./methods/spider')

var s=new spider({
    callback : function (error, res, done){
        console.log(res)

    }
});
s.request('https://www.baidu.com/s?wd=quantaxis')


console.log('test'+s.response)