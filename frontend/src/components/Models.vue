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
        <Card v-for="(each_card, index) in card_list"
              :key="index"
              :engine="each_card.engine"
              :create_time="each_card.create_time"
              :name="each_card.name"></Card>
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
      card_list: []
    }
  },
  mounted () {
    let _self = this
    this.axios.get('/api/plan/')
      .then(function (res) {
        console.log(res.data)
        _self.card_list = res.data
      })
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
