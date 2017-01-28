[![NPM version](https://badge.fury.io/js/phantomjs-server.png)](http://badge.fury.io/js/phantomjs-server)

PhantomJS Server
=======

Use PhantomJS as a drop-in replacement for your Selenium Standalone server.

-

This is just a simple script to start a PhantomJS webdriver instead of the Selenium standalone server.

The server.address() works the same way as the selenium-webdriver's version, by responding with a promise that will eventually resolve to the localhost address of PhantomJS.

PhantomJS is 1.9.2-6 as this is, at the time of writing, the last working version on Mac OS X.

### Start a PhantomJS server with package.json pretest
To start a PhantomJS server before running your test scripts, you can create a file that is called pretest like this:

package.json
```
{
  ...
  "devDependencies": {
	...
    "selenium-webdriver": "~2.39.0",
    "phantomjs-server": "1.9.2"
  },
  "scripts": {
	...
    "pretest": "node start-phantomjs.js",
    "posttest": "node stop-phantomjs.js",
  }
}
```

start-phantomjs.js
```
var phantomjs = require('phantomjs-server');
phantomjs.start().then(function() {
  process.exit(0);
});
```

stop-phantomjs.js
```
require('child_process').exec(process.platform === 'win32' ? 'taskkill /F /IM phantomjs.exe /T' : 'killall phantomjs',
    function (error, stdout, stderr) {
        console.log(stdout);
    });
```


### Using phantomjs-server inline instead of selenium-server-standalone

Assuming a Selenium testing script looking something like this:
```
var webdriver = require('selenium-webdriver');

var SeleniumServer = require('selenium-webdriver/remote').SeleniumServer;
var server = new SeleniumServer('bin/selenium-server-standalone.jar', { port: 4444 });
server.start();

var driver = new webdriver.Builder().
  usingServer(server.address()).
  withCapabilities({ "browserName": "firefox" }).
  build();
```

You only need to replace this:
```
var SeleniumServer = require('selenium-webdriver/remote').SeleniumServer;
var server = new SeleniumServer('bin/selenium-server-standalone.jar', { port: 4444 });
server.start();
```

With this:
```
var phantom = require('phantomjs-server');
phantom.start();
```



So the final script looks like:

```
var webdriver = require('selenium-webdriver');

var phantom = require('phantomjs-server');
phantom.start();

var driver = new webdriver.Builder().
  usingServer(phantom.address()). // This part is important!
  withCapabilities({ "browserName": "phantomjs" }).
  build();
```

### Troubleshooting
If the PhantomJS server won't start, it is probably because you have these 2 files:

* /usr/local/lib/libssl.0.9.8.dylib
* /usr/local/lib/libssl.dylib

Move them to something like:

* /usr/local/lib/_libssl.0.9.8.dylib
* /usr/local/lib/_libssl.dylib

And you should be good to go!
