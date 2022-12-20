<template>
  <div>
    <LoginForm
        :form="{ mainTitle: 'Sign up', buttonTitle: 'Sign up', toggle: 'Sign in'}"
      @submitForm="submitForm"
    />
  </div>
</template>

<script setup>

const submitForm = (username, password) => {
  console.log(username.value, password.value)
}
</script>