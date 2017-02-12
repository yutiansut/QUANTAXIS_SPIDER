const stock = require('../lib').stock;

stock.getHS300().then(({ data }) => {
  console.log(data);
});

