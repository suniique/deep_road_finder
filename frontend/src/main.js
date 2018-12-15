// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Chartkick from 'chartkick'
import VueChartkick from 'vue-chartkick'
import ElementUI from 'element-ui'
import BootstrapVue from 'bootstrap-vue'

import 'chart.js'
import 'hchs-vue-charts'
import 'element-ui/lib/theme-chalk/index.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(ElementUI)
Vue.use(window.VueCharts)
Vue.use(VueChartkick, { Chartkick })
Vue.use(BootstrapVue)

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
