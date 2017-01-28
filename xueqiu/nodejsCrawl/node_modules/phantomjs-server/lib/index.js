var when = require('when');
var fs = require('fs');
var spawn = require('child_process').spawn;

exports.version = '1.9.10';
exports.commandOptions = ['--webdriver=4444', '--ignore-ssl-errors=true'];

exports.logFilePath = './phantomjs.log';
exports.errorLogFilePath = './phantomjs.log';

var out = fs.openSync(exports.logFilePath, 'w+');
var err = fs.openSync(exports.errorLogFilePath, 'w+');

exports.path = require.resolve('phantomjs/bin/phantomjs');
if(process.platform === 'win32') {
  exports.path = require.resolve('phantomjs/lib/phantom/phantomjs.exe');
}

var deferredAddress = when.defer();

exports.address = function() {
  return deferredAddress.promise;
};


exports.start = function() {
  var deferred = when.defer();

  exports.child = spawn(exports.path,
                  exports.commandOptions,
                  { detached: true, stdio: [ 'ignore', out, err ] });
  exports.child.unref();

  // This should be replaced by a test, that waits til the server is up...
  setTimeout(function() {
    deferredAddress.resolve('http://127.0.0.1:4444/wd/hub');
    deferred.resolve();
  }, 2000);

  return deferred.promise;
};

exports.stop = function() {
  if(exports.child != null) {
    exports.child.kill();
  }
};
