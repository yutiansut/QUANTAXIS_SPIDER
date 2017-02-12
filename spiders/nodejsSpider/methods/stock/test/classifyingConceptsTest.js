const stock = require('../lib').stock;

stock.getSinaConceptsClassified().then(({ data }) => {
  console.log(JSON.stringify(data));
});
