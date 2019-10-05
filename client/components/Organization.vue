<template>
  <v-expansion-panel>
    <v-expansion-panel-header v-slot="{ open }">
      <v-row align="center" justify="space-around">
        <v-col cols="auto">
          <v-fade-transition leave-absolute>
            <div v-if="!open" class="title">
              {{ item.title }}
            </div>

            <h2 v-else class="text-no-bold">
                {{ item.title }}
            </h2>
          </v-fade-transition>
        </v-col>

        <v-col cols="auto" class="text--secondary">
          <v-fade-transition>
            <span v-if="!open">
              {{ item.description }}
            </span>
          </v-fade-transition>
        </v-col>
      </v-row>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-container v-if="!open" fluid dense>
        <v-divider></v-divider>
        <v-row>
          <v-col cols="auto" class="title">
            {{ item.description }}
          </v-col>
        </v-row>
        <v-row class="pt-2" v-if="item.phones.length > 0">
          <v-col cols="auto">
            Telefono{{ item.phones.length === 1 ? "" : "s" }}:
          </v-col>
        </v-row>
        <ul>
          <li v-for="phone in item.phones">- {{phone}}</li>
        </ul>

        <v-row class="pt-2" v-if="item.emails.length > 0">
          <v-col cols="auto">
            Email{{ item.emails.length === 1 ? "" : "s" }}:
          </v-col>
        </v-row>
        <ul>
          <li v-for="email in item.emails">
            - <a :href="'mailto:' + email">
              {{email}}
            </a>
          </li>
        </ul>

        <v-row class="pt-2" v-if="item.addresses.length > 0">
          <v-col cols="auto">
            Direccion{{ item.addresses.length === 1 ? "" : "es" }}:
          </v-col>
        </v-row>
        <ul>
          <li v-for="address in item.addresses">- {{address}}</li>
        </ul>

        <v-row class="pt-2">
          <v-col>
            <v-img
              max-height="300"
              :src="item.map_img">
            </v-img>
          </v-col>
        </v-row>
      </v-container>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
  export default {
    title: "Organization",
    props: {
      item: {
        type: Object,
        required: true
      }
    }
  }
</script>

<style scoped>

</style>
