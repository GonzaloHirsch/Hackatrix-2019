<template>
  <div>

    <div class="tw-container mx-auto tw-flex tw-justify-center tw-mt-32">
        <div class="tw-flex">
            <nuxt-link v-for="category in recycleCategories" :key="category.id" :to="'/reciclaje/' + category.slug">
                <RecycleCategory :category="category" />
            </nuxt-link>
        </div>

        <!-- <div v-if="selectedCategory">
            {{ selectedCategory.name }}
        </div> -->
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import RecycleCategory from "@/components/RecycleCategory";

export default {
    components: {
        RecycleCategory
    },
    data() {
        return {
            selectedCategory: null,
        }
    },
    computed: {
        ...mapState({
            recycleCategories: state => state.recycleCategories
        })
    }
}
</script>

<style>

</style>
