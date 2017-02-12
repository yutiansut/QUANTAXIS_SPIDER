const stock = require('../lib').stock;


stock.getAllStocks().then(({ data }) => {
  console.log(JSON.stringify(data));
});

