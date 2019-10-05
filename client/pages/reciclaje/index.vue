<template>
  <div>
    <header class="tw-mb-32 tw-w-full tw-bg-gray-500 tw-flex tw-justify-center tw-items-center" style="height: 200px;">
        <div class="tw-inline-block">
            <v-text-field
                filled
                label="Prepend inner"
                class="tw-w-full"
            ></v-text-field>
            <v-icon>mdi-place</v-icon>
        </div>
    </header>

    <div class="tw-container mx-auto tw-flex tw-justify-center">
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