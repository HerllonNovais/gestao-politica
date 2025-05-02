<template>
  <v-app>
    <NavBar v-if="isAuthenticated" />
    <SideMenu v-if="isAuthenticated" />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import { computed } from 'vue'
import { useAuthStore } from '@/store/auth'
import NavBar from '@/components/NavBar.vue'
import SideMenu from '@/components/SideMenu.vue'

const authStore = useAuthStore()
const isAuthenticated = computed(() => authStore.isAuthenticated)
</script>

<style scoped>
.v-main {
  padding: 20px;
}
</style>
