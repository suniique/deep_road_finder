<template>
    <b-card title="Model #1"
        img-src="https://view.moezx.cc/images/2018/12/15/model.jpg"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-4 card">
        <p class="card-text">
            Accuracy: {{props.accuracy}}<br>
            Train Time: {{props.trainTime}}
        </p>
        <b-button href="#/dashboard/" variant="warning">View Details</b-button>
    </b-card>
</template>

<script>
export default {
  data () {
    return {
      props: {
        accuracy: '',
        trainTime: ''
      },
      datas: []
    }
  }
}
</script>

<style  scoped>
    .card {
        float: left;
        margin: 10px;
        width: 250px;
    }

    .card a {
        color: white;
    }
</style>
