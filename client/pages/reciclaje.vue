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
        <div v-if="!selectedCategory" class="tw-flex">
            <RecycleCategory v-for="category in categories" :key="category.id" @click.native="selectedCategory = category" :category="category" />
        </div>

        <div v-if="selectedCategory">
            {{ selectedCategory.name }}
        </div>
    </div>
  </div>
</template>

<script>
import RecycleCategory from "@/components/RecycleCategory";

export default {
    components: {
        RecycleCategory
    },
    data() {
        return {
            selectedCategory: null,
            categories: [
                {
                    id: 1,
                    name: "Cartón",
                    img: "https://images.unsplash.com/photo-1509956563346-93a1179cea68?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80",
                    info: {
                        place: "asdasdasd"
                    }
                },
                {
                    id: 2,
                    name: "Plástico",
                    img: "https://images.unsplash.com/photo-1530587191325-3db32d826c18?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80"
                }
            ]
        }
    }
}
</script>

<style>

</style>