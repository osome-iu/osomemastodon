<template>
    <div>
        <div id="layoutSidenav">
            <div id="layoutSidenav_nav">
                <nav class="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
                    <div class="sb-sidenav-menu">
                        <div class="nav">
                            <div class="sb-sidenav-menu-heading">INSTANCES</div>
                            <router-link class="nav-item nav-link" :to="{name: 'MastodonInstances'}" exact-active-class="active-link" >
                                <div class="sb-nav-link-icon"><i class="fas fa-list-alt"></i></div>Mastodon Instances
                            </router-link>
                            <div class="sb-sidenav-menu-heading">SEARCH</div>
                            <a class="nav-link collapsed" href="#" data-bs-toggle="collapse" data-bs-target="#collapseLayouts" aria-expanded="false" aria-controls="collapseLayouts" >
                                <div class="sb-nav-link-icon"><i class="fas fa-columns"></i></div>
                                Get Statuses
                                <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
                            </a>
                            <div class="collapse" id="collapseLayouts" aria-labelledby="headingOne" data-bs-parent="#sidenavAccordion">
                                <nav class="sb-sidenav-menu-nested nav">
                                    <router-link class="nav-item nav-link" :to="{name: 'SearchByKeyword'}"  exact-active-class="active-link" >
                                        <div class="sb-nav-link-icon"><i class="fa fa-search"></i></div>Search by keyword
                                    </router-link>
                                    <router-link class="nav-item nav-link" :to="{name: 'TimelineHashtag'}"  exact-active-class="active-link">
                                        <div class="sb-nav-link-icon"><i class="fa fa-refresh"></i></div>Most recent by hashtag
                                    </router-link>
                                    <router-link class="nav-item nav-link" :to="{name: 'TimelineStatus'}" exact-active-class="active-link" >
                                        <div class="sb-nav-link-icon"><i class="fa fa-list-alt"></i></div>
                                        Most recent for instance
                                    </router-link>
                                    <router-link class="nav-item nav-link" :to="{name: 'SearchByIdStatus'}" exact-active-class="active-link" >
                                        <div class="sb-nav-link-icon"><i class="fa fa-clipboard-check"></i></div>
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
                                    <router-link class="nav-item nav-link" :to="{name: 'SearchAccounts'}"  exact-active-class="active-link">
                                        <div class="sb-nav-link-icon"><i class="fa fa-search-plus"></i></div>Search by keyword
                                    </router-link>
                                    <router-link class="nav-item nav-link" :to="{name: 'singleAccountById'}" exact-active-class="active-link" >
                                        <div class="sb-nav-link-icon"><i class="fa fa-user-circle"></i></div>Single Account by ID
                                    </router-link>
                                </nav>
                            </div>
                            <router-link class="nav-item nav-link" :to="{name: 'SearchHashtags'}"  exact-active-class="active-link">
                                <div class="sb-nav-link-icon"><i class="fa fa-tags"></i></div>
                                Get Hashtag metadata
                            </router-link>
                            <div class="sb-sidenav-menu-heading">DOCUMENTATION</div>
                            <router-link class="nav-item nav-link" :to="{name: 'FAQ'}"  exact-active-class="active-link">
                                <div class="sb-nav-link-icon"><i class="fa fa-life-ring"></i></div>
                                FAQ
                            </router-link>
                            <router-link class="nav-item nav-link" :to="{name: 'APIdoc'}"  exact-active-class="active-link">
                                <div class="sb-nav-link-icon"><i class="fa fa-link"></i></div>
                                API Doc
                            </router-link>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    data() {
        return {
            is_expanded: ref(localStorage.getItem('is_expanded') === 'true'),
        };
    },
    methods: {
    },
};
</script>


<style scoped>

.active-link {
    border-right: 8px solid #0096FF;
    color:#0073cf;
    .sb-nav-link-icon{
        color: #0073cf;
    }
    background: linear-gradient(to right, #151C62, #0073cf);
}

.active-link:hover {
    border-right: 8px solid #0096FF;
    color:#0073cf;
    .sb-nav-link-icon{
        color: #0073cf;
    }
    .nav{
        color: #0073cf;
    }
    background: linear-gradient(to right, #151C62, #0073cf);
}

</style>
