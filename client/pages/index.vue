<template>
  <div class="container mx-auto">
      <section class="tw-flex tw-flex-wrap tw--mx-4">
          <article v-for="problem in problems" :key="problem.id" class="problem tw-w-1/3  tw-rounded-lg tw-cursor-pointer tw-my-6 tw-px-4" :class="{ 'tw-w-full': selectedProblem && selectedProblem.id == problem.id }" @click="selectedProblem = problem">
              <div class="tw-flex tw-bg-gray-200 tw-rounded-lg">
                  <img class="tw-object-cover tw-w-1/2" :src="problem.imageUrl" alt="">
                  <div class="tw-w-1/2 tw-p-6">
                    <h1 class="tw-break-words tw-font-bold tw-text-2xl tw-uppercase tw-tracking-wide tw-leading-tight">{{ problem.title }}</h1>
                    <p>{{ problem.description }}</p>
                  </div>
              </div>
          </article>
      </section>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
    data() {
        return {
            selectedProblem: null
        }
    },
    computed: {
        ...mapState({
            problems: state => state.problems
        })
    }
}
</script>

<style>
.problem {
    transition: width 300ms ease;
}
</style>