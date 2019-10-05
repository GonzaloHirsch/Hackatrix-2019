<template>
  <div class="container mx-auto">
      <section class="tw-flex tw-flex-wrap tw--mx-4">
          <article v-for="problem in problems" :key="problem.id" class="problem tw-w-1/3  tw-rounded-lg tw-cursor-pointer tw-my-6 tw-px-4" :class="{ 'tw-w-full': isSelected(problem) }" @click="selectedProblem = problem">
              <div class="tw-flex tw-bg-gray-200 tw-rounded-lg" :class="{ 'tw-flex-col': !isSelected(problem) }">
                  <img class="tw-object-cover tw-w-1/2" :class="{ 'tw-w-full': !isSelected(problem) }" :src="problem.imageUrl" alt="">
                  <div class="tw-w-1/2 tw-p-6" :class="{ 'tw-w-full': !isSelected(problem) }">
                    <h1 class="tw-break-words tw-font-bold tw-text-2xl tw-uppercase tw-tracking-wide tw-leading-tight tw-mb-6">{{ problem.title }}</h1>
                    <div :class="{ 'tw-hidden': !isSelected(problem) }">
                        <p>{{ problem.description }}</p>
                        <ul>
                            <li v-for="(cause, i) in problem.causes" :key="i"><v-icon color="red">error</v-icon> {{ cause }}</li>
                        </ul>
                    </div>
                  </div>
              </div>
          </article>
      </section>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
    async asyncData({ $axios }) {
        const problems = await $axios.$get("/problems");

        return {
            problems
        }
    },
    data() {
        return {
            selectedProblem: null
        }
    },
    methods: {
        isSelected(problem) {
            return this.selectedProblem && this.selectedProblem.id == problem.id;
        }
    },
    computed: {
        // ...mapState({
        //     problems: state => state.problems
        // })
    }
}
</script>

<style>
.problem {
    transition: width 300ms ease;
}
</style>
