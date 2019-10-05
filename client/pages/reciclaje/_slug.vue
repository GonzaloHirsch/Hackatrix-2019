<template><v-container fluid>
  <v-row justify="center">
    <v-col md="6" lg="8">
      <div class="pl-6 display-1">
        {{ currentCategory.name }}
      </div>
    </v-col>
  </v-row>

<!--  <v-row justify="center" dense class="pb-8 pl-6 pr-6 mb-n8">-->
<!--    <v-col md="6" lg="8">-->
<!--      <v-select-->
<!--        chips-->
<!--        label="Tipo de Tip"-->
<!--        multiple-->
<!--        solo-->
<!--        :items="filterChips"-->
<!--        clearable-->
<!--        deletable-chips-->
<!--        @change="chipFilterAdded"-->
<!--        menu-props="offsetY"-->
<!--      >-->
<!--      </v-select>-->
<!--    </v-col>-->
<!--  </v-row>-->

<!--  <div v-for="item in items" class="pb-8" :hidden="item.hidden">-->
<!--    <v-row justify="center">-->
<!--      <v-col md="6" lg="8">-->
<!--        <div class="pl-6 headline">{{ item.type }}</div>-->
<!--      </v-col>-->
<!--    </v-row>-->

<!--    <v-row justify="center">-->
<!--      <v-col md="6" lg="8">-->
<!--        <v-expansion-panels popout>-->
<!--          <Tip-->
<!--            v-for="tip in item.tips"-->
<!--            :key="tip.title"-->
<!--            :title="tip.title"-->
<!--            :items="tip.items"-->
<!--          ></Tip>-->
<!--        </v-expansion-panels>-->
<!--      </v-col>-->
<!--    </v-row>-->
<!--  </div>-->

</v-container>
</template>

<script>
import { mapState } from "vuex";

export default {
    props: [""],
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
