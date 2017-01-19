// test.js
var page = require('webpage').create(),
	system = require('system'),
	address;
if (system.args.length === 1) {
	phantom.exit(1);
} else {
	address = system.args[1];
	page.open(address, function (status) {
		console.log(page.content);
		phantom.exit();
	});
}