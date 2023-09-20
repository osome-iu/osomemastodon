<template>
    <div id="layoutSidenav_nav">
        <nav class="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
            <div class="sb-sidenav-menu">
                <div class="nav">
                    <div class="collapse" id="collapsePages" aria-labelledby="headingTwo" data-bs-parent="#sidenavAccordion">
                        <nav class="sb-sidenav-menu-nested nav accordion" id="sidenavAccordionPages">
                            <a class="nav-link collapsed" href="#" data-bs-toggle="collapse" data-bs-target="#pagesCollapseAuth" aria-expanded="false" aria-controls="pagesCollapseAuth">
                                Authenticate
                                <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
                            </a>
                            <div class="collapse" id="pagesCollapseAuth" aria-labelledby="headingOne" data-bs-parent="#sidenavAccordionPages">
                                <nav class="sb-sidenav-menu-nested nav">
                                    <router-link class="nav-item nav-link" :to="{name: 'MastodonInstances'}" >
                                        <div class="sb-nav-link-icon"><i class="fas fa-file-alt"></i></div>
                                        Mastodon Instances
                                    </router-link>
                                    <router-link class="nav-item nav-link" :to="{name: 'SingleStatus'}" >
                                        <div class="sb-nav-link-icon"><i class="fas fa-file-alt"></i></div>
                                        Single Status
                                    </router-link>
                                </nav>
                            </div>
                            <a class="nav-link collapsed" href="#" data-bs-toggle="collapse" data-bs-target="#pagesCollapseError" aria-expanded="false" aria-controls="pagesCollapseError">
                                Error
                                <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
                            </a>
                            <div class="collapse" id="pagesCollapseError" aria-labelledby="headingOne" data-bs-parent="#sidenavAccordionPages">
                                <nav class="sb-sidenav-menu-nested nav">
                                    <a class="nav-link" href="401.html">401 Page</a>
                                    <a class="nav-link" href="404.html">404 Page</a>
                                    <a class="nav-link" href="500.html">500 Page</a>
                                </nav>
                            </div>
                        </nav>
                    </div>
                    <div class="sb-sidenav-menu-heading">SEARCH</div>
                    <router-link class="nav-item nav-link" :to="{name: 'MastodonInstances'}" >
                        <div class="sb-nav-link-icon"><i class="fas fa-file-alt"></i></div>
                        Mastodon Instances
                    </router-link>
                    <router-link class="nav-item nav-link" :to="{name: 'SingleStatus'}" >
                        <div class="sb-nav-link-icon"><i class="fas fa-user-shield"></i></div>
                        Single Status
                    </router-link>
                </div>
            </div>
        </nav>
    </div>
</template>
<script setup>
</script>