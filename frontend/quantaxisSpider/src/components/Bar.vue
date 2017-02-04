<template>
<swiper :options="swiperOption" ref="mySwiperA">
  <!-- 幻灯内容 -->
  <swiper-slide>I'm Slide 1</swiper-slide>
  <swiper-slide>I'm Slide 2</swiper-slide>
  <swiper-slide>I'm Slide 3</swiper-slide>
  <swiper-slide>I'm Slide 4</swiper-slide>
  <swiper-slide>I'm Slide 5</swiper-slide>
  <swiper-slide>I'm Slide 6</swiper-slide>
  <swiper-slide>I'm Slide 7</swiper-slide>
  <!-- ... -->
  <!-- 以下控件元素均为可选（使用具名slot来确定并应用一些操作控件元素） -->
  <div class="swiper-pagination"  slot="pagination"></div>
  <div class="swiper-button-prev" slot="button-prev"></div>
  <div class="swiper-button-next" slot="button-next"></div>
  <div class="swiper-scrollbar"   slot="scrollbar"></div>
</swiper>
</template>

<script>
export default {
  name: 'carrousel',
  data() {
    return {
      swiperOption: {
        // 所有配置均为可选（同Swiper配置）
        // NotNextTick is a component's own property, and if notNextTick is set to true, the component will not instantiate the swiper through NextTick, which means you can get the swiper object the first time (if you need to use the get swiper object to do what Things, then this property must be true)
        // notNextTick是一个组件自有属性，如果notNextTick设置为true，组件则不会通过NextTick来实例化swiper，也就意味着你可以在第一时间获取到swiper对象（假如你需要使用获取swiper对象来做什么事，那么这个属性一定要是true）
        notNextTick: true,
        autoplay: 3000,
        direction : 'vertical',
        grabCursor : true,
        setWrapperSize :true,
        autoHeight: true,
        pagination : '.swiper-pagination',
        paginationClickable :true,
        prevButton:'.swiper-button-prev',
        nextButton:'.swiper-button-next',
        scrollbar:'.swiper-scrollbar',
        mousewheelControl : true,
        observeParents:true,
        // if you need use plugins in the swiper, you can config in here like this
        // 如果自行设计了插件，那么插件的一些配置相关参数，也应该出现在这个对象中，如下debugger
        //ebugger: true,
        // swiper callbacks
        // swiper的各种回调函数也可以出现在这个对象中，和swiper官方一样
        onTransitionStart(swiper){
          console.log(swiper)
        },
        // more Swiper config ...
        // ...
      }
    }
  },
  // example code (if you need to get the current swiper object, you can find the swiper object like this, the $ref object is a ref attribute corresponding to the dom redefined)
  // 如果你需要得到当前的swiper对象来做一些事情，你可以像下面这样定义一个方法属性来获取当前的swiper对象，实际上这里的$refs对应的是当前组件内所有关联了ref属性的组件元素对象，同时配置中的notNextTick属性一定要设置为true
  computed: {
    swiper() {
      return this.$refs.mySwiperA.swiper
    }
  },
  mounted() {
    // you can use current swiper object to do something(swiper methods)
    // 然后你就可以使用当前上下文内的swiper对象去做你想做的事了
    console.log('this is current swiper object', this.swiper)
    this.swiper.slideTo(3, 1000, false)
  }
}
</script>

<style scoped>
  .swiper-inner {
    width: 100%;
    height: 400px;
    padding-top: 50px;
    padding-bottom: 50px;
  }
  .swiper-slide {
    background-position: center;
    background-size: cover;
    width: 300px;
    height: 300px;
  }
</style>