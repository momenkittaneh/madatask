import { createRouter, createWebHashHistory } from 'vue-router'
import store from '../store'
import Home from '../views/Home.vue'
import Signup from '../views/Signup.vue'
import LogIN from '../views/Login.vue'
import List from '../views/Dashboard/customerlist.vue'

const routes = [
  {
    path: '',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-up',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/sign-in',
    name: 'LogIN',
    component: LogIN
  },
  {
    path: '/list',
    name: 'list',
    component: List
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
//     next('/log-in')
//   } else {
//     next()
//   }
// })

export default router
