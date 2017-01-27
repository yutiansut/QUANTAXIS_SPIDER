var webdriver = require('selenium-webdriver'),
    chrome = require('selenium-webdriver/chrome'),
    firefox = require('selenium-webdriver/firefox'),
    phantom = require('phantom'),
    By = webdriver.By,
    until = webdriver.until;


var driver = new webdriver.Builder()
    .forBrowser('phantom')
    .setChromeOptions(/* ... */)
    .setFirefoxOptions(/* ... */)
    .setPhantomOptions()
    .build();

driver.get('https://xueqiu.com/user/login')
    .then(_ => driver.wait(until.titleIs("登录 - 雪球"), 1000))
    .then(_ => driver.findElement(By.name('username')).sendKeys('13382753152'))
    .then(_ => driver.findElement(By.name('password')).sendKeys('Yutiansut940809'))
    .then(_ => driver.findElement(By.name('remember_me')).click())
    .then(_ => driver.findElement({"class":'button.button'}).click())
    .then(_ => driver.wait(until.titleIs("我的首页 - 雪球"), 1000))
console.log(driver.getCookie())


driver.quit();