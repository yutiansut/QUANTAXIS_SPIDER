<template>  
    <button>getajax</button>
</template>
<script>

  axios.get('http://localhost:3000/apis/querytitlebyname?name=%E7%89%B9%E6%9C%97%E6%99%AE')
  .then(function (response) {
    console.log(response);
  })
  .catch(function (response) {
    console.log(response);
  });
</script>