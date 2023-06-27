import { createWebHistory, createRouter } from "vue-router";
import AboutPage  from "@/views/AboutPage.vue";
import DocumentationPage from "@/views/DocumentationPage.vue";
import HomePage from '../views/HomePage'

const routes = [
    {
        path: "/",
        name: "Home",
        component: HomePage,
    },
    {
        path: "/about",
        name: "About",
        component: AboutPage,
    },
    {
        path: "/documentation",
        name: "Documentation",
        component: DocumentationPage,
    }
];

const router = createRouter({
    history: createWebHistory('/tools/mastodon/'),
    routes: routes,
});

export default router;