<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-4 is-offset-4">
                <router-link :to="{ name: 'edit', params: { id: customer.id }}">edit</router-link>
            </div>
            <div class="column is-12">
      <h2>{{customer.name}}</h2>
      <h2>{{customer.gender}}</h2>
      <h2>{{customer.age}}</h2>
      <h2>{{customer.company}}</h2>
 </div>
 
        </div>
        
        <h2>services</h2>
        <div v-for="serv in services"
        v-bind:key="serv.id">
           <h3 > {{serv.name}} </h3><br> 
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name : 'detail'
,
data(){
    return{
        customer : {},
        services : []
    }
},
mounted(){
    this.getcustomer()
    this.getservices()
},
methods : {
     getcustomer(){
        const customerid = this.$route.params.id
        axios.get(`/api/v1/customers/${customerid}/`)
        .then(response => {this.customer=response.data})
        .catch(console.error(404))},
     getservices(){
        axios.get(`/api/v1/services/`)
        .then(response => {this.services=response.data})
        .catch(console.error(404))}
}





}
</script>
