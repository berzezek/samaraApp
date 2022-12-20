<template>
  <div class="flex flex-col">
    <div>
      <h1 class="text-3xl font-bold text-center my-5">{{ data.poll.title }}</h1>
    </div>
    <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
        <div class="overflow-hidden flex justify-center">
          <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mr-4">
            <router-link :to="'/polls/vote-' + data.poll.id">Vote</router-link>
          </button>
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            <router-link to="/polls">Back</router-link>
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
const route = useRoute()

const {data} = await useFetch(`http://localhost:8000/api/v1/polls/${route.params.id}/`)
</script>

<style scoped>

</style>