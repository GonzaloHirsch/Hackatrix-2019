<template>
  <v-app class="font-sans">
    <v-toolbar color="primary" max-height="64" class="white--text tw-fixed tw-top-0 tw-w-full tw-z-50">
      <v-toolbar-title class="tw-flex tw-items-center"><img class="tw-w-10 tw-mr-3" src="/img/icon.png" alt="logo MyWorld">MyWorld</v-toolbar-title>

      <div class="flex-grow-1"></div>

      <v-toolbar-items>
        <v-btn class="white--text" active-class="font-weight-bold" to="/" text>Problemas</v-btn>
        <v-btn class="white--text" active-class="font-weight-bold" to="/reciclaje" text>Reciclaje</v-btn>
        <v-btn class="white--text" active-class="font-weight-bold" to="/tips" text>Tips</v-btn>
        <v-btn class="white--text" active-class="font-weight-bold" to="/organizaciones" text>Organizaciones</v-btn>
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

.v-application--wrap {
  font-family: "Poppins", sans-serif !important;
  background-color: white;
}
</style>
