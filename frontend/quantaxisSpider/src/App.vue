<template>
  <div id="app">
    <div id='nav'>
      <ul>
        <li><router-link to='/slides'>home</router-link></li>
        <li><router-link to='/bar'>bar</router-link></li>
      </ul>
    </div>
    <h1>welcome to QUANTAXIS</h1>
    <div class="container">
      <router-view></router-view>
    </div>
            
  </div>
</template>

<script>
export default {
  name: 'app',
  //vm
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}

h1, h2 {
  font-weight: normal;
}

</style>
