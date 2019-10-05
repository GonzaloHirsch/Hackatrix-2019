<template>
  <v-app>
    <v-toolbar max-height="64" class="tw-fixed tw-top-0 tw-w-full tw-z-50">
      <v-toolbar-title>MyWorld</v-toolbar-title>

      <div class="flex-grow-1"></div>

      <v-toolbar-items>
        <v-btn exact-active-class="tw-text-primary" to="/problemas" text>Problemas</v-btn>
        <v-btn exact-active-class="tw-text-primary" to="/reciclaje" text>Reciclaje</v-btn>
        <v-btn exact-active-class="tw-text-primary" to="/tips" text>Tips</v-btn>
        <v-btn exact-active-class="tw-text-primary" to="/organizaciones" text>Organizaciones</v-btn>
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

<style>
body {
  padding-top: 64px;
  padding-bottom: 200px;
}
</style>