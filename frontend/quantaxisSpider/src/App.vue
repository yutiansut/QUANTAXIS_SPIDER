<template>
  <div id="app">

  </div>
</template>

<script>
import Slides from './components/Slides.vue';
import Bar from './components/Bar.vue';

export default {
  name: 'app',
  components : {Slides,Bar},
  data () {
    //Vue 实例的数据对象。
    //Vue 将会递归将 data 的属性转换为 getter/setter，从而让 data 的属性能够响应数据变化。
    //对象必须是纯粹的对象(含有零个或多个的key/value对)
  }
  //vm
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}


</style>
