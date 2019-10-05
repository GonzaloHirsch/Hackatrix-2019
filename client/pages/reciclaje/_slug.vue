<template>
  <section class="w-full" style="height: 50vh;">
    <img class="tw-object-cover tw-w-full tw-h-full" :src="currentCategory.img" alt="">
    <h1 class="tw-mt-8 tw-text-center tw-text-5xl tw-font-bold tw-uppercase tw-tracking-wide ">
      {{ currentCategory.name }}
    </h1>

    <v-container fluid>
      <v-row justify="center" v-if="currentCategory.actions.length > 0">
        <v-col cols="auto">
          <div class="display-1">¿Como se encuentra el material?</div>
        </v-col>
      </v-row>

      <v-row justify="center">
        <v-col cols="auto" :key="action.name" v-for="action in currentCategory.actions">
          <v-btn rounded x-large color="primary" :outlined="selectedAction == null || selectedAction.name !== action.name" @click="selectedAction = action">
            {{ action.name }}
          </v-btn>
        </v-col>
      </v-row>

      <v-row justify="center" v-if="selectedAction">
        <v-col cols="auto">
          <div class="headline">{{selectedAction.description}}</div>
        </v-col>
      </v-row>
      <div class="title tw-text-center" v-if="selectedAction && selectedAction.valid">
        <v-row align="center" justify="center">
          <v-col>
            Direccion{{currentCategory.addresses.length === 1 ? "" : "es"}}:
          </v-col>
        </v-row>
        <ul>
          <li v-for="address in currentCategory.addresses">- {{address}}</li>
        </ul>
      <v-row align="center" justify="center">
        <v-col>
          <img :src="currentCategory.img_map" class="tw-text-center tw-mx-auto" alt="">
        </v-col>
      </v-row>
      </div>

    </v-container>
  </section>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      selectedAction: null
    }
  },
    computed: {
        ...mapState({
            recycleCategories: state => state.recycleCategories
        }),
        currentCategory() {
            return this.recycleCategories.filter(c => c.slug == this.$route.params.slug)[0]
        }
    }
}
</script>

<style>

</style>
