<template>
  <v-container>
    <v-card>
      <v-card-title>Gerenciar Eleitores</v-card-title>
      <v-card-text>
        <v-btn @click="dialog = true" color="primary">Novo Eleitor</v-btn>
        <v-table>
          <thead>
            <tr>
              <th>Nome</th>
              <th>Telefone</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="eleitor in eleitores" :key="eleitor.id">
              <td>{{ eleitor.nome }}</td>
              <td>{{ eleitor.telefone }}</td>
              <td>
                <v-btn icon @click="editEleitor(eleitor)">
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
        <v-card-title>{{ editing ? 'Editar' : 'Novo' }} Eleitor</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="saveEleitor">
            <v-text-field v-model="form.nome" label="Nome" required />
            <v-text-field v-model="form.telefone" label="Telefone" required />
            <v-text-field v-model="form.email" label="E-mail" />
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

const eleitores = ref([]);
const dialog = ref(false);
const editing = ref(false);
const form = ref({
  nome: "",
  telefone: "",
  email: "",
});

async function loadEleitores() {
  const response = await api.get("/eleitores");
  eleitores.value = response.data;
}

async function saveEleitor() {
  if (editing.value) {
    await api.put(`/eleitores/${form.value.id}`, form.value);
  } else {
    await api.post("/eleitores", form.value);
  }
  dialog.value = false;
  loadEleitores();
}

function editEleitor(eleitor) {
  form.value = { ...eleitor };
  editing.value = true;
  dialog.value = true;
}

onMounted(() => {
  loadEleitores();
});
</script>
