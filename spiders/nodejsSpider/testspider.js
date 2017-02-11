var spider = require('./methods/spider')

var s=new spider({
    callback : function (error, res, done){
        console.log(res)

    }
});
s.request('http://www.baidu.com')