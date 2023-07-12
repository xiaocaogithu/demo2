<template>
    <div class="home" v-if="csrftoken">
        <div class="step">
            <div v-for="(Block,index) in steps" :key="index" class="grid-item" >
                <div>
                    <img :src="Block.image" class="dishes_img">
                    <p v-text="Block.description" class="dishes_text"></p>
                </div>
                <div v-if="index<steps.length">
                    <div v-if="[3, 4,11,12].includes(index)" >
                        <div v-if="Block.image!=''">
                            <img src="@/assets/箭头_下.png" class="step_img">
                        </div>
                    </div>
                    <div v-else-if="index>3 && index<=7 || index>=11">
                        <div v-if="Block.image!=''">
                            <img src="@/assets/箭头_左.png" class="step_img">
                        </div>
                    </div>
                    <div v-else>
                        <div v-if="Block.image!=''">
                            <img src="@/assets/箭头_右.png" class="step_img">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="comment">
            <img src="@/assets/评论.png" @click="post_comments">
        </div>
        <div v-if="isPopupVisible" id="popup" @scroll="handleScroll">
            <div class="user_msg">
                <div class="user_comment" v-for="comment in comments" :key="comment.id">
                <div class="user_msg1">
                    <p>用户名</p>
                    <p>用户头像</p>
                </div>
                <div class="scroll_reply">
                    <p>{{ comment.content}}</p>
                    <div v-for="reply in comment.replies" :key="reply.id">
                            <p>{{ reply.content }}</p>
                            <!-- 显示回复的用户信息等 -->
                    </div>
                </div>
                
                <div class="comment_all">
                        <div class="comment_">
                            <img src="@/assets/点赞.png">
                            <div class="comment_love_replace">
                                <p>1654</p>
                                <p>点赞</p>
                            </div>
                        </div>
                        <div class="comment_">
                            <img src="@/assets/回复.png" @click="reply(comment)">
                            <div class="comment_love_replace">
                                <p>1654</p>
                                <p>回复</p>
                            </div>
                        </div>
                </div>
                </div>
                
            </div>
        </div>
        <!-- <div>
            <div  class="upload">
                <img :src="avatar"/>
                <button class="btn btn-default" @click="imagecropperShow = true">
                    修改头像
                </button>
            </div>
            <div>
            <my-upload
                :modelValue.sync="imagecropperShow"
                :key="imagecropperKey"
                lang-type="zh"
                img-format="png"
                @crop-success="cropSuccess"
                @crop-upload-success="cropUploadSuccess"
                @crop-upload-fail="cropUploadFail"
            ></my-upload>
        </div>
        </div> -->
    </div>
</template>

<style>
.home{
    height: 100vh;
    width:100vw;
}
.step{
    display: flex;
    flex-wrap: wrap;

    /* height:1000px */
}
.step_1{
    display: flex;
    flex-wrap: wrap;

}
.grid-item{
  flex: 1 0 calc(25% - 10px);
   /* 设置项目宽度为三分之一，减去间隔宽度 */
  /* height: 50%;  */
  /* 设置项目高度 */
  margin-bottom: 20px; 
  /* 设置项目间隔 */
  /* background-color: #f0f0f0; */
  display: flex;
}
.step_img{
    margin-top: 50%;
    width: 100%;
    background-size: cover; /* 或其他调整方式 */
    background-repeat: no-repeat;
    background-position: center;
}

.dishes_img{
    width: 100%;
    background-size: cover; /* 或其他调整方式 */
    background-repeat: no-repeat;
    background-position: center;
}
/* .reserver{ */
    /* display: flex;  */
    /* flex-wrap: wrap;
    flex-direction: row-reverse; */
/* } */
.comment{
    position: absolute;
    top:50%;
    right:0;
    /* display: flex;
    flex-wrap: wrap; */

}
.comment img{
    height: 10%;
    width: 30%;
    float: right;
}

#popup {
    position: fixed;
    top:60%;
    right: 100px;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    height: 600px;
    background-color: #fff;
    border: 1px solid #ccc;
    transition: bottom 1s ease;
    /* background-color: rgba(254, 254, 255, 0.5); */
    /* z-index: 9999;  */
    /* 确保遮罩层位于其他元素之上 */
    /* pointer-events: none; */
     /* 防止遮挡下方元素的交互事件 */
    transition: opacity 1s ease; /* 添加过渡效果 */
    overflow: auto;
}
#popup div{
    z-index: 999; 
}

.user_msg1{

}
.user_comment{
    display: flex;
    justify-content: space-between;
    margin-right: 20px;
}
.user_msg{
    /* display: flex; */
    width: 100%;
    height: 20%;
    justify-content: space-between;
}
.comment_ img{
    height: 40%;
    width:40%;
    left:50%;
    text-align: center;
}
.comment_{
    /* margin-right: 10%; */
    height: 100%;
    width: 100%;
}
.comment_love_replace{
    display: flex;
}
.comment_all{
    display: flex;
}
.scroll_reply{
    overflow: hidden;
}

</style>

<script>
// import { generateId } from './utils';

// 然后在组件中使用 generateId() 函数
import axios from "axios";
import i from "../assets/上传中.png"
import myUpload from "vue-image-crop-upload";

// import { mapGetters } from "vuex";

export default {
    components: {
        "my-upload": myUpload,
    },
    data(){
        return {
            steps:[
                {image:require('@/assets/home2.png'),description:'菜品描述'},
                {image:require('@/assets/home2.png'),description:'菜品描述'},
                {image:require('@/assets/home2.png'),description:'菜品描述'},
                {image:require('@/assets/home2.png'),description:'HTML5 的 FileReader 提供了一种新的方式来读取用户本地设备的文件，我们可以利用它来完成图片上传。这种方式可以避免浏览器的默认提交和页面跳转，也更加友好地与 Vue 的组件化开发方式结合起来。'},
                {image:require('@/assets/home2.png'),description:'菜品描述1'},
                {image:require('@/assets/home2.png'),description:'菜品描述2'},
                {image:require('@/assets/home2.png'),description:'本文介绍了在 Vue 中实现图片上传的三种方法，它们分别是使用第三方插件、原生 Ajax 以及利用 HTML5 的 FileReader。每种方法都有其优缺点，开发者可以根据项目的实际需求来选择合适的方法。图片上传是一个常见的功能，掌握这些上传的方法也是 Vue 开发者必备的技能之一。 '},
                {image:require('@/assets/home2.png'),description:'菜品描述4'},
                {image:require('@/assets/home2.png'),description:'菜品描述'},
                {image:require('@/assets/home2.png'),description:'HTML5 的 FileReader 提供了一种新的方式来读取用户本地设备的文件，我们可以利用它来完成图片上传。这种方式可以避免浏览器的默认提交和页面跳转，也更加友好地与 Vue 的组件化开发方式结合起来。'},
                {image:require('@/assets/home2.png'),description:'HTML5 的 FileReader 提供了一种新的方式来读取用户本地设备的文件，我们可以利用它来完成图片上传。这种方式可以避免浏览器的默认提交和页面跳转，也更加友好地与 Vue 的组件化开发方式结合起来。'},
                // {image:require('@/assets/home2.png'),description:'菜品描述'},
                // {image:require('@/assets/home2.png'),description:'菜品描述5'},
                // {image:require('@/assets/home2.png'),description:'菜品描述6'},
                // {image:require('@/assets/home2.png'),description:'菜品描述7'},
                // {image:require('@/assets/home2.png'),description:'菜品描述8'},
                // {image:require('@/assets/home2.png'),description:'菜品描述'},
            ],
            imagecropperShow: false,
            imagecropperKey: 0,
            //img的src值
            avatar: i,
            window_:[],
            isPopupVisible: false,
            comments: [{
                        id: 1,
                        content: "这是一条评论",
                        replies: []
                        },
                        {
                        id: 2,
                        content: "这是一条评论",
                        replies: []
                        },
                    ],
            csrftoken:'',
        }
    },
    methods:{
        post_comments(){
            this.isPopupVisible= !this.isPopupVisible
        },
        handleScroll(event) {
            event.stopPropagation();
        },
        reply(comment) {
        // 创建回复对象
            const reply = {
            id: 1, // 生成唯一ID
            content: "asdasdasd",
            // 其他属性...
            };
            comment.replies.push(reply); // 将回复对象添加到评论的回复数组中
        },
        generateId() {
            return Date.now().toString(36) + Math.random().toString(36).substr(2, 5);
        }   
        
    },
    created(){
        var window_=[]
        window_.push(window.screen.width)
        window_.push(window.screen.availHeight-100)
        this.windo_list=window_
        console.log(this.windo_list)
        this.csrftoken =localStorage.getItem('csrftoken')

    },
    beforeMount(){
        if (this.steps.length>4){
            for(var i=0;i<=this.steps.length;i++){
                if([3, 7, 11, 15].includes(i)){
                    let num =this.steps.slice(i+1,i+5);
                    num.reverse()
                    console.log(...num)
                    this.steps.splice(i+1,4,...num)
                    console.log(this.steps)
                }
            }
        }
    },
    mounted(){
        console.log(this.steps)
        console.log(this.steps.length)
        if (this.steps.length%4!=0){
            var add_length=(Math.floor(this.steps.length/4)+1)*4-this.steps.length
            for( var i =0 ;i<add_length;i++){
                this.steps.push({image:'',description:''},)
            }
            console.log(this.steps.length)
        }
        else{
            console.log('4的倍数')
        }
    }
}
</script>