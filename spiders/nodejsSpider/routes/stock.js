var express = require('express');
var router = express.Router();
var stock = require('./methods/stock').stock;
/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get('/getHistory', function(req, res, next) {
  console.log(req.query.code);
  console.log(req.query.ktype);
  stock.getHistory()
});

module.exports = router;
