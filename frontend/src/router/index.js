import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import VueChartJS from '@/components/VueChartJS'
import VueCharts from '@/components/VueCharts'
import Models from '@/components/Models'
import Create from '@/components/Create'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/dashboard',
      name: 'VueChartJS',
      component: VueChartJS
    },
    {
      path: '/models',
      name: 'Models',
      component: Models
    },
    {
      path: '/results',
      name: 'VueCharts',
      component: VueCharts
    },
    {
      path: '/create',
      name: 'Create',
      component: Create
    }
  ]
})
