import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import AddGood from "../components/AddGood";
import ShowGoods from "../components/ShowGoods";


Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
 
    {
      path:'/goods',
      name:'AddGood',
      component:AddGood
    },{
     path:'/update_cate/:id',
      name:'UpdateCate',
      component:UpdateCate
    },{
     path:'/show_goods',
      name:'ShowGoods',
      component:ShowGoods
    }
]
})
