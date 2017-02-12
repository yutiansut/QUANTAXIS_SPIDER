var express = require('express');
var router = express.Router();
var stock = require('../methods/stock/index').stock;
/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get('/history/all', function(req, res, next) {
  console.log(req.query.code);
  console.log(req.query.feq);
  var code=req.query.code;
  var options={};
  if (req.query.feq){
    var ktype=req.query.ktype;
    options={
    code: code,
    ktype: ktype,
  }
  }
  else options={
    code: code
  };

  console.log(options)
  stock.getHistory(options).then(({ data }) => {
    res.send(data.record);
  });
});

router.get('/history/time', function(req, res, next) {
  console.log(req.query.code);
  console.log(req.query.start);
  console.log(req.query.end);
  var code=req.query.code;
  var options={
    code:code
  };
  var start=req.query.start;
  var end=req.query.end;
  console.log(options)
  stock.getHistory(options).then(({ data }) => {
    var datas=data.record;
    for(i=0;i<datas.length;i++){
      if (datas[i][0]==start){
        var sId=i;
      }
    }
    for(i=0;i<datas.length;i++){
      if (datas[i][0]==end){
        var eId=i;
      }
    }
    console.log(sId)

    var newarray=datas.slice(sId,eId)
    res.send(newarray)
  });
});

module.exports = router;
