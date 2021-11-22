<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-4 is-offset-4">
                <h1 class="title">CUSTOMERS LIST</h1>
            </div>
            <div class="column is-12">
                        <router-link to="/new">add customer</router-link>
            <form @submit.prevent="submitForm">
              <div class="field has-addons">
                <div class="control">
                  <input class="input" type="text" placeholder="Search" v-model="search">
                </div>
                <div class="control">
                  <button class="button is-info">
                    Search
                  </button>
              </div></div>
            </form>
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
                <router-link :to="{ name: 'detail', params: { id: customer.id }}">
                <th scope="row">{{customer.name}}</th>

                </router-link>

      <th scope="row">{{customer.gender}}</th>
      <th scope="row">{{customer.age}}</th>
      <th scope="row">{{customer.company}}</th>
    </tr>
  </tbody></table></div>
          <h2>services</h2>

              <table class="table">
  <thead>
    <tr>
      <th scope="col">name</th>
    </tr>
  </thead>
  <tbody>

        <tr v-for="serv in services"
        v-bind:key="serv.id"> 
                        <router-link :to="{ name: 'service', params: { id: serv.id }}">

        <th scope="row">{{serv.name}}</th> </router-link>
        </tr>
          </tbody></table>

    </div></div>
</template>
<script>
import axios from 'axios'

export default{
    name:'customerslist',
    data(){
        return {
            customers:[],
            services:[],
            search:''
        }
    },
    mounted(){
        this.getcustomers(),
        this.getservices()
    },
    methods :{
        getcustomers(){

            axios.get(`/api/v1/customers/?search=${this.search}`)
            .then( response => {
                this.customers = response.data.results

            })
            .catch(error =>{ console.log(error)})
        },
             getservices(){
        axios.get(`/api/v1/services/`)
        .then(response => {this.services=response.data})
        .catch(console.error(404))},
        submitForm(){
          this.getcustomers()
            }

    }
}

</script>
