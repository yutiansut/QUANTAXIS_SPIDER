var _tushare = require('tushare');
var stock = _tushare.stock;

stock.getTodayAll().then(({ data }) => {
  console.log(data);
});