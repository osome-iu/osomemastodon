<template>
    <nav class="sb-topnav navbar navbar-expand navbar-dark" id="nav-bar">
        <div class="d-flex align-items-center m-0">
            <!-- Use ml-auto to push the button to the right -->
            <button class="btn btn-link btn-sm order-10 order-sm-10 order-lg-0 ml-auto me-9 me-lg-0" id="sidebarToggle" href="#!" aria-label="navigate-button" style="font-size:1.2rem">
                <i class="fas fa-bars" style="color:white"></i>
            </button>
            <a href="https://osome.iu.edu/" target="_blank" class="navigation-link">
                <!-- Add 'small' class to make the text smaller on smaller screens -->
                <h1 class="navbar-brand mb-0 small" style="letter-spacing: -1px; font-size: 1.5rem; font-weight: bold; margin-right: -138px; margin-left: 18px;">OSoMe</h1>
            </a>
            <!-- Add 'small' class to make the image smaller on smaller screens -->
            <router-link to="/">
                <img src="../assets/mastodon_png.png" alt="OSoMe Logo" style="width: 120px; margin-right: 20px; margin-top: 8px;" class="small" >
            </router-link>
            <!-- Add 'small' class to make the text smaller on smaller screens -->
            <router-link to="/" style="text-decoration: none;">
                <h1 class="navbar-brand mb-0 small" style="letter-spacing: -1px; font-size: 1.5rem; margin-left: -10px; font-weight: bold;">Search</h1>
            </router-link>
        </div>
    </nav>
</template>


<style scoped>

#nav-bar {
    background-color: #151C62;
    padding: 10px;
    margin-bottom: 0; /* Ensure no margin at the bottom */
}


.navbar-brand {
    margin-bottom: 0;
    font-kerning: normal;
}

.navigation-link{
    text-decoration: none;
}

.btn btn-link{
    color: black;
}
</style>
<script setup>
</script>