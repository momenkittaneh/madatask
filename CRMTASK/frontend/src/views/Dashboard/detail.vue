<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-4 is-offset-4">
                <router-link to="/" class="button is-light">EDIT</router-link>
            </div>
            <div class="column is-12">
                <h1>not found</h1>
      <h2>{{customer.name}}</h2>
      <h2>{{customer.gender}}</h2>
      <h2>{{customer.age}}</h2>
      <h2>{{customer.company}}</h2>
 </div>
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
        customer:{}
    }
},
mounted:{
     getcustomer(){
        const customerid = this.$route.params.id
        axios.get(`/api/v1/customers/${customerid}/`)
        .then(response => {this.customer=response.data})
        .catch(console.error(404))

    }
}





}
</script>
