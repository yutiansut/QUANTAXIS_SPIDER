const stock = require('../lib').stock;

stock.getSinaIndustryClassified().then(({ data }) => {
  console.log(data);
});

