const stock = require('../lib').stock;


const query = { code: '600848' };
stock.getHistory(query).then(({ data }) => {
  console.log(data);
});



const query2 = {
  code: '600848',
  ktype: 'week',
};
stock.getHistory(query2).then(({ data }) => {
  console.log(data);
});

const query3 = {
  code: '600848',
  ktype: '15',
};
stock.getHistory(query3).then(({ data }) => {
  console.log(data);
});
