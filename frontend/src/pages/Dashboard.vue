<template>
  <v-container>
    <h1>Dashboard</h1>
    <iframe
      :src="metabaseUrl"
      width="100%"
      height="800"
      frameborder="0"
    ></iframe>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'

const metabaseUrl = ref('http://metabase:3000/public/dashboard/YOUR_DASHBOARD_ID')
</script>
