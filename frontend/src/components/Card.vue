<template>
    <b-card :title="name"
        img-src="https://view.moezx.cc/images/2018/12/15/model.jpg"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-4 card">
        <p class="card-text">
            Engine: {{engine}}<br>
            CreateTime: {{create_time.slice(0, 10)}}
        </p>
        <b-button href="#/dashboard/" variant="warning">View Details</b-button>
    </b-card>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  props: ['name', 'create_time', 'engine']
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
