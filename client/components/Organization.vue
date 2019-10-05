<template>
  <v-expansion-panel>
    <v-expansion-panel-header v-slot="{ open }">
      <v-row>
        <v-col cols="6">
          <v-fade-transition leave-absolute>
            <h3 v-if="!open" class="text-no-bold">
              {{ item.name }}
            </h3>

            <h2 v-else class="text-no-bold">
              Click para mas informacion
            </h2>
          </v-fade-transition>
        </v-col>

        <v-col cols="auto" class="text--secondary">
          <v-fade-transition leave-absolute>
            <span v-if="!open">
              {{ item.description }}
            </span>
          </v-fade-transition>
        </v-col>
      </v-row>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-row>
        <v-col cols="6">
          <v-fade-transition leave-absolute>
            <h3 v-if="!open" class="text-no-bold">
              {{ item.name }}
            </h3>

            <h2 v-else class="text-no-bold">
              {{ item.description }}
            </h2>
          </v-fade-transition>
        </v-col>
      </v-row>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
  export default {
    name: "Organization",
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
