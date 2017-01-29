var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});
router.get('/first', function(req, res, next) {
  res.send(json({name:'aaa',pwd:'123'}));
});

module.exports = router;
