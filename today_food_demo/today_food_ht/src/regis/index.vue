<template>
    <div class="regi_all">
        <div class="animo">
            <img :src="imageSrc" :style="{ opacity :imageOpacity}">
        </div>

    </div>
</template>

<style>
.animo{
  position: relative;
  width: 100%;
  height: 100%;
}
#fade-in-image {
  opacity: 0; /* 初始时设置图片透明度为 0 */
  transition: opacity 2s; /* 定义过渡效果的持续时间为 2 秒 */
}

</style>

<script>
    export default{
        data(){
            return  {
                imageSrc:require('@/assets/home2.png'),
                imageOpacity:0,
            }
        },
        methods:{
            fadeInImage() {
                    setTimeout(() => {
                        this.imageOpacity = 1;
                    }, 1000); // 设置延迟 1000 毫秒，使图片逐渐显示
                },
        },
        mounted() {
            this.fadeInImage();
        },
    }
</script>