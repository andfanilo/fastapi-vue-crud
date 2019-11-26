<template>
  <div id="app">
    <BooksTable heading="Welcome to Your Vue.js App" />
    <AlertButton msg="Ping!" />
  </div>
</template>

<script>
import AlertButton from "./components/AlertButton.vue";
import BooksTable from "./components/BooksTable.vue";

export default {
  name: "app",
  components: {
    AlertButton,
    BooksTable
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
<style src="./assets/tailwind.css"></style>
