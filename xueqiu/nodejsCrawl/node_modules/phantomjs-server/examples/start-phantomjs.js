var phantomjs = require('phantomjs-server');
phantomjs.start().then(function() {
  process.exit(0);
});