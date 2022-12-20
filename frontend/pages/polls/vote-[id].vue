<template>
  <h1>vote - {{ vote }}</h1>
  {{ data.questions }}
</template>

<script setup>
const route = useRoute()
const vote = route.params.id

const {data} = await useFetch(`http://localhost:8000/api/v1/polls/${route.params.id}/`)

</script>

<style scoped>

</style>