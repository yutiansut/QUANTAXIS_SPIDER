var stock = require('./lib/index').stock;

stock.getTodayAll().then(({ data }) => {
  console.log(data);
});



