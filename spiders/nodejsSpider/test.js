var Crawler = require("crawler");
var url = require('url');

var c = new Crawler({
    maxConnections : 10,
    // This will be called for each crawled page
    callback : function (error, res, done) {
        if(error){
            console.log(error);
        }else{
            var $ = res.$;
            // $ is Cheerio by default
            //a lean implementation of core jQuery designed specifically for the server
            console.log($("title").text());
        }
        done();
    }
});

// Queue just one URL, with default callback
c.queue('http://www.amazon.com');

// Queue a list of URLs
c.queue(['http://www.google.com/','http://www.yahoo.com']);

// Queue URLs with custom callbacks & parameters
c.queue([{
    uri: 'http://parishackers.org/',
    jQuery: false,

    // The global callback won't be called
    callback: function (error, res, done) {
        if(error){
            console.log(error);
        }else{
            console.log('Grabbed', res.body.length, 'bytes');
        }
        done();
    }
}]);

// Queue some HTML code directly without grabbing (mostly for tests)
c.queue([{
    html: '<p>This is a <strong>test</strong></p>'
}]);