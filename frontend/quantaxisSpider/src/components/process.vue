<template>

<div class="demo-step-container">
    <h1>Welcome to Quantaxis</h1>
    <h2>Only Three Steps</h2>
    <mu-stepper :activeStep="activeStep">
    <mu-step>
        <mu-step-label>
        下载QUANTAXIS.Spider
        </mu-step-label>
    </mu-step>
    <mu-step>
        <mu-step-label>
        一键安装
        </mu-step-label>
    </mu-step>
    <mu-step>
        <mu-step-label>
        部署
        </mu-step-label>
    </mu-step>
    </mu-stepper>
    <div class="demo-step-content">
    <p v-if="finished">
        都完成啦!<a href="javascript:;" @click="reset">点这里</a>可以重置
    </p>
    <template v-if="!finished">
        <p>
        {{content}}
        </p>
        <div>
        <mu-flat-button class="demo-step-button" label="BACK" :disabled="activeStep === 0" @click="handlePrev"/>
        <mu-raised-button class="demo-step-button" :label="activeStep === 2 ? 'FINISH' : 'NEXT'" primary @click="handleNext"/>
        </div>
    </template>
    </div>
</div>
</template>

<script>
export default {
  name:'process',
  data () {
    return {
      activeStep: 0
    }
  },
  computed: {
    content () {
      let message = ''
      switch (this.activeStep) {
        case 0:
          message = 'SETTING Environment git clone https://github.com/yutiansut/QUANTAXIS_SPIDER'
          break
        case 1:
          message = 'powershell>install.ps1'
          break
        case 2:
          message = 'powershell>start'
          break
        default:
          message = 'fuck! 又 TM 出错了！！！'
          break
      }
      return message
    },
    finished () {
      return this.activeStep > 2
    }
  },
  methods: {
    handleNext () {
      this.activeStep++
    },
    handlePrev () {
      this.activeStep--
    },
    reset () {
      this.activeStep = 0
    }
  }
}
</script>

<style>
h1{
    color: darkgrey;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.demo-step-container {
  width: 100%;
  max-width: 700px;
  margin: auto;
}

.demo-step-content {
  margin: 0  16px;
}

.demo-step-button {
  margin-top: 12px;
  margin-right: 12px;
}
</style>