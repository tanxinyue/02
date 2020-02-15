<template>
  <div>
    <table>
        <tr>
        
          <td>商品名称</td>
          <td>商品价格</td>
           <td>商品数量</td>
          
        </tr>
        <tr v-for="i in arry" v-if='i.id%2==0' style="background:red">

          <td>{{i.name}}</td>
          <td>{{i.price}}</td>
          <td>{{i.num}}</td>
        </tr>
         <tr v-for="i in arry" v-if='i.id%2==1' style="background:green">

          <td>{{i.name}}</td>
          <td>{{i.price}}</td>
          <td>{{i.num}}</td>
        </tr>
      </table>
  </div>

</template>

<script>
  import axios from 'axios'
    export default {
        name: "ShowGoods",
        data(){
            return{
                 arry:[],


            }
        },
        created() {
            axios({
                url:'http://127.0.0.1:8000/myapp/show/',
               method:'get',

            }).then(res=>{
                this.arry=res.data.good
            })
        }
    }
</script>




