<template>
  <div class="antialiased text-gray-900 px-6">
    <div class="max-w-xl mx-auto py-12 divide-y md:max-w-4xl">
      <div class="py-8">
        <h1 class="text-4xl font-bold text-center">{{ props.form.mainTitle }}</h1>
      </div>
      <div class="py-12">
        <div class="mt-2">
          <div class="grid grid-cols-1 gap-6">
            <label class="block">
              <span class="text-gray-700">Login</span>
              <input type="text" class="mt-1 block w-full" v-model="username">
            </label>
            <label class="block">
              <span class="text-gray-700">Password</span>
              <input type="password" class="mt-1 block w-full" v-model="password">
            </label>
          </div>
          <div class="mt-6 flex justify-end">
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mx-5">
              {{ props.form.toggle }}
            </button>
            <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" @click="submitForm">
              {{ props.form.buttonTitle }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const emit = defineEmits(['submitForm'])
const props = defineProps({
  form: {
    type: Object,
    default: () => ({
      mainTitle: 'Sign in',
      buttonTitle: 'Sign in',
      toggle: 'Sign up',
    }),
  }
})

const username = ref('')
const password = ref('')

const submitForm = () => {
  emit('submitForm', username, password)
}

</script>

