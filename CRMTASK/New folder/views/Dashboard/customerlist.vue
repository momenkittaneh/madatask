<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-4 is-offset-4">
                <h1 class="title">CUSTOMERS LIST</h1>
            </div>
            <div class="column is-12">
            <table class="table">
  <thead>
    <tr>
      <th scope="col">name</th>
      <th scope="col">gender</th>
      <th scope="col">age</th>
      <th scope="col">company</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="customer in customers"
        v-bind:key="customer.id">
      <th scope="row">{{customer.name}}</th>
      <th scope="row">{{customer.gender}}</th>
      <th scope="row">{{customer.age}}</th>
      <th scope="row">{{customer.company}}</th>
    </tr>
  </tbody></table></div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default{
    name:'customerslist',
    data(){
        return {
            customers:[]
        }
    },
    mounted(){
        this.getcustomers()
    },
    methods :{
        getcustomers(){

            axios.get('/api/v1/customers')
            .then( response => {
                this.customers = response.data

            })
            .catch(error =>{ console.log(error)})
        }
    }
}

</script>
