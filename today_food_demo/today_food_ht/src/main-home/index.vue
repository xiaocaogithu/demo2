<template>
  <div class="content" :style="{height:this.windo_list[1] +'px'}" v-if="csrftoken">
    <div class="slideshow-container">
      <div v-for="(image, index) in images" :key="index" :class="['slide', { active: index === currentIndex }]">
        <img :src="image.src" :alt="image.alt">
      </div>
    </div>
    <div class="people_msg_content" v-if="show_people_msg">
            <div>
            <div  class="upload">
                <div class="peop_msg_">
                  <img :src="avatar"/>
                  <p> 登录账号</p>
                </div>
                <div class="peop_msg_all">
                  <button class="btn-default" @click="imagecropperShow = true">
                    修改头像
                  </button>
                  <p>个人资料</p>
                </div>
                
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
        </div>
    </div>

    <div class="search">
      <div>今日厨房</div>
      <div>理想人间 吃遍世界 烹饪创意，尽在今日厨房</div>
      <p>今日厨房，是一处散发着美食和创意的灵感之地。在这里，我们尊重食材的本质，追求烹饪的精髓，让每一道菜品都展现出独特的个性与魅力。正如人生一样，每一步都应该追求卓越和创新，让自己的生命之旅充满乐趣和惊喜。让我们一起在今日厨房，用美食和创意，丰富人生的味道</p>
      <div class="search_input">
        <span></span>
        <input type="text" placeholder="  今 天 想 吃 什 么">
        <img :src="default_a" @click="search_dishes">
      </div>
    </div>
    <div class="menu">
        <div>
          <router-link to="/login">首页</router-link>
          <!-- <router-link to=""></router-link> -->
        </div>
        <div>
          <router-link to="/turntable">今日转盘</router-link>
          </div>
        <div class="people_msg" @click="switch_people_msg">
          个人中心
        </div>
        <div>厨房佐料</div>
    </div>

    <!-- <div v-if="showPopup" class="popup">
      <vue-hcaptcha sitekey="157d50d2-fb29-4919-82dc-ae9876967c74" @verify="callback">aaa</vue-hcaptcha>
    </div> -->
    <div class="food_recomment">
    <div class="div-container" ref="container" >
      <div v-for="(di, index) in column" :key="index" class="div-item">
        <div  v-for="(div,index1) in visibleDivs[di-1]" :key="index1"   @click="one_dishes" class="icon-items">
          <div v-for="(d,index2) in div" :key="index2" class="ico-item">
            <h3>{{d.title}}</h3>
            <p>{{d.content}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
    <div id="loading-message" style="display: none;">正在加载...</div>
  </div>
</template>

<style>
*{
  margin: 0;
}
.content{
  /* height: 700px; */
  width:100%;
}
.slideshow-container {
  position: relative;
  width: 100%;
  height: 60%; /* 设置轮播图的高度 */
  overflow: hidden;
}
.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.5s ease-in-out;
}
.slide.active {
  opacity: 1;
}
.slideshow-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.search{
  height: 60%;
  width: 33%;
  position:absolute;
  top:10%;
  right: 40%;
  font-size:50px;
  color:tomato;
  font-family:cursive;
  z-index: 88;
}
.search div:nth-child(2){
  margin-top:20px;
  font-size:25px;
  font-family:cursive;

}
.search p{
  margin-top:20px;
  font-size:20px;
  color:rgb(156, 189, 164);
  font-family:cursive;
  text-indent:2em
}
.search_input{
  position: relative;
}
.search_input input{
  font-family:cursive;
  font-size:20px;
  margin-top:10%;
  width:100%;
  border-radius: 25px 25px 25px 25px;
  height: 30px;
}
.search_input img{
  position: absolute;
  margin-top:-7%;
  right:0;
}
.menu{
  display:flex;
  position:absolute;
  right: 10%;
  top:0;
}
.menu div{
  margin-top:20px;
  margin-left:60px;
  color:chocolate;
}
.food_recomment{
  height: 60%;
}
.div-container{
  height:50%;
}
.ico-item{
  width: 100%;
  height: 100%;
  margin:2px;
  background-color:rgb(29, 75, 136);
}
.div-item{
  height:100%; 
  display: flex;
  width:100%;
  margin:2px;
  /* 设置容器高度以进行滚动测试 */

}
.icon-items{
  display: flex;
  height:100%;
  width: 100%;
}
.peoplr_msg{
  position: absolute;
}
.people_msg_content{
  /* display: block; */
  position: absolute;
  height: 17%;
  width: 15%;
  right:15%;
  top:10%;
  background-color: aqua;
  z-index: 999;
  border-radius: 25px;
}
.peop_msg_ img{
  width: 4em;
  height: 4em;
  border-radius: 15px;
  margin: 1em;
}
.peop_msg_{
  display: flex;
  align-items: center;

}
.peop_msg_ p{
  justify-content: center;
        align-items: center;
        text-align: center;
}
.btn-default{
 left:20px;
}
.peop_msg_all{
  display: flex;
  padding: 15px;
}
.peop_msg_all button{
  margin-right: 10%;
}

</style>

<script>
import axios  from 'axios';
import Cookies from 'js-cookie'
import md5 from 'md5'
import i from "../assets/上传中.png"
import myUpload from "vue-image-crop-upload";
import VueHcaptcha from '@hcaptcha/vue-hcaptcha';
import { computed } from 'vue';

export default {
  components: { VueHcaptcha },
  components: {
        "my-upload": myUpload,
    },
  data() {
    return {
      images: [
        // { src: require('../assets/home2.png'), alt: 'Image 1' },
        // { src: require('../assets/home1.webp'), alt: 'Image 2' },
        // { src: require('../assets/home22.webp'), alt: 'Image 3' }
      ],
      currentIndex: 0,
      divs: [], // 存储所有的div信息
      visibleDivs: [], // 当前可见的div数组
      column:1,
      visibleDivsCount: 4, // 初始可见的div数量
      showLoader: false, // 是否显示加载器
      default_a:require('@/assets/search.png'), alt: 'Image',
      show_people_msg:false,
      time_parameters:'a',
      showPopup: false,
      csrftoken:'',
      imagecropperKey: 0,
      avatar: i,
      imagecropperShow: false,

    };
  },
  mounted() {
    this.startSlideshow();
    this.getDivs(); // 获取div信息
    window.addEventListener('scroll', this.handleScroll);
    this.csrftoken =localStorage.getItem('csrftoken')
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    startSlideshow() {
      setInterval(() => {
        this.currentIndex = (this.currentIndex + 1) % this.images.length;
      }, 2000); // 切换间隔时间（以毫秒为单位），这里设置为3秒
    },
    getDivs() {
      // 使用你自己的逻辑获取div信息
      // 例如，从API端点获取数据或手动创建数据
      // 这里仅作示例

      // 使用共享参数这里
      var parameters=this.validateParams(this.$store.state.parament)
      if (parameters){
            axios.post('http://127.0.0.1:8000/backend/home/',{params:{'column':this.column}}).then(res=>{
              this.divs.push(res.data)
              console.log(this.divs)
              console.log('bbbbbb')
              this.visibleDivs=this.divs
              // for()
            },err =>{
              console.log(err)
            })
        }
      else{
          // this.showPopup=true
          // alert('等我搞好这个人机验证，我看你怎么爬')
      }
      
    },
    validateParams(params) {
      // 在这里进行参数验证，根据你的需求编写验证逻辑
      // if (!params) {
      //   return false
      // }
      return true;
    },
    callback(response){
      alert("aaa")
    },
    handleScroll() {
      const container = this.$refs.container;
      const containerHeight = container.offsetHeight;
      const scrollPosition = window.innerHeight + window.pageYOffset;
      if (scrollPosition >= containerHeight && !this.showLoader) {
        this.showLoader = true;
        console.log("鼠标滚动了")
        this.loadMoreDivs();
      }
    },
    loadMoreDivs() {
      // 模拟异步加载更多的div信息
      setTimeout(() => {
        this.column+=1;
        this.visibleDivsCount += 4; 
        // 增加可见的div数量
        this.updateVisibleDivs();
        this.showLoader = false;
      }, 1000);
    },
    updateVisibleDivs() {
      this.getDivs();
      console.log(this.column)
      this.visibleDivs = this.divs
      // this.visibleDivs = this.divs[this.column-2][this.column-1];
      console.log(this.visibleDivs)
      console.log("hskdjhasdkjhla")
    },
    one_dishes(){
      this.$router.push({
        path:"/one_dishes",
        name:'one_dishes',
        params:{userList:'userlist'}
      })
    },
    switch_people_msg(){
      this.show_people_msg=! this.show_people_msg
    },
    search_dishes(){
      // 这里通过用户搜索的菜名去搜索，传菜名id
      this.$router.push({
        path:"/cuisine",
        name:'cuisine',
        params:{userList:'userlist'}
      })
    },
    cropSuccess(imgDataUrl, field) {
            console.log("-------- crop success --------");
            console.log(imgDataUrl);
            //把头像设置成上传的图片
            this.avatar = imgDataUrl;
            console.log(field);
        },
        //上传成功回调
    cropUploadSuccess(res, originPicName) {
        //res是后端返回的结果，originPicName是后端接收到图片的名字
            console.log("-------- upload success --------");
            console.log(res);
            this.imagecropperShow = false;
            this.imagecropperKey = this.imagecropperKey + 1;
        },
        //上传失败回调
        cropUploadFail(status, field) {
            console.log("-------- upload fail --------");
            console.log("上传失败状态" + status);
            console.log("field: " + field);
        },
  },
  created(){
    var window_=[]
    window_.push(window.screen.width)
    window_.push(window.screen.availHeight)
    this.windo_list=window_
    console.log(this.windo_list)
    // var catid=this.$route.params.userdata
    // this.time_parameters=catid
    // alert(catid)
  },
  // computed(){

  // }
};
</script>
