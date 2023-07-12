// store/index.js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
  // 定义状态
  state: {
    // 定义需要管理的状态
    parament: null,
  },
  // 定义修改状态的方法
  mutations: {
    // 定义修改parameter状态的方法
    setParament(state, payload) {
      state.parament = payload;
    },
  },
});

export default store;
