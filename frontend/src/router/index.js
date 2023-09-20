import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/instances',
    name: 'MastodonInstances',
    component: () => import(/* webpackChunkName: "about" */ '../components/InstanceData.vue')
  },
  {
    path: '/',
    name: 'SingleStatus',
    component: () => import(/* webpackChunkName: "about" */ '../components/SingleStatus.vue')
  }
]

const router = createRouter({
  history: createWebHistory('/tools/mastodon/instances'),
  routes: routes,
});

export default router
