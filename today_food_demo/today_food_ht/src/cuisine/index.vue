<template>
    <div class="all_cuisine">
        <div v-for="cuisine in cuisines" :key="cuisine.id" class="one_cuisine">
            <img :src="cuisine.image" class="cuisine_img">
            <p v-text="cuisine.description" class="cuisine_text"></p>
        </div>
    </div>
</template>

<style>
.all_cuisine{
    display:flex;
    flex-wrap: wrap;
    padding-left: 2%;
    padding-right: 2%;
}
.all_cuisine div{
    height: 200px;
    width: 420px;
    margin-right: 2%;
    margin-bottom: 2%;
}
.one_cuisine{
    display: flex;
}
.cuisine_img{
    border-radius: 10%;
    height: auto; 
}
.cuisine_text{
    text-indent:2em;
    align-content: space-between;
}
</style>

<script>
    export default{
        data(){
            return {
                cuisines:[
                    {image:require('@/assets/home2.png'),description:'粤菜粤菜即广东菜，是中国四大菜系、八大菜系之一。狭义上的粤菜指广府菜（即广州府菜），广义上又包含潮州菜（潮汕菜）、东江菜（也称客家菜）',id:1},
                    {image:require('@/assets/home2.png'),description:'菜品描述',id:2},
                    {image:require('@/assets/home2.png'),description:'菜品描述',id:3},
                    {image:require('@/assets/home2.png'),description:'菜品描述',id:4},
                    {image:require('@/assets/home2.png'),description:'菜品描述',id:5},
                    {image:require('@/assets/home2.png'),description:'菜品描述',id:6},
                    {image:require('@/assets/home2.png'),description:'菜品描述',id:7},
                    {image:require('@/assets/home2.png'),description:'菜品描述',id:8},
                    {image:require('@/assets/home2.png'),description:'菜品描述',id:9},
                    {image:require('@/assets/home2.png'),description:'菜品描述',id:10},

                ]
            }
        }
    }
</script>