<template>
  <v-expansion-panel>
    <v-expansion-panel-header v-slot="{ open }">
      <v-row align="center" justify="space-between">
        <v-col cols="auto">
          <v-fade-transition leave-absolute>
            <div v-if="!open" class="title">
              {{ title }}
            </div>

            <div v-else class="headline">
              {{ title }}
            </div>
          </v-fade-transition>
        </v-col>
        <v-col cols="auto" class="pr-8">
          <v-avatar color="primary" size="36" v-if="counter != null">
            <span class="tw-text-white"> {{ counter }} </span>
          </v-avatar>
          <v-btn icon color="primary" @click.stop="incrementCounter()" :hidden="!buttonVisibility">
            <v-icon>add</v-icon>
          </v-btn>

        </v-col>
      </v-row>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-container v-if="!open" fluid dense>
        <v-divider></v-divider>
        <ul>
          <li v-for="item in items">- {{item}}</li>
        </ul>
      </v-container>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
  export default {
    title: "Tip",
    props: {
      title: {
        type: String,
        required: true
      },
      items: {
        type: Array,
        required: true
      },
      counter: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        buttonVisibility: true
      };
    },
    methods: {
      incrementCounter() {
        this.counter++;
        this.buttonVisibility = false;
      }
    }
  }
</script>

<style scoped>

</style>
