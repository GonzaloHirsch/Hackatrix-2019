<template>
    <article class="recycle-category">
        <img class="tw-absolute tw-left-0 tw-top-0 tw-w-full tw-h-full tw-object-cover tw-rounded-lg" :src="category.img" style="filter: brightness(0.65);">
        <div class="tw-z-10">
            <h1 class="tw-text-2xl tw-font-bold tw-uppercase tw-tracking-wide tw-text-white">{{ category.name }}</h1>
        </div>
    </article>
</template>

<script>
export default {
    props: ["category"]
}
</script>

<style>
.recycle-category {
    @apply tw-h-48 tw-w-48 tw-mx-4 tw-bg-gray-800 tw-flex tw-items-center tw-justify-center tw-overflow-hidden tw-relative tw-rounded-lg tw-cursor-pointer tw-shadow tw-text-center;
    transition: all 150ms ease;
}

.recycle-category:hover {
    @apply tw-shadow-md;
    transform: translateY(-2px);
}
</style>