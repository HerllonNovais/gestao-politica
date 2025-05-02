import api from './api'

export async function login(email, password) {
  const response = await api.post('/auth/login', { email, password })
  return {
    token: response.data.access_token,
    user: response.data.user
  }
}

export async function logout() {
  await api.post('/auth/logout')
}

export async function getCurrentUser() {
  const response = await api.get('/auth/me')
  return response.data
}
