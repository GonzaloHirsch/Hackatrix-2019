<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col md="6" lg="8">
        <div class="pl-6 display-1">
          Tips
        </div>
      </v-col>
    </v-row>

    <v-row justify="center" dense class="pb-8 pl-6 pr-6 mb-n8">
      <v-col md="6" lg="8">
        <v-select
          chips
          label="Tipo de Tip"
          multiple
          solo
          :items="filterChips"
          clearable
          deletable-chips
          @change="chipFilterAdded"
          menu-props="offsetY"
        >
        </v-select>
      </v-col>
    </v-row>

    <div v-for="item in items" class="pb-8" :hidden="item.hidden">
      <v-row justify="center">
        <v-col md="6" lg="8">
          <div class="pl-6 headline">{{ item.type }}</div>
        </v-col>
      </v-row>

      <v-row justify="center">
        <v-col md="6" lg="8">
          <v-expansion-panels popout>
            <Tip
              v-for="tip in item.tips"
              :key="tip.title"
              :title="tip.title"
              :items="tip.items"
            ></Tip>
          </v-expansion-panels>
         </v-col>
       </v-row>
    </div>

  </v-container>
</template>

<script>
  import Tip from "../components/Tip";

  export default {
    name: "tip.vue",
    components: { Tip },
    data() {
      return {
        items: [],
        filterChips: []
      };
    },
    async mounted() {
      await this.loadTips();
      this.filterChips = [];
      for (let item of this.items) {
        this.filterChips.push({
          text: item.type,
          value: item.type
        })
      }
    },
    methods: {
      async loadTips() {
        try {
          let items = (await this.$axios.$get("/tips"));
          if (items != null) this.items = items;
        } catch (e) {
          console.error(e);
        }
      },
      chipFilterAdded(chips) {
        if (chips.length === 0) {
          for (let item of this.items) {
            if (item.hidden) item.hidden = false;
          }
        } else {
          for (let item of this.items) {
            let index = chips.indexOf(item.type);
            if (index !== -1) {
              if (item.hidden) item.hidden = false;
            } else {
              if (!item.hidden) item.hidden = true;
            }
          }
        }
      }
    }
  }
</script>

<style scoped>

</style>
