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
    component: () => import(/* webpackChunkName: "about" */ '../components/SingleStatusById.vue')
  },
  {
    path: '/searchbykeyword',
    name: 'SearchByKeyword',
    component: () => import(/* webpackChunkName: "about" */ '../components/SearchStatuses.vue')
  },
  {
    path: '/accountsbyId',
    name: 'singleAccountById',
    component: () => import(/* webpackChunkName: "about" */ '../components/SingleAccountById.vue')
  },
  {
    path: '/timelinehashtag',
    name: 'TimelineHashtag',
    component: () => import(/* webpackChunkName: "about" */ '../components/TimelineHashtag.vue')
  },
  {
    path: '/timelinestatus',
    name: 'TimelineStatus',
    component: () => import(/* webpackChunkName: "about" */ '../components/TimelineStatuses.vue')
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: () => import(/* webpackChunkName: "about" */ '../components/faq.vue')
  },
  {
    path: '/apidocumentation',
    name: 'APIdoc',
    component: () => import(/* webpackChunkName: "about" */ '../components/APIdocumentation.vue')
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
