<template>
  <section class="w-full" style="height: 50vh;">
    <img class="tw-object-cover tw-w-full tw-h-full" :src="currentCategory.img" alt="">
    <h1 class="tw-mt-8 tw-text-center tw-text-5xl tw-font-bold tw-uppercase tw-tracking-wide ">
      {{ currentCategory.name }}
    </h1>
  </section>
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
