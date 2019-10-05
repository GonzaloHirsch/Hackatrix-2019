<template>
  <v-container fluid>
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
              description: "Activistas para frenar el CC",
              addresses: [],
              phones: [],
              mails: [],
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
