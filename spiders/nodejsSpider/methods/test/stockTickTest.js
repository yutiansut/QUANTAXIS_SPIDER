const stock = require('../lib').stock;

const query = {
  code: '600848',
  date: '2015-12-31',
};
stock.getTick(query).then(({ data }) => {
  console.log(data);
});

