import Vue from 'vue'
import Router from 'vue-router'
import login from '@/login_regi/index'
import home from '@/main-home/index'
import turntable from '@/turntable/index'
import one_dishes from '@/one_Dishes/index'
import cuisine from '@/cuisine/index'
import regis from '@/regis/index'


Vue.use(Router)

export default new Router({
  routes: [
    {
        path: '*',
        redirect: '/login'
    },
    {
        path: '/login',
        component: login,
    },
    {
        path:'/home',
        name:'home',
        component: home,
    },
    {
        path:'/turntable',
        component:turntable
    },
    {
        path:'/one_dishes',
        name:"one_dishes",
        component:one_dishes
    },
    {
        path:'/cuisine',
        name:"cuisine",
        component:cuisine
    },
    {
        path:'/regis',
        name:"regis",
        component:regis
    },
  ]
})
