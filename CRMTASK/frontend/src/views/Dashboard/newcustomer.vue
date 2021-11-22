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
                            <input type="text" class="input" v-model="name">
                        </div>
                    </div>

                    <div class="field">
                        <label>age</label>
                        <div class="control">
                            <input type="text" class="input" v-model="age">
                        </div>
                    </div>

                    <div class="field">
                        <label>company</label>
                        <div class="control">
                            <input type="text" class="input" v-model="company">
                        </div>
                    </div>


                    <div class="field">
                        <label>gender</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="gender">
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
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { toast } from 'bulma-toast'
    export default {
        name: 'newcustomer',
        data() {
            return {
                name: '',
                age: '',
                company: '',
                gender: 'Male',
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const customer = {
                name: this.name,
                age: this.age,
                company: this.company,
                gender: this.gender,
                }
                await axios
                    .post('/api/v1/customers/', customer)
                    .then(response => {
                        toast({
                            message: 'The customer was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
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
