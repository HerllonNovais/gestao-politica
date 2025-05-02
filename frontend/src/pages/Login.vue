<template>
  <v-container class="fill-height">
    <v-card width="400" class="mx-auto">
      <v-card-title class="text-center">Login</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="submit">
          <v-text-field v-model="email" label="E-mail" required />
          <v-text-field v-model="password" label="Senha" type="password" required />
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
