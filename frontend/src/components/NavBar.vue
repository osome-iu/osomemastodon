<template>
    <nav class="sb-topnav navbar navbar-expand navbar-dark" id="nav-bar">
        <div class="d-flex align-items-center m-0">
            <a href="https://osome.iu.edu/" target="_blank" class="navigation-link"><h1 class="navbar-brand mb-0" style="letter-spacing: -1px; font-size: 1.5rem; font-weight: bold; margin-right: -130px;">OSoMe</h1></a>
            <img src="../assets/mastodon_png.png" alt="OSoMe Logo" style="width: 120px; margin-right: 20px; margin-top: 8px;">
            <h1 class="navbar-brand mb-0" style="letter-spacing: -1px; font-size: 1.5rem; margin-left: -5px; font-weight: bold;">Search</h1>
        </div>
        <button class="btn btn-link btn-sm order-1 order-lg-0 me-4 me-lg-0" id="sidebarToggle" href="#!" style="margin-top:4px;margin-left: -130px;" aria-label="navigate-button"><i class="fas fa-bars"></i></button>
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

/* Add additional styles as needed */
</style>
<script setup>
</script>