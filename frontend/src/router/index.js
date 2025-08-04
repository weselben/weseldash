import { createRouter, createWebHistory } from 'vue-router'

// Import views
import Dashboard from '../views/Dashboard.vue'
import AiChat from '../views/AiChat.vue'
import Knowledge from '../views/Knowledge.vue'
import Analytics from '../views/Analytics.vue'
import System from '../views/System.vue'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      title: 'Dashboard - Personal Hub'
    }
  },
  {
    path: '/ai-chat',
    name: 'AiChat',
    component: AiChat,
    meta: {
      title: 'AI Chat - Personal Assistant'
    }
  },
  {
    path: '/knowledge',
    name: 'Knowledge',
    component: Knowledge,
    meta: {
      title: 'Knowledge Management'
    }
  },
  {
    path: '/analytics',
    name: 'Analytics',
    component: Analytics,
    meta: {
      title: 'Personal Analytics'
    }
  },
  {
    path: '/system',
    name: 'System',
    component: System,
    meta: {
      title: 'System Management'
    }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue'),
    meta: {
      title: 'Page Not Found'
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Navigation guard to update page title
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Personal Dashboard'
  next()
})

export default router