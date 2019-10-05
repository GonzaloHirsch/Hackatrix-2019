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

    <NoItemsFoundComponent v-if="filteredItems.length === 0"></NoItemsFoundComponent>

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
  import NoItemsFoundComponent from "../components/NoItemsFoundComponent";
  import Organization from "../components/Organization";

  export default {
    name: "organizaciones.vue",
    components: { NoItemsFoundComponent, Organization },
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
      async loadOrganizations() {
        let items = await this.$axios.$get("/orgs");
        if (items != null) this.items = items;
      }
    }
  }
</script>

<style scoped>

</style>
