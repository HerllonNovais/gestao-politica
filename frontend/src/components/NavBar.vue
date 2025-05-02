<template>
  <v-app-bar color="primary" dark>
    <v-app-bar-title>Gestão Política</v-app-bar-title>
    <v-spacer></v-spacer>
    <v-btn @click="logout">Sair</v-btn>
  </v-app-bar>
</template>

<script setup>
import { useAuthStore } from '@/store/auth'

const authStore = useAuthStore()

function logout() {
  authStore.handleLogout()
}
</script>
