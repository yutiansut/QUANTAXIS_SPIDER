// test.js
var page = require('webpage').create();
page.open('https://www.27sihu.com/', function () {
    page.render('baidu.png');
	//console.log(page.content);
	var a=document.getElementsByTagName('a');
	console.log(a[6].href);
    phantom.exit();
	
});