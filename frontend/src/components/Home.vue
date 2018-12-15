<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container">
        <h1>Deep Road Finder -- Monitor your Nerual Network Training Process</h1>
        <h2>In Memory Database Project</h2>
        <ul>
          <li><router-link to="/dashboard">DashBoard</router-link></li>
          <li><router-link to="/results">Results</router-link></li>
          <li><router-link to="/models">Models</router-link></li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'home'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .home {
    display: flex;
    align-items: center;
    align-content: center;
    justify-content: center;
  }
  h1, h2 {
    font-weight: normal;
  }

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
    text-decoration: underline;
  }
</style>
