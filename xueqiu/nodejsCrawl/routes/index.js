var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'yutiansut' });
});

router.get('/login', function(req, res, next) {
  console.log(JSON.stringify(req.query.id));
  console.log(req.query);
  console.log(JSON.stringify(req.query))
  res.render('index', { title: 'yutiansut' });
});

module.exports = router;
