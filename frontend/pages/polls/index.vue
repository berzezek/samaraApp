<template>
  <div class="flex flex-col">
    <div>
      <h1 class="text-3xl font-bold text-center my-5">Polls</h1>
    </div>
    <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
        <div class="overflow-hidden">
          <table class="min-w-full">
            <thead class="bg-blue-50 border-b text-center">
            <tr>
              <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4">
                #
              </th>
              <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4">
                Title
              </th>
            </tr>
            </thead>
            <tbody class="text-center">

            <tr class="bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100" v-for="poll in polls"
                @click="toPoll(poll.id)">

              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">1</td>
              <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                {{ poll.title }}
              </td>

            </tr>

            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup>

const {data: polls} = await useFetch('http://localhost:8000/api/v1/polls/')
const router = useRouter()
const toPoll = (id) => {
  router.push('/polls/' + id)
}

</script>

<style scoped>

</style>