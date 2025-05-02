<template>
  <v-navigation-drawer permanent>
    <v-list>
      <v-list-item
        v-for="item in menuItems"
        :key="item.title"
        :to="item.route"
        active-color="primary"
      >
        <template v-slot:prepend>
          <v-icon :icon="item.icon"></v-icon>
        </template>
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup>
const menuItems = [
  { title: "Dashboard", icon: "mdi-view-dashboard", route: "/" },
  { title: "Eleitores", icon: "mdi-account-group", route: "/eleitores" },
  { title: "Campanhas", icon: "mdi-calendar-send", route: "/campanhas" },
  { title: "WhatsApp", icon: "mdi-whatsapp", route: "/whatsapp" },
];
</script>
