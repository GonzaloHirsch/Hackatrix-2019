<template>
  <v-container fluid>
    <v-row>
      <v-col cols="auto">
        <div class="pl-6 display-1">
          Organizaciones
        </div>
      </v-col>
    </v-row>
    <v-expansion-panels popout>
      <Organization
        v-for="item of items"
        :key="item.name"
        :item="item"
      ></Organization>
    </v-expansion-panels>
  </v-container>
</template>

<script>
  import Organization from "../components/Organization";

  export default {
    name: "organizaciones.vue",
    components: { Organization },
    data() {
      return {
        items: []
      };
    },
    mounted() {
      this.loadOrganizations();
    },
    methods: {
      loadOrganizations() {
        // setTimeout(() => {
          this.items = [
            {
              title: "Greenpeace",
              description: "ONG para defender el medioambiente",
              map_img: "img/organizations/greenpeace_map.png",
              addresses: ["Zabala 3873, CABA"],
              phones: ["01143128432"],
              emails: ["contacto@greenpeace.org.ar"],
              img: ""
            }
          ]
        // }, 1000);
      }
    }
  }
</script>

<style scoped>

</style>
