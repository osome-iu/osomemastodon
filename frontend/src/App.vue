<template>
  <HomeView/>
</template>

<script>
import '@/assets/css/styles.css';
import '../src/assets/js/scripts.js';
import '@/assets/js/scripts.js';
import '@/assets/js/datatables-simple-demo.js';
import '../src/assets/js/datatables-simple-demo.js';

import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import SideBar from "@/components/SideBar.vue";
import HomeView from "@/views/HomeView.vue";

export default {
    name: 'App',
    components: {
        NavBar,
        Footer,
        SideBar,
        HomeView
    },
}
</script>

<style>
body, html, #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    background-color: #fff;
}
@import'~bootstrap/dist/css/bootstrap.css';
@import '../src/assets/css/styles.css';
</style>
