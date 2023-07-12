<template>
    <div class="home_bg_img" :style="{width:this.windo_list[0] +'px',height:this.windo_list[1] +'px'}">
        <!-- <div></div> -->
        <div class="login_bg_img" :style="{width:this.windo_list[0]/3+'px',height:this.windo_list[1]/2 +'px'}">
            <div>
            <span>账号</span> <input type="text" ref="name">
            </div>
            <div>
            <span>邮箱</span> <input type="email" ref="email">
            </div>
            <div>
            <span>密码</span>  <input type="password" ref="password">
            </div>
            <span class="prompt">提示:密码等级必须包含一个字母并且长度在6以上</span>
            <div class="but">
                <button @click="get_input">
                    登录
                </button>
                <button @click="get_input">注册</button>
            </div>
        </div>
    </div>
</template>
<script>
import axios from "axios"
import md5 from 'md5'
import Cookies from 'js-cookie'
import { mapState, mapMutations } from 'vuex'
// axios.defaults.xsrfHeaderName = "X-CSRFToken";
// axios.defaults.xsrfCookieName = "csrftoken";
export default {
        name:'login_home',
        data(){
            return {
                window_:[],
                data_list:[]
            }
        },
        created(){
            var window_=[]
            window_.push(window.screen.width)
            window_.push(window.screen.availHeight-70)
            this.windo_list=window_
            console.log(this.windo_list[1]/2);
        },
        methods:{
            ...mapMutations(['setParament']),
            get_input(){
                if(!this.$refs.name.value){
                    alert('账号不能为空');
                }
                else if(!this.$refs.email.value){
                    alert('邮箱不能为空');

                }else if(!this.$refs.password.value){
                    alert('密码不能为空');
                }
                else{
                    var email_check= new RegExp(/^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/)
                    if (false==email_check.test(this.$refs.email.value)){
                        alert('邮箱');
                    }
                    else{
                    var strongRegex = new RegExp("^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
                    var mediumRegex = new RegExp("^(?=.{7,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
                    var enoughRegex = new RegExp("(?=.{6,}).*", "g");
                    if (false == enoughRegex.test(this.$refs.password.value)) {
                        alert('密码安全等级为弱');
                        } else if(false == mediumRegex.test(this.$refs.password.value)){
                            alert('密码安全等级为中等');
                        }else if(false == strongRegex.test(this.$refs.password.value)){
                            alert('强');
                            this.data_list.push(this.$refs.name.value)
                            this.data_list.push(this.$refs.email.value)
                            this.data_list.push(this.$refs.password.value)
                            console.log(this.$refs.name.value.length)
                            const md5encrypt =md5(String(this.$refs.name.value)+String(this.$refs.password.value))
                            Cookies.set('data',md5encrypt)
                            localStorage.setItem('csrftoken',md5encrypt)
                            const csrftoken = Cookies.get('data');
                            this.setParament(csrftoken)
                            alert(this.parament)
                            axios.get('/backend/getcookie',{
                                params:{
                                    'msg':csrftoken
                                }
                            }).then(res=>{
                            console.log(res.data);
                        },err=>{
                            console.log('err');
                        }),
                        this.$router.push({
                                path:"/home",
                                name:'home',
                                params:{userdata:md5encrypt}
                            })
                        }
                    }
                }
            }
        },
        computed:{
            ...mapState(['parament'])
        }
    }
</script>

<style>
    *{
        margin: 0;
        padding: 0;
    }
    .home_bg_img{
        background-image: url('../assets/home2.png');
        background-size: cover; /* 或其他调整方式 */
        background-repeat: no-repeat;
        background-position: center;
        display: flex;
      /* 水平垂直居中 */
        justify-content: center;
        align-items: center;
    }
    .login_bg_img{ 
        background-color: rgb(246,244,240);
        border-radius: 50%;
        display: flex;
      /* 水平垂直居中 */
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .login_bg_img div{
        margin: 20px;
    }
    .login_bg_img div input{
        font-weight:700;
        margin: 10px;
        width:72%;
        height: 20px;
        size:10px;
        border-radius: 25px 25px 25px 25px;
        background-color:rgb(194, 194, 216);
    }
    .login_bg_img div span{
        color:rgb(181,97,37);
        font-weight:700;

    }
    .login_bg_img div button{
        color:rgb(119,131,57);
        margin: 20px;
        font-size: 15px;
        height: 30px;
        width: 90px;
    }
    .but :hover {
        background-color:rgb(120, 177, 148) ;
    }
    .prompt{
        color:rgb(124, 146, 126)
    }
</style>