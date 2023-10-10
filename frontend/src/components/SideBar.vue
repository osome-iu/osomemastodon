<template>
    <div id="layoutSidenav_nav" class="fixed">
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
                                    <router-link class="nav-item nav-link" :to="{name: 'SearchByIdStatus'}" >
                                        <div class="sb-nav-link-icon"><i class="fas fa-file-alt"></i></div>
                                        Status
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
                    <a class="nav-link collapsed" href="#" data-bs-toggle="collapse" data-bs-target="#collapseLayouts" aria-expanded="false" aria-controls="collapseLayouts">
                        <div class="sb-nav-link-icon"><i class="fas fa-columns"></i></div>
                        Search
                        <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
                    </a>
                    <div class="collapse" id="collapseLayouts" aria-labelledby="headingOne" data-bs-parent="#sidenavAccordion">
                        <nav class="sb-sidenav-menu-nested nav">
                            <router-link class="nav-item nav-link" :to="{name: 'SearchByKeyword'}" >
                                <div class="sb-nav-link-icon"><i class="fas fa-file-alt"></i></div>
                                Search by keyword
                            </router-link>
                            <router-link class="nav-item nav-link" :to="{name: 'SearchByIdStatus'}" >
                                <div class="sb-nav-link-icon"><i class="fas fa-user-shield"></i></div>
                                Search by status Id
                            </router-link>
                        </nav>
                    </div>
                    <router-link class="nav-item nav-link" :to="{name: 'HashtagSearch'}" >
                        <div class="sb-nav-link-icon"><i class="fa-solid fa-hashtag"></i></div>
                        Hashtag
                    </router-link>
                    <router-link class="nav-item nav-link" :to="{name: 'Accounts'}" >
                        <div class="sb-nav-link-icon"><i class="fa-solid fa-user"></i></div>
                        Accounts
                    </router-link>
                </div>
            </div>
        </nav>
    </div>
</template>
<script setup>
</script>