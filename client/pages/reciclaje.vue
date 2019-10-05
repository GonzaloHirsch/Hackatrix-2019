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
        <div class="recycle-category" v-for="category in categories" :key="category.id" @click="category.showSubcategories = true">
            <img class="tw-absolute tw-left-0 tw-top-0 tw-w-full tw-h-full tw-object-cover" :src="category.img" alt="">
            <div class="tw-z-10">
                <h1 class="tw-text-xl tw-font-bold tw-uppercase tw-tracking-wide">{{ category.name }}</h1>
            </div>
            <!-- <div v-if="category.showSubcategories">
                <div  v-for="subcategory in category.subcategories" :key="subcategory.id">
        
                    <h2>{{ subcategory.name }}</h2>
                </div>
            </div> -->
        </div>
    </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            categories: [
                {
                    name: "Cartón",
                    img: "https://images.unsplash.com/photo-1509956563346-93a1179cea68?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80",
                    showSubcategories: false,
                    subcategories: [
                        {
                            id: 4,
                            name: "Cartón Mojado",
                            img: "https://images.unsplash.com/photo-1564413679915-b0c50085eddb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"
                        },
                        {
                            id: 5,
                            name: "Cartón Seco",
                            img: "https://5.imimg.com/data5/VI/AA/MY-2196349/corrugated-cardboard-sheet-500x500.jpg"
                        }
                    ]
                },
                {
                    name: "Plástico",
                    img: "https://images.unsplash.com/photo-1530587191325-3db32d826c18?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80"
                }
            ]
        }
    }
}
</script>

<style>
.recycle-category {
    @apply tw-h-48 tw-w-48 tw-mx-4 tw-bg-gray-800 tw-flex tw-items-center tw-justify-center tw-overflow-hidden tw-relative tw-rounded-lg tw-cursor-pointer tw-shadow;
    transition: all 150ms ease;
}

.recycle-category:hover {
    @apply tw-shadow-md;
    transform: translateY(-2px);
}
</style>