<template>
  <div class="flex justify-between items-center py-4 bg-green-500">
    <div class="flex-shrink-0 ml-10 cursor-default">
      <span class="ml-1 text-3xl text-white font-semibold">Hello World !</span>
    </div>
    <ul class="hidden md:flex overflow-x-hidden mr-10 font-semibold">
      <li class="mr-6 p-1 border-b-2 border-orange-500">
        <a class="text-white cursor-default" href="#">Home</a>
      </li>
      <li class="mr-6 p-1">
        <a
          class="text-white hover:text-green-300"
          href="https://fastapi.tiangolo.com/"
          >FastAPI</a
        >
      </li>
      <li class="mr-6 p-1">
        <a class="text-white hover:text-green-300" href="https://vuejs.org/"
          >Vue.js</a
        >
      </li>
      <li class="mr-6 p-1">
        <a
          class="text-white hover:text-green-300"
          href="https://tailwindcss.com/"
          >Tailwindcss</a
        >
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Header"
};
</script>
