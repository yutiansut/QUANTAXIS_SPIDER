var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    until = webdriver.until;
    phantom = require('phantom');
phantom.create([], {
    phantomPath: '../../phantomjs.exe',
    logLevel: 'debug',
}) 

var driver = new webdriver.Builder()
    .forBrowser('phantom')
    .build();


driver.get('https://www.baidu.com');
driver.findElement(By.id('kw')).sendKeys('webdriver');
driver.findElement(By.id('su')).click();
driver.wait(until.titleIs('webdriver_百度搜索'), 1000);
driver.quit();