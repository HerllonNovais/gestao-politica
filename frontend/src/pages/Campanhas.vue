<template>
  <v-container>
    <v-card>
      <v-card-title>Campanhas de WhatsApp</v-card-title>
      <v-card-text>
        <v-btn @click="dialog = true" color="primary">Nova Campanha</v-btn>
        <v-table>
          <thead>
            <tr>
              <th>Nome</th>
              <th>Data de Disparo</th>
              <th>Status</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="campanha in campanhas" :key="campanha.id">
              <td>{{ campanha.nome }}</td>
              <td>{{ new Date(campanha.data_disparo).toLocaleString() }}</td>
              <td>{{ campanha.status }}</td>
              <td>
                <v-btn icon @click="editCampanha(campanha)">
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </td>
            </tr>
          </tbody>
        </v-table>
      </v-card-text>
    </v-card>

    <!-- Modal de Cadastro -->
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title>{{ editing ? 'Editar' : 'Nova' }} Campanha</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="saveCampanha">
            <v-text-field v-model="form.nome" label="Nome" required />
            <v-textarea v-model="form.mensagem" label="Mensagem" required />
            <v-date-picker v-model="form.data_disparo" label="Data de Disparo" />
            <v-btn type="submit" color="primary">Salvar</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "@/services/api";

const campanhas = ref([]);
const dialog = ref(false);
const editing = ref(false);
const form = ref({
  nome: "",
  mensagem: "",
  data_disparo: new Date().toISOString().split("T")[0],
});

async function loadCampanhas() {
  const response = await api.get("/campanhas");
  campanhas.value = response.data;
}

async function saveCampanha() {
  if (editing.value) {
    await api.put(`/campanhas/${form.value.id}`, form.value);
  } else {
    await api.post("/campanhas", form.value);
  }
  dialog.value = false;
  loadCampanhas();
}

function editCampanha(campanha) {
  form.value = { ...campanha };
  editing.value = true;
  dialog.value = true;
}

onMounted(() => {
  loadCampanhas();
});
</script>
