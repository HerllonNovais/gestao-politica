<template>
  <v-card>
    <v-card-title>Conectar WhatsApp</v-card-title>
    <v-card-text>
      <div v-if="qrCode">
        <p>Escaneie o QR Code abaixo:</p>
        <img :src="qrCode" alt="QR Code WhatsApp" />
      </div>
      <v-btn @click="fetchQRCode" color="green" :loading="loading">
        Gerar QR Code
      </v-btn>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref } from "vue";
import api from "@/services/api";

const qrCode = ref("");
const loading = ref(false);

async function fetchQRCode() {
  loading.value = true;
  try {
    const response = await api.get("/whatsapp/qr-code");
    qrCode.value = response.data.qr_code;
  } catch (error) {
    alert("Erro ao gerar QR Code: " + error.message);
  } finally {
    loading.value = false;
  }
}
</script>
