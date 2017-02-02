<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <h2>QUANTAXIS量化工具箱爬虫部分</h2>
    <logo></logo>
  </div>
</template>

<script>
import logo from './components/logo.vue';
export default {
  name: 'app',
  components : {logo},
  data () {
    //Vue 实例的数据对象。
    //Vue 将会递归将 data 的属性转换为 getter/setter，从而让 data 的属性能够响应数据变化。
    //对象必须是纯粹的对象(含有零个或多个的key/value对)
    return {
      msg: 'QUANTAXIS_Spider 可视化爬虫' //键值对
    }
  }
  //vm
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
