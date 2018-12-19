<template>
<section class="container">
  <div class="main page">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/dashboard">Dashboard</router-link></li>
      <li><router-link to="/results">Results</router-link></li>
      <li><router-link to="/models">Models</router-link></li>
    </ul>
    <h1>Dashboard: Monitor Training Process</h1>
    <div class="columns">
      <div class="column">
        <h3>Monitor of Model Name</h3>
        <ul>
          <li>
            <b-button class='mybutton' size='sm' variant='warning' v-on:click='start_training'>
              Start
            </b-button>
          </li>
          <li>
            <b-button class='mybutton' size='sm' variant='warning' v-on:click='end_training'>
              Stop
            </b-button>
          </li>
        </ul>
        <line-chart></line-chart>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <h3>Output of Network</h3>
        <img src="../assets/mask.png">
      </div>
  </div>
  </div>
</section>
</template>

<script>
  import LineChart from '@/components/LineChart'
  import BarChart from '@/components/BarChart'
  import BubbleChart from '@/components/BubbleChart'
  import Reactive from '@/components/Reactive'
  import NewButton from './NewButton'

  export default {
    name: 'VueChartJS',
    components: {
      LineChart,
      BarChart,
      BubbleChart,
      Reactive,
      NewButton
    },
    data () {
      return {
        buttons: {
          size: 'sm',
          variant: 'warning'
        }
      }
    },
    created () {
      this.fillData()
    },
    methods: {
      handleOpen (key, keyPath) {
        console.log(key, keyPath)
      },
      handleClose (key, keyPath) {
        console.log(key, keyPath)
      },
      fillData () {
        this.datacollection = {
          labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
          datasets: [
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
            }
          ]
        }
      },
      getRandomInt () {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5
      },
      start_training () {
        this.axios.patch('/api/trial/1/', {state: 1})
        .then(function (response) {
          console.log('success in starting')
        })
        .catch(function (error) {
          console.log('Error! Could not reach the API. ' + error)
        })
      },
      end_training () {
        this.axios.patch('/api/trial/1/', {state: 2})
        .then(function (response) {
          console.log('success in ending')
        })
        .catch(function (error) {
          console.log('Error! Could not reach the API. ' + error)
        })
      }
    }
  }
</script>

<style scoped>
  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #FFB119;
  }

  .mybutton {
    float: left;
    margin: 10px;
    color: white;
  }
</style>
