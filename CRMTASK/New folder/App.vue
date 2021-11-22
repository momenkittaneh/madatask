<template>
    <div>
        <navbar />

        <section class="section">
            <router-view/>
        </section>
    </div>
</template>

<script>
    import axios from 'axios'
    import navbar from '@/components/layout/navbar'
    export default {
        name: 'App',
        components: {
            navbar
        },
   
    }
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
