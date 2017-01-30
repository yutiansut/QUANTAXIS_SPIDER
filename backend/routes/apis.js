var express = require('express');
var router = express.Router();
var wscQuery =require('../database/config')
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
}); 

router.get('/json', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.get('/querybyname', function(req, res, next) {
    console.log('get data')
    console.log(req.query.name)
    wscQuery.find({content:req.query.name},function(err,docs){
        if(!err){
            console.log(docs);
        	res.json(docs);
        }else{
            console.log(err);
        }
    });
});


module.exports = router;
