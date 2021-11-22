<template>
    <nav class="nav is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
            <strong>Home Page</strong>
            </router-link></div>
        <div class="navbar-menu">
            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <router-link to="/sign-up" class="button is-sucssess"><strong>sign up</strong></router-link>
                        <router-link to="/log-in" class="button is-light"><strong>log in</strong></router-link>
                    </div>
                </div>
            </div>
        </div>
    </nav>

</template>

<script>
export default{
    name : 'navbar'
}
</script>
