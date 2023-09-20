import Vue, { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import Vuex, {createStore} from 'vuex';

const store = createStore({
    state: {
        bearerToken: null,
    },
    mutations: {
        setBearerToken(state, token) {
            state.bearerToken = token;
        },
    },
    actions: {
        updateBearerToken({ commit }, token) {
            commit('setBearerToken', token);
        },
    },
    getters: {
        getBearerToken(state) {
            return state.bearerToken;
        },
    },
})

createApp(App).use(store).use(router).use(Vuex).mount('#app')
