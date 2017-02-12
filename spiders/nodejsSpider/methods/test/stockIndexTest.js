const stock = require('../lib').stock;

stock.getIndex().then(({ data }) => {
  console.log(data);
});
