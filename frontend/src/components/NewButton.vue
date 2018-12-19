<template>
    <div id='NewButton'>
        <b-button class='mybutton' :size='size' :variant='variant'>
            {{name}}
        </b-button>
    </div>
</template>

<script>
export default {
  name: 'NewButton',
  data () {
    return {
      props: ['name', 'size', 'variant'],
      data: {
        modelname: 'abc',
        name: 'abc',
        size: 'sm',
        variant: 'warning'
      }
    }
  }
}
</script>

<style scoped>
    .mybutton {
        float: left;
        margin: 10px;
    }

    .mybutton {
        color: white;
    }
</style>
