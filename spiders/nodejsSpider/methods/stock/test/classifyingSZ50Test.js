const stock = require('../lib').stock;

stock.getSZ50().then(({ data }) => {
  console.log(data);
});

