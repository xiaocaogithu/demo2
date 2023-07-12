<template>
    <div class="aa" v-if="csrftoken">
        <div class="host" :style="{height:this.windo_list[1] +'px'}">
            <div class="left_content">
                <div class="Cuisine">
                    <img src="../assets/home2.png">
                    <div>
                        粤系菜
                        <P>粤菜可选原料多，选料精细。粤菜讲究原料的季节性，“不时不吃”。吃鱼，有“春鳊秋鲤夏三犁（鲥鱼）隆冬鲈”；吃虾，“清明虾，最肥美”；吃蔬菜要挑“时菜”，是指合季节的蔬菜，如菜心为“北风起菜心最甜”。除了选原料的最佳肥美期之外，粤菜还特别注意选择原料的最佳部位</P>
                    </div>
                </div>
                <div class="Cuisine"><img src="../assets/home2.png">
                    <div>
                        川菜
                        <P>川菜是中国汉族传统的四大菜系之一、中国八大菜系之一 [6] 。主要特点在于味型多样，变化精妙。辣椒、胡椒、花椒、豆瓣酱等是主要调味品，不同的配比，化出了麻辣、酸辣、椒麻、麻酱、蒜泥、芥末、红油、糖醋、鱼香、怪味等各种味型，无不厚实醇浓，具有“一菜一格”、“百菜百味”的特殊风味，各式菜点无不脍炙人口。川菜是中国最有特色的菜系，因此全国闻名。</P>
                    </div>
                </div>
                <div class="Cuisine"><img src="../assets/home2.png">
                    <div>
                        苏菜
                        <P>烹调技艺以炖、焖、煨著称；重视调汤，保持原汁。原为江浙菜系，是中国长江中下游地区的著名菜系，其覆盖地域甚广，包括现今江苏、浙江、安徽、上海，以及江西、河南部分地区，它有“东南第一佳味”、“天下之至美”之誉，声誉远播海内外</P>
                    </div>
                </div>
                <div class="Cuisine"><img src="../assets/home2.png">
                    <div>
                        鲁菜
                        <P>由济南和胶东两个地方清、鲜、脆、嫩著称。胶东地方菜，以烹制各种海鲜菜驰名。它的烹调技术来自福山菜，烹调方法，擅长"爆、炸、扒、蒸"，口味以鲜为主，偏重清淡，味浓厚、嗜葱蒜，尤以烹制海鲜，汤菜和各种动物内脏为长</P>
                    </div>
                </div>
                <div class="Cuisine"><img src="../assets/home2.png">
                    <div>
                        楚菜
                        <P>《史记》中曾记载了楚地"地势饶食，无饥馑之患"。湖北被称“千湖之省”，楚菜以湖北得天独厚的淡水河鲜为本，鱼馔为主，汁浓芡亮，香鲜微辣，注重本色、原汁原味，菜式丰富，筵席众多，擅长蒸、煨、炸、烧、炒等烹调方法，特点是汁浓、芡稠、口重、味纯，民间肴馔以煨汤、蒸菜、肉糕、鱼丸和米制品小吃为主体，具有滚、烂、鲜、醇、香、嫩、足“七美”之说。</P>
                    </div>
                </div>
                <div class="Cuisine"><img src="../assets/home2.png">
                    <div>
                        浙菜
                        <P>鲜嫩软滑，香醇绵糯，清爽不腻。浙江菜有悠久的历史，它的风味包括杭州、宁波和温州、金华四个地方的菜点特色。杭州菜重视原料的鲜、活、嫩，以鱼、虾、时令蔬菜为主，讲究刀工，口味清鲜，突出本味。宁波菜咸鲜合一，以烹制海鲜见长</P>
                    </div>
                </div>
            </div>
            <div class="right_content">
                <div class="main_course">
                    <p>主料 :</p>
                    <input type="text" placeholder="请输入一到两种主料">
                </div>
                <div class="main_course">
                    <p>佐料 :</p>
                    <input type="text" placeholder=" 请输入佐料">
                </div>
                <div class="action">
                    <button  @click="handleClick" >开始今日份制作</button>
                </div>
                <div class="lottery">
                    <img :src="item" id="jpg">
                </div>
                
            </div>
        </div>
        <!-- <div class="menu_true">aaas</div> -->
        <div :class='hand_display?"menu_true":"menu_false"' >
            <div class="Cuisine_1">
                <img src="../assets/home2.png">
                    <div >
                        粤系菜
                        <P>粤菜粤菜即广东菜，是中国四大菜系、八大菜系之一。狭义上的粤菜指广府菜（即广州府菜），广义上又包含潮州菜（潮汕菜）、东江菜（也称客家菜）</P>
                    </div>
            </div>
            <div class="Cuisine_1">
                <img src="../assets/home2.png">
                    <div >
                        粤系菜
                        <P>粤菜粤菜即广东菜，是中国四大菜系、八大菜系之一。狭义上的粤菜指广府菜（即广州府菜），广义上又包含潮州菜（潮汕菜）、东江菜（也称客家菜）</P>
                    </div>
            </div>
            <div class="Cuisine_1">
                <img src="../assets/home2.png">
                    <div >
                        粤系菜
                        <P>粤菜粤菜即广东菜，是中国四大菜系、八大菜系之一。狭义上的粤菜指广府菜（即广州府菜），广义上又包含潮州菜（潮汕菜）、东江菜（也称客家菜）</P>
                    </div>
            </div>
            <div class="Cuisine_1">
                <img src="../assets/home2.png">
                    <div>
                        <title>粤系菜</title>
                        <P>粤菜粤菜即广东菜，是中国四大菜系、八大菜系之一。狭义上的粤菜指广府菜（即广州府菜），广义上又包含潮州菜（潮汕菜）、东江菜（也称客家菜）</P>
                    </div>
            </div>
            <div  class="but">
                <button @click="hand_true">关闭</button>
            </div>
        </div>
    </div>
</template>

<style>
.aa{
    display: flex;
}
.host{
    display: flex;
}
.left_content{
    width:50%;
    overflow: auto;
    /* background-color: blue; */
}
.right_content{
    width: 50%;
    /* background-color:aqua; */
}
.Cuisine{
    display: flex;
    margin:2em;
}
.Cuisine_1{
    display: flex;
    margin:5px;
}
.Cuisine_1 div p{
    display: flex;
    text-indent:2em;
    align-content: space-between;
}
.Cuisine_1 img{
    border-radius: 5px 5px 5px 5px;
    margin-right: 2%;
    width: 10%;
    background-size: cover; /* 或其他调整方式 */
    background-repeat: no-repeat;
    background-position: center;
}

.Cuisine div p{
    display: flex;
    text-indent:2em;
    /* font-size:18px; */
    align-content: space-between;
}
.Cuisine img{
    border-radius: 5px 5px 5px 5px;
    margin-right: 2%;
    width: 20%;
    background-size: cover; /* 或其他调整方式 */
    background-repeat: no-repeat;
    background-position: center;
}
.main_course{
    display: flex;
    margin:20px;
    margin-top:10%;
}
.main_course p{
    font-size:20px;
}
.main_course input{
    border-radius: 5px 5px 5px 5px;
    width:80%;
    margin-left: 5px;
    font-size:16px;
}
.lottery img{
    width: 70%;
    background-size: cover; /* 或其他调整方式 */
    background-repeat: no-repeat;
    background-position: center;
}
.action{
    /* margin-top:10%; */
    /* text-align: center; */
    padding-top: 2%;
    padding-left: 3%;
}

.menu_true{
    position: absolute; 
    top:20%;
    left:20%; 
    height: 60%;
    width:60%;
    background-color: aqua;
    display: none;
}
.menu_false{
    border-radius: 25px 25px 25px 25px;
    position: absolute; 
    top:20%;
    left:20%; 
    height: 60%;
    width:60%;
    background-color: rgb(0, 0, 0,.5);
    display: block;
    color:yellow;
}
.but{
    /* margin-top:10%; */
    text-align: center;
}
.but button{

}
</style>

<script>
// import { resolve } from 'path'

export default {
    data() {
        return {
            item:require('../assets/static_1.jpg'),
            hand_display:true,
            csrftoken:'',
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
    methods:{
        async handleClick(){
            await this.action();
            await new Promise(resolve => setTimeout(resolve,4000));
            console.log('aaa');
            this.item=require('../assets/static_1.jpg');
            this.hand_display=false
        },
        action(){
            this.item=require('../assets/static_gif.gif')
            // 这这里设置发送请求向后端，等到返回数据时切换回静态图片
            return new Promise(resolve =>{
                resolve();
            })
        },
        hand_true(){
            this.hand_display=true;
        }
    }
}
</script>