<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add customer</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="customer.name">
                        </div>
                    </div>

                    <div class="field">
                        <label>age</label>
                        <div class="control">
                            <input type="text" class="input" v-model="customer.age">
                        </div>
                    </div>

                    <div class="field">
                        <label>company</label>
                        <div class="control">
                            <input type="text" class="input" v-model="customer.company">
                        </div>
                    </div>


                    <div class="field">
                        <label>gender</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="customer.gender">
                                    <option value="Male">Male</option>
                                    <option value="Female">Female</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
                                <form @submit.prevent="deleteForm">
                                        <button class="button is-success">delete</button>
                                </form>

            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { toast } from 'bulma-toast'
    export default {
        name: 'edit',
        data() {
            
            return {

                customer: {}
        }},
        mounted(){
    this.getcustomer()
},
methods : {
     getcustomer(){
        const customerid = this.$route.params.id
        axios.get(`/api/v1/customers/${customerid}/`)
        .then(response => {this.customer=response.data})
        .catch(console.error(404))

    },
        submitForm() {
        const customerid = this.$route.params.id
        this.$store.commit('setIsLoading', true)
        axios
            .patch(`/api/v1/customers/${customerid}/`, this.customer)
            .then(response => {
                this.$router.push('/list')
            })
            .catch(error => {
                console.log(error)
            })
        this.$store.commit('setIsLoading', false)
    },
            deleteForm() {
        const customerid = this.$route.params.id
        this.$store.commit('setIsLoading', true)
        axios
            .delete(`/api/v1/customers/${customerid}/`, this.customer)
            .then(response => {
                this.$router.push('/list')
            })
            .catch(error => {
                console.log(error)
            })
        this.$store.commit('setIsLoading', false)
    }

}

    }
</script>
