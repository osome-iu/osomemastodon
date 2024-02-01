<template>
        <div id="sidebarcontent" class="scrollable-sidebar">
            <div id="layoutSidenav_nav">
                <nav class="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
                    <div class="sb-sidenav-menu">
                        <div class="nav">
                            <router-link class="nav-item nav-link" :to="{name: 'LandingView'}"  exact-active-class="active-link">
                                <div class="sb-nav-link-icon"><i class="fa fa-home"></i></div>
                                OSoMe Mastodon
                            </router-link>

                            <div class="sb-sidenav-menu-heading">SEARCH</div>
                            <a class="nav-link collapsed" href="#" @click="toggleCollapse_one" aria-expanded="false" aria-controls="collapsePages1">
                                <div class="sb-nav-link-icon"><i class="fas fa-book-open"></i></div>
                                Get statuses
                                <div :class="arrowIconClassesOne" :click="toggleCollapse_one">
                                    <i class="fas fa-angle-down" :click="toggleCollapse_one"></i>
                                </div>
                            </a>
                            <div :class="{ 'collapse': true, 'show': isCollapsedOne }" id="collapseLayouts" aria-labelledby="headingOne" data-bs-parent="#sidenavAccordion">
                                <nav class="sb-sidenav-menu-nested nav accordion" id="sidenavAccordionLayouts">
                                    <router-link class="nav-item nav-link" :to="{name: 'SearchByKeyword'}" exact-active-class="active-link" >
                                        <div class="sb-nav-link-icon"><i class="fa fa-search"></i></div>Search by keyword
                                    </router-link>
                                    <router-link class="nav-item nav-link" :to="{name: 'TimelineHashtag'}"  exact-active-class="active-link">
                                        <div class="sb-nav-link-icon"><i class="fa fa-refresh"></i></div>Search by hashtag
                                    </router-link>
                                    <router-link class="nav-item nav-link" :to="{name: 'TimelineStatus'}" exact-active-class="active-link" >
                                        <div class="sb-nav-link-icon"><i class="fa fa-list-alt"></i></div>Recent for instance
                                    </router-link>
                                    <router-link class="nav-item nav-link" :to="{name: 'SearchByIdStatus'}" exact-active-class="active-link" >
                                        <div class="sb-nav-link-icon"><i class="fa fa-clipboard-check"></i></div>Single status by id
                                    </router-link>
                                </nav>
                            </div>

                            <a class="nav-link collapsed" href="#" @click="toggleCollapse_two" aria-expanded="false" aria-controls="collapsePages2">
                                <div class="sb-nav-link-icon"><i class="fas fa-users"></i></div>
                                Get accounts
                                <div :class="arrowIconClassesTwo" :click="toggleCollapse_two">
                                    <i class="fas fa-angle-down" :click="toggleCollapse_two"></i>
                                </div>
                            </a>

                            <div :class="{ 'collapse': true, 'show': isCollapsedTwo }" id="collapsePages" aria-labelledby="headingTwo" data-bs-parent="#sidenavAccordion">
                                <nav class="sb-sidenav-menu-nested nav accordion" id="sidenavAccordionPages">
                                    <!-- Your nested navigation links -->
                                    <router-link class="nav-item nav-link" :to="{name: 'SearchAccounts'}"  exact-active-class="active-link">
                                        <div class="sb-nav-link-icon"><i class="fa fa-search-plus"></i></div>Search by keyword
                                    </router-link>
                                    <router-link class="nav-item nav-link" :to="{name: 'singleAccountById'}" exact-active-class="active-link">
                                        <div class="sb-nav-link-icon"><i class="fa fa-user-circle"></i></div>Single account by id
                                    </router-link>
                                </nav>
                            </div>

                            <router-link class="nav-item nav-link" :to="{name: 'SearchHashtags'}"  exact-active-class="active-link">
                                <div class="sb-nav-link-icon"><i class="fa fa-tags"></i></div>
                                Get hashtag metadata
                            </router-link>

                            <div class="sb-sidenav-menu-heading">INSTANCES</div>
                            <router-link class="nav-item nav-link" :to="{name: 'MastodonInstances'}" exact-active-class="active-link" >
                                <div class="sb-nav-link-icon"><i class="fas fa-list-alt"></i></div>Mastodon Instances
                            </router-link>

                            <div class="sb-sidenav-menu-heading">DOCUMENTATION</div>
                            <router-link class="nav-item nav-link" :to="{name: 'FAQ'}"  exact-active-class="active-link">
                                <div class="sb-nav-link-icon"><i class="fa fa-life-ring"></i></div>
                                FAQ
                            </router-link>
                            <router-link class="nav-item nav-link" :to="{name: 'APIdoc'}"  exact-active-class="active-link">
                                <div class="sb-nav-link-icon"><i class="fa fa-link"></i></div>
                                API documentation
                            </router-link>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
</template>

<script>
import { ref } from 'vue';

export default {
    data() {
        return {
            isCollapsedOne: false,
            isCollapsedTwo: false,
            is_expanded: ref(localStorage.getItem('is_expanded') === 'true'),
        };
    },
    methods: {
        toggleCollapse_one() {
            this.isCollapsedOne = !this.isCollapsedOne;
        },
        toggleCollapse_two(){
            this.isCollapsedTwo = !this.isCollapsedTwo;
        }
    },
    computed: {
        arrowIconClassesOne() {
            return [!this.isCollapsedOne ? 'sb-sidenav-collapse-arrow' : 'sb-sidenav-collapse-below'];
        },
        arrowIconClassesTwo() {
            return [!this.isCollapsedTwo ? 'sb-sidenav-collapse-arrow' : 'sb-sidenav-collapse-below'];
        },
    },
};
</script>


<style scoped>

.scrollable-sidebar {
    max-height: 100vh; /* Set maximum height as the viewport height */
    overflow-y: auto; /* Enable vertical scrolling */
}

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
