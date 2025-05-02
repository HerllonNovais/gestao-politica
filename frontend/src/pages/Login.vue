<template>
  <v-container class="fill-height login-container">
    <v-card width="400" class="mx-auto login-card">
      <v-img src="@/assets/images/logo.svg" height="80" contain />
      <v-card-title class="text-center">Acessar Sistema</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="submit">
          <v-text-field
            v-model="email"
            label="E-mail"
            prepend-icon="mdi-email"
            required
          />
          <v-text-field
            v-model="password"
            label="Senha"
            type="password"
            prepend-icon="mdi-lock"
            required
          />
          <v-btn type="submit" color="primary" block>Entrar</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/store/auth'

const email = ref('')
const password = ref('')
const authStore = useAuthStore()

async function submit() {
  try {
    await authStore.handleLogin(email.value, password.value)
  } catch (error) {
    alert('Erro no login: ' + error.message)
  }
}
</script>

<style scoped lang="scss">
@import '@/assets/styles/variables';

.login-container {
  background: url('@/assets/images/bg-auth.jpg') no-repeat center center;
  background-size: cover;
}

.login-card {
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  background: rgba(255, 255, 255, 0.9);
}
</style>
