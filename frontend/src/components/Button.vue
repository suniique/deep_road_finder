<template>
    <div class="col-md-4">
        <b-button class='mybutton' :size='props.size' :variant='props.variant'>
            Model #1
        </b-button>
    </div>
</template>

<script>
export default {
  data () {
    return {
      props: {
        size: 'sm',
        variant: 'warning'
      }
    }
  }
}
</script>

<style  scoped>
    .mybutton {
        float: left;
        margin: 10px;
    }

    .mybutton {
        color: white;
    }
</style>
