import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/pages/Login.vue'
import Dashboard from '@/pages/Dashboard.vue'
import Eleitores from '@/pages/Eleitores.vue'
import Campanhas from '@/pages/Campanhas.vue'
import WhatsApp from '@/pages/WhatsApp.vue'

const routes = [
  { path: '/login', name: 'Login', component: Login },
  { path: '/', name: 'Dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/eleitores', name: 'Eleitores', component: Eleitores, meta: { requiresAuth: true } },
  { path: '/campanhas', name: 'Campanhas', component: Campanhas, meta: { requiresAuth: true } },
  { path: '/whatsapp', name: 'WhatsApp', component: WhatsApp, meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
