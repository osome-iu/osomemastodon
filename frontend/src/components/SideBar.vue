<template>
    <div>
    <div id="layoutSidenav">
        <div id="layoutSidenav_nav">
            <nav class="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
                <div class="sb-sidenav-menu">
                    <div class="nav">
                        <div class="sb-sidenav-menu-heading">INSTANCES</div>
                        <router-link class="nav-item nav-link" :to="{name: 'MastodonInstances'}" >
                            <div class="sb-nav-link-icon"><i class="fas fa-list-alt"></i></div>Mastodon Instances
                        </router-link>
                        <div class="sb-sidenav-menu-heading">SEARCH</div>
                        <a class="nav-link collapsed" href="#" data-bs-toggle="collapse" data-bs-target="#collapseLayouts" aria-expanded="false" aria-controls="collapseLayouts">
                            <div class="sb-nav-link-icon"><i class="fas fa-columns"></i></div>
                            Get Statuses
                            <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
                        </a>
                        <div class="collapse" id="collapseLayouts" aria-labelledby="headingOne" data-bs-parent="#sidenavAccordion">
                            <nav class="sb-sidenav-menu-nested nav">
                                <router-link class="nav-item nav-link" :to="{name: 'SearchByKeyword'}" >
                                    <div class="sb-nav-link-icon"><i class="fas fa-file-alt"></i></div>Search by keyword
                                </router-link>
                                <router-link class="nav-item nav-link" :to="{name: 'TimelineHashtag'}" >
                                    <div class="sb-nav-link-icon"><i class="fa-solid fa-hashtag"></i></div>Most recent by hashtag
                                </router-link>
                                <router-link class="nav-item nav-link" :to="{name: 'TimelineStatus'}" >
                                    <div class="sb-nav-link-icon"><i class="fa-solid fa-user"></i></div>
                                    Most recent for instance
                                </router-link>
                                <router-link class="nav-item nav-link" :to="{name: 'SearchByIdStatus'}" >
                                    <div class="sb-nav-link-icon"><i class="fa-solid fa-id-card"></i></div>
                                    Single Status by ID
                                </router-link>
                            </nav>
                        </div>
                        <a class="nav-link collapsed" href="#" data-bs-toggle="collapse" data-bs-target="#collapsePages" aria-expanded="false" aria-controls="collapsePages">
                            <div class="sb-nav-link-icon"><i class="fas fa-book-open"></i></div>
                            Get Accounts
                            <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
                        </a>
                        <div class="collapse" id="collapsePages" aria-labelledby="headingTwo" data-bs-parent="#sidenavAccordion">
                            <nav class="sb-sidenav-menu-nested nav accordion" id="sidenavAccordionPages">
                                <router-link class="nav-item nav-link" :to="{name: 'SearchAccounts'}" >
                                    <div class="sb-nav-link-icon"><i class="fas fa-file-alt"></i></div>Search by keyword
                                </router-link>
                                <router-link class="nav-item nav-link" :to="{name: 'AccountsById'}" >
                                    <div class="sb-nav-link-icon"><i class="fa-solid fa-hashtag"></i></div>Single Account by ID
                                </router-link>
                            </nav>
                        </div>
                        <router-link class="nav-item nav-link" :to="{name: 'SearchHashtags'}" >
                            <div class="sb-nav-link-icon"><i class="fa fa-question-circle"></i></div>
                            Get Hashtag metadata
                        </router-link>
                        <div class="sb-sidenav-menu-heading">DOCUMENTATION</div>
                        <router-link class="nav-item nav-link" :to="{name: 'FAQ'}" >
                            <div class="sb-nav-link-icon"><i class="fa fa-question-circle"></i></div>
                            FAQ
                        </router-link>
                    </div>
                </div>
            </nav>
        </div>
    </div>
    </div>
</template>
<script setup>
</script>