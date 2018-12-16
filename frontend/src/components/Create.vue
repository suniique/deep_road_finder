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
      <el-form ref="form" :model="sizeForm" label-width="100px" size="medium">
        <el-form-item label="Plan Name">
          <el-input v-model="sizeForm.name"></el-input>
        </el-form-item>
        <el-form-item label="Data Engine">
          <el-select v-model="sizeForm.region" placeholder="Please Select Data Engine">
            <el-option label="Pandas" value="pandas"></el-option>
            <el-option label="MySQL" value="mysql"></el-option>
            <el-option label="Oracle" value="oracle"></el-option>
            <el-option label="TimesTen" value="timesten"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Create Time">
          <el-col :span="11">
            <el-date-picker type="date" placeholder="Date" v-model="sizeForm.date1" style="width: 100%;"></el-date-picker>
          </el-col>
          <el-col class="line" :span="2">-</el-col>
          <el-col :span="11">
            <el-time-picker type="fixed-time" placeholder="Date" v-model="sizeForm.date2" style="width: 100%;"></el-time-picker>
          </el-col>
        </el-form-item>
        <el-form-item label="Model Type">
          <el-radio-group v-model="sizeForm.resource" size="medium">
            <el-radio border label="MLP"></el-radio>
            <el-radio border label="U-Net"></el-radio>
            <el-radio border label="VGG19"></el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item size="large">
          <el-button type="primary" @click="onSubmit">Create!</el-button>
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
        sizeForm: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        }
      }
    },
    methods: {
      onSubmit () {
        console.log('submit!')
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

  .my_form {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
