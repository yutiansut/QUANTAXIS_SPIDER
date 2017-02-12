const stock = require('../index').stock;

const query = {
  codes: [
    '600848',
    '600000',
  ],
};
stock.getLiveData(query).then(({ data }) => {
  console.log(data);
});

