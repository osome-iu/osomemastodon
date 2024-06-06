<template>
    <nav class="sb-topnav navbar navbar-expand navbar-dark" id="top-nav-bar">
        <a href="https://www.iu.edu" title="Indiana University">
            <img class ="indiana-university-logo" src="//assets.iu.edu/brand/3.2.x/trident-large.png" alt="Indiana University Logo">
        </a>
        <a class="indiana-university-h1" href="https://www.iu.edu" title="Indiana University">
            <p style="color: black; text-transform: uppercase; font-family: 'Benton Sans Regular', sans-serif;">Indiana University</p>
        </a>
    </nav>
    <nav class="sb-topnav navbar navbar-expand navbar-dark" id="nav-bar" style="margin-top: 50px;">
        <div class="d-flex align-items-center justify-content-between w-100">
            <div class="d-flex align-items-center">
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
        </div>
    </nav>
</template>


<style scoped>
#top-nav-bar {
    background-color: white;
    padding: 10px;
    margin-bottom: 0; /* Ensure no margin at the bottom */
    color: black;
}


#nav-bar {
    background-color: #990000;
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

.indiana-university-logo{
    width: 36px;
    height: 40px;
    margin-right:6px;
}

.indiana-university-h1{
    text-decoration: none;
    margin-top: 15px;
}

/* CSS for hiding the element gradually */
.hide-on-small-screen {
    opacity: 1;
    transition: opacity 0.0s ease;
}

@media (max-width: 768px) {
    .hide-on-small-screen {
        opacity: 0;
        pointer-events: none; /* Prevents interaction with hidden elements */
    }
}

</style>
<script setup>
</script>