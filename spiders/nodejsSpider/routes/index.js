var express = require('express');
var router = express.Router();
var spider = require('../methods/spider.js')

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/tasks/1',function(req,res,next){
  spider;
})
module.exports = router;
