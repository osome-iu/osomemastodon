import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/instances',
    name: 'MastodonInstances',
    component: () => import(/* webpackChunkName: "about" */ '../components/InstanceData.vue')
  },
  {
    path: '/searchbyid',
    name: 'SearchByIdStatus',
    component: () => import(/* webpackChunkName: "about" */ '../components/SearchByIdStatus.vue')
  },
  {
    path: '/searchbykeyword',
    name: 'SearchByKeyword',
    component: () => import(/* webpackChunkName: "about" */ '../components/SearchByKeyword.vue')
  },
  {
    path: '/streamer',
    name: 'Streamer',
    component: () => import(/* webpackChunkName: "about" */ '../components/Streamer.vue')
  },
  {
    path: '/accounts',
    name: 'Accounts',
    component: () => import(/* webpackChunkName: "about" */ '../components/Accounts.vue')
  }
]

const router = createRouter({
  history: createWebHistory('/tools/mastodon/instances'),
  routes: routes,
});

export default router
