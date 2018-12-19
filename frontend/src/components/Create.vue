<template>
  <section class="container">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/dashboard">Dashboard</router-link></li>
      <li><router-link to="/results">Results</router-link></li>
      <li><router-link to="/models">Models</router-link></li>
    </ul>
    <h1>Create A Training Plan</h1>
    <div class="columns my_form">
      <el-form ref="form" :model="modelForm" label-width="100px" size="medium">
        <el-form-item label="Plan Name">
          <el-input v-model="modelForm.name"></el-input>
        </el-form-item>
        <el-form-item label="Data Engine">
          <el-select v-model="modelForm.engine" placeholder="Please Select Data Engine">
            <el-option label="Pandas" value="pandas"></el-option>
            <el-option label="MySQL" value="mysql"></el-option>
            <el-option label="Oracle" value="oracle"></el-option>
            <el-option label="TimesTen" value="timesten"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Model Args">
          <el-input v-for="(arg,index) in modelForm.args_list" :key="index" class="my_form" v-model="modelForm.args_list[index]"></el-input>
          <b-button class="mybutton" size="sm" variant="warning" v-on:click="addArg">
            Add New Arg
          </b-button>
          <b-button class="mybutton" size="sm" variant="warning" v-on:click="removeArg">
            Remove Arg
          </b-button>
        </el-form-item>
        <el-form-item label="Model Type">
          <el-radio-group v-model="modelForm.model" size="medium">
            <el-radio border label="MLP"></el-radio>
            <el-radio border label="U-Net"></el-radio>
            <el-radio border label="VGG19"></el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item size="large">
          <el-button type="primary" v-on:click="onSubmit">Create!</el-button>
          <el-button>Cancel</el-button>
        </el-form-item>
      </el-form>
    </div>
  </section>
</template>

<script>
  export default {
    data () {
      return {
        modelForm: {
          name: '',
          engine: '',
          model: '',
          args_list: [''],
          repository: 1,
          para: ''
        }
      }
    },
    methods: {
      onSubmit () {
        this.modelForm.para = this.modelForm.args_list.join()
        console.log(this)
        this.axios.post('/api/plan/', this.qs.stringify(
          {
            'name': this.modelForm.name,
            'engine': this.modelForm.engine,
            'repository': this.modelForm.repository,
            'para': this.modelForm.para,
            'model': this.modelForm.model
          }))
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
      },
      addArg () {
        this.modelForm.args_list.push(' ')
      },
      removeArg () {
        this.modelForm.args_list.pop()
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

  .my_form {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
