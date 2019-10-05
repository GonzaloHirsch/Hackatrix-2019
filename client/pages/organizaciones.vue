<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col md="6" lg="8">
        <div class="pl-6 display-1">
          Organizaciones
        </div>
      </v-col>
    </v-row>

    <v-row justify="center" dense class="pb-8 pl-6 pr-6 mb-n8">
      <v-col md="6" lg="8">
        <v-text-field
          hide-details
          prepend-icon="search"
          single-line
          class="ml-3"
          placeholder="Start typing to Search"
          v-model="search"
          clearable
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col md="6" lg="8">
    <v-expansion-panels popout>
      <Organization
        v-for="item of filteredItems"
        :key="item.title"
        :item="item"
      ></Organization>
    </v-expansion-panels>
    </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import Organization from "../components/Organization";

  export default {
    name: "organizaciones.vue",
    components: { Organization },
    data() {
      return {
        items: [],
        search: ""
      };
    },
    mounted() {
      this.loadOrganizations();
    },
    computed: {
      filteredItems() {
        if (this.search == null || this.search == "") return this.items;
        let search = this.search.trim().toUpperCase();
        return this.items.filter(v => v.title.toUpperCase().match(search));
      }
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
