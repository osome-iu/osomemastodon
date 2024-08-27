import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../src/assets/css/IU_brand.css';
import VueScrollTo from 'vue-scrollto';

const app = createApp(App);
app.use(router);
app.use(VueScrollTo, {
    offset: -110,
})

app.mount('#app')
