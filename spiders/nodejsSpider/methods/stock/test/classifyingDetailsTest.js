const stock = require('../lib').stock;

stock.getSinaClassifyDetails().then(({ data }) => {
  console.log(data);
});

const options = {
  tag: 'gn_zndw',
};
stock.getSinaClassifyDetails(options).then(({ data }) => {
  console.log(data);
});

