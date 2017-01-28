var webdriver = require('selenium-webdriver'),
    chrome = require('selenium-webdriver/chrome'),
    firefox = require('selenium-webdriver/firefox'),
    phantomjs = require('phantomjs-server');
    By = webdriver.By,
    until = webdriver.until;

var SeleniumServer = require('selenium-webdriver/remote').SeleniumServer;
var server = new SeleniumServer('bin/selenium-server-standalone.jar', { port: 4444 });
server.start();


var driver = new webdriver.Builder().
  usingServer(phantom.address()). // This part is important!
  withCapabilities({ "browserName": "phantomjs" }).
  build();

driver.get('https://xueqiu.com/user/login')
    .then(_ => driver.wait(until.titleIs("登录 - 雪球"), 1000))
    .then(_ => driver.findElement(By.name('username')).sendKeys('13382753152'))
    .then(_ => driver.findElement(By.name('password')).sendKeys('Yutiansut940809'))
    .then(_ => driver.findElement(By.name('remember_me')).click())
    .then(_ => driver.findElement({"class":'button.button'}).click())
    .then(_ => driver.wait(until.titleIs("我的首页 - 雪球"), 1000))
console.log(driver.getCookie())


driver.quit();