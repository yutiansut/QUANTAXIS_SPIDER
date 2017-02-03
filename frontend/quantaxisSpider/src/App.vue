<template>
  <div id="app">
  <mu-appbar title="Title">
    <mu-text-field icon="search" class="appbar-search-field"  slot="right" hintText="请输入搜索内容"/>
    <mu-flat-button color="white" label="flat Button" slot="right"/>  
    <mu-icon-button icon="close" slot="left"/>
    <mu-icon-menu icon="more_vert" slot="right">
      <router-link to='/slides'><mu-menu-item title="菜单 1" ></mu-menu-item></router-link>
      <router-link to='/bar'><mu-menu-item title="菜单 2"/></router-link>
      <mu-menu-item title="菜单 3"/>
      <mu-menu-item title="菜单 4"/>
      <mu-menu-item title="菜单 5"/>
    </mu-icon-menu>
  </mu-appbar>
    <div class="container">
      <router-view></router-view>
    </div>
            
  </div>
</template>

<script>
import mobileTearSheet from './components/mobile.vue'
export default {
  name: 'app',
  components: {
    'mobile-tear-sheet': mobileTearSheet
  }
  //vm
}
</script>

<style lang='less'>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}

h1, h2 {
  font-weight: normal;
}

.appbar-search-field{
  color: #FFF;
  margin-bottom: 0;
  &.focus-state {
    color: #FFF;
  }
  .mu-text-field-hint {
    color: fade(#FFF, 54%);
  }
  .mu-text-field-input {
    color: #FFF;
  }
  .mu-text-field-focus-line {
    background-color: #FFF;
  }
}
</style>
