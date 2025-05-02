import { defineStore } from 'pinia'
import { ref } from 'vue'
import router from '@/router'
import { login, logout } from '@/services/auth'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token'))
  const user = ref(JSON.parse(localStorage.getItem('user')))

  const isAuthenticated = computed(() => !!token.value)

  async function handleLogin(email, password) {
    try {
      const response = await login(email, password)
      token.value = response.token
      user.value = response.user
      localStorage.setItem('token', token.value)
      localStorage.setItem('user', JSON.stringify(user.value))
      router.push('/')
    } catch (error) {
      throw error
    }
  }

  async function handleLogout() {
    await logout()
    token.value = null
    user.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    router.push('/login')
  }

  return { token, user, isAuthenticated, handleLogin, handleLogout }
})
