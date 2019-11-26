<template>
  <div>
    <h1>{{ heading }}</h1>
  </div>
</template>

<script>
export default {
  name: "BooksTable",
  props: {
    heading: String
  }
};
</script>
