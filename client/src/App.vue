<template>
  <div id="app" class="container mx-auto">
    <Header />
    <BooksTable heading="Books" class="px-4 py-4" />
    <AlertButton msg="Ping!" class="px-4 py-4" />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import AlertButton from "./components/AlertButton.vue";
import BooksTable from "./components/BooksTable.vue";

export default {
  name: "app",
  components: {
    Header,
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
