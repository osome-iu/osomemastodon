<template>
    <div class="sb-nav-fixed">
        <NavBar/>
        <div id="layoutSidenav">
            <SideBar/>
            <div id="layoutSidenav_content">
                <router-view/>
                <Footer/>
            </div>
        </div>
    </div>
</template>

<script>
import Footer from '../components/Footer.vue';
import NavBar from '../components/NavBar.vue';
import SideBar from '../components/SideBar.vue';
import InstanceData from '../components/InstanceData.vue';
export default {
    name: 'HomeView',
    components: {
        NavBar,
        Footer,
        SideBar,
        InstanceData
    },
    data() {
        return {
        };
    }
}
</script>

<style>
body, html, #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    background-color: #fff;
    margin-top: 10px;
    margin-bottom: 20px;
}

#layoutSidenav_content{
    padding-top: -10px;
}
@import'~bootstrap/dist/css/bootstrap.css';

</style>