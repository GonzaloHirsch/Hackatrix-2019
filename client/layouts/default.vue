<template>
  <v-app>
    <v-toolbar fixed max-height="64">
      <v-toolbar-title>MyWorld</v-toolbar-title>

      <div class="flex-grow-1"></div>

      <v-toolbar-items>
        <v-btn to="/problemas" text>Problemas</v-btn>
        <v-btn to="/reciclaje" text>Reciclaje</v-btn>
        <v-btn to="/tips" text>Tips</v-btn>
        <v-btn to="/organizaciones" text>Organizaciones</v-btn>
      </v-toolbar-items>
      <!-- <template v-if="$vuetify.breakpoint.smAndUp">
        <v-btn icon>
          <v-icon>mdi-export-variant</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-delete-circle</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-plus-circle</v-icon>
        </v-btn>
      </template> -->
    </v-toolbar>

    <nuxt />
  </v-app>
</template>
