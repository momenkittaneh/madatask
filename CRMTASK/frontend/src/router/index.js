import { createRouter, createWebHashHistory } from 'vue-router'
import store from '../store'
import Home from '../views/Home.vue'
import Signup from '../views/Signup.vue'
import LogIN from '../views/Login.vue'
import List from '../views/Dashboard/customerlist.vue'
import newcustomer from '../views/Dashboard/newcustomer.vue'
import detail from '../views/Dashboard/detail.vue'
import edit from '../views/Dashboard/edit.vue'
import service from '../views/Dashboard/service.vue'

const routes = [
  {
    path: '/service/:id',
    name: 'service',
    component: service,
    meta: {
      requireLogin: true
    }},
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
    path: '/log-in',
    name: 'LogIN',
    component: LogIN
  },
  {
    path: '/list',
    name: 'list',
    component: List,
    meta: {
      requireLogin: true
  }},{
    path: '/new',
    name: 'newcustomer',
    component: newcustomer,
    meta: {
      requireLogin: true
  }},{
    path: '/details/:id',
    name: 'detail',
    component: detail,
    meta: {
      requireLogin: true
  }},
  {
    path: '/edit/:id',
    name: 'edit',
    component: edit,
    meta: {
      requireLogin: true
    }},


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

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})

export default router
