<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light fixed-top p-st">
            <div class="container">
                <AppLogo/>
                <button
                    class="navbar-toggler"
                    type="button"
                    data-toggle="collapse"
                    data-target="#navbarContentSupport"
                    aria-controls="navbarContentSupport"
                    aria-expanded="false"
                    aria-label="Toggle navigation">
                </button>
                <div class="collapse navbar-collapse" id="navbarContentSupport">
                    <ul class="navbar-nav ml-auto">
                        <li class="nav-item mx-2">
                            <a class="nav-link"
                               href="/about" style="color: white">About</a>
                        </li>
                        <li class="nav-item mx-2 ">
                            <a class="nav-link"
                               href="/documentation" style="color: white">Documentation</a>
                            <i class="fas fa-bars"></i>
                        </li>
                        <li class="nav-item mx-2 ">
                            <a class="nav-link"
                               href="/documentation" style="color: white"><i class="fa fa-bars" aria-hidden="true"></i></a>
                            <i class="bi bi-0-square"></i>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
import AppLogo from "./helpers/AppLogo.vue";
export default {
    name: "AppNavBar",
    components: {
        AppLogo,
    },
};
</script>

<style scoped>

.navbar {
    background-color: rgb(153, 0, 0);
    text-align: center;
}

.navbar-nav{
    color: white;
}

.nav-link{
    color:white;
}

button {
    border: none;
    outline: none;
}

button:hover {
    border: none;
    outline: none;
}

nav {
    border-bottom: 1px solid rgba(160, 159, 159, 0.336);
    position: fixed !important;
}

</style>
