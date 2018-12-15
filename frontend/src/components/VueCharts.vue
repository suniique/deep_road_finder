<template>
  <section class="container">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/dashboard">Dashboard</router-link></li>
      <li><router-link to="/results">Results</router-link></li>
      <li><router-link to="/models">Models</router-link></li>
    </ul>
    <h1>Results of Different Load Data Methods</h1>
    <div class="columns">
      <div class="column">
        <h3>Loss</h3>
        <chartjs-horizontal-bar 
        :labels="mylabels"
        :datasets="mydatasets"
        :height="height_size"></chartjs-horizontal-bar>
      </div>
      <div class="column">
        <h3>IOU</h3>
        <chartjs-horizontal-bar 
        :labels="mylabels"
        :datasets="mydatasets"
        :height="height_size"></chartjs-horizontal-bar>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <h3>Time Cost</h3>
        <chartjs-horizontal-bar 
        :labels="mylabels"
        :datasets="mydatasets"
        :height="height_size"></chartjs-horizontal-bar>
      </div>
      <div class="column">
        <h3>Bar Chart</h3>
        <chartjs-horizontal-bar 
        :labels="mylabels"
        :datasets="mydatasets"
        :height="height_size"></chartjs-horizontal-bar>
      </div>
    </div>
  </section>
</template>

<script>
  export default {
    name: 'VueCharts',
    data () {
      return {
        mylabels: ['#1', '#2', '#3', '#4', '#5'],
        mydatasets: [{
          label: 'My First dataset',
          backgroundColor: ['rgba(255,175,25,0.8)', 'rgba(255,175,25,0.8)', 'rgba(255,175,25,0.8)', 'rgba(255,175,25,0.8)', 'rgba(255,175,25,0.8)'],
          borderWidth: 1,
          data: [65, 59, 80, 81, 56, 55]
        }],
        height_size: 100
      }
    },
    methods: {
      addData () {
        this.dataset.push(this.dataentry)
        this.labels.push(this.datalabel)
        this.datalabel = ''
        this.dataentry = ''
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
</style>
