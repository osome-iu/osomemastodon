import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
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
    component: () => import(/* webpackChunkName: "about" */ '../components/SearchStatuses.vue')
  },
  {
    path: '/accountsbyId',
    name: 'AccountsById',
    component: () => import(/* webpackChunkName: "about" */ '../components/AccountById.vue')
  },
  {
    path: '/timelinehashtag',
    name: 'TimelineHashtag',
    component: () => import(/* webpackChunkName: "about" */ '../components/TimelineHashtag.vue')
  },
  {
    path: '/timelinestatus',
    name: 'TimelineStatus',
    component: () => import(/* webpackChunkName: "about" */ '../components/TimelineStatus.vue')
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: () => import(/* webpackChunkName: "about" */ '../components/faq.vue')
  },
  {
    path: '/searchaccounts',
    name: 'SearchAccounts',
    component: () => import(/* webpackChunkName: "about" */ '../components/SearchAccounts.vue')
  },
  {
    path: '/searchhashtags',
    name: 'SearchHashtags',
    component: () => import(/* webpackChunkName: "about" */ '../components/SearchHashtag.vue')
  },
]

const router = createRouter({
  history: createWebHistory('/tools/mastodon'),
  routes: routes,
});

export default router
