<template>
    <div>
        {{ currentCategory.name }}
    </div>
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