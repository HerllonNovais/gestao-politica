<template>
  <v-container>
    <WhatsAppQR />
    <v-card class="mt-4">
      <v-card-title>Disparo Manual</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="sendMessage">
          <v-text-field v-model="telefone" label="Telefone (DDD+Número)" />
          <v-textarea v-model="mensagem" label="Mensagem" />
          <v-btn type="submit" color="green">Enviar Mensagem</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import api from "@/services/api";
import WhatsAppQR from "@/components/WhatsAppQR.vue";

const telefone = ref("");
const mensagem = ref("");

async function sendMessage() {
  try {
    await api.post("/whatsapp/enviar-mensagem", {
      telefone: telefone.value,
      mensagem: mensagem.value,
    });
    alert("Mensagem enviada com sucesso!");
  } catch (error) {
    alert("Erro ao enviar mensagem: " + error.message);
  }
}
</script>
