<template>
    <div>
      <form action="" @submit.prevent="on_submit">
            <p>商品名称：<input type="text" v-model="name"></p>
            <p>商品价格：<input type="text" v-model="price"></p>
            <p>商品数量：<input type="text" v-model="num"></p>
           
        </form>

    </div>
</template>

<script>
  import axios from 'axios'
    export default {
      
        data(){
            return{
                name:'',
            price:'',
            num:'',
         
              
            }
        },
        methods:{
            on_submit(){
                let form_data = new FormData()
            
            form_data.append('name', this.name)
            form_data.append('price', this.price)
            form_data.append('num', this.num)
         
                axios({
                    url:'http://127.0.0.1:8000/myapp/add/',
                    method:'post',
                    data:form_data,
                }).then(res=>{
                    alert('添加成功')
                })

            }
        }
    }
</script>

<style scoped>

</style>





