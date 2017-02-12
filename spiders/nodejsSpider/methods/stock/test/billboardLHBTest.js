const stock = require('../lib').stock;


const options = {
  start: '2016-01-15',
  end: '2016-01-15',
};
stock.lhb(options).then(({ data }) => {
  console.log(data);
});

