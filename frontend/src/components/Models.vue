<template>
  <section class="container">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/dashboard">Dashboard</router-link></li>
      <li><router-link to="/results">Results</router-link></li>
      <li><router-link to="/models">Models</router-link></li>
    </ul>
    <h1>Results of Different Load Data Methods</h1>
    <br>
    <ul>
      <li>
        <b-button size="lg" variant="warning" class="lsb_button"><router-link to="/create">Create</router-link>
        </b-button>
      </li>
      <li>
        <b-button size="lg" variant="warning" class="lsb_button"><router-link to="/dashboard">View All</router-link>
        </b-button>
      </li>
    </ul>
    <div class="columns">
      <div class="column">
        <Card :accuarcy="props.accuracy"
              :trainTime="props.trainTime"></Card>
        <Card></Card>
        <Card></Card>
      </div>
    </div>
  </section>
</template>

<script>
import Card from './Card'
export default {
  components: {Card},
  data () {
    return {
      props: {
        name: 'model #1',
        accuracy: '99.78%',
        trainTime: '1.53h'
      }
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

  .lsb_button a{
    color: white;
  }
</style>
