<template>
  <div id="app">
    <BooksTable heading="Books" />
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
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
<style src="./assets/tailwind.css"></style>
