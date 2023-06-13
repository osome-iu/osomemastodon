import { createWebHistory, createRouter } from "vue-router";
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
    }
];

const router = createRouter({
    history: createWebHistory('/tools/mastodon/'),
    routes: routes,
});

export default router;