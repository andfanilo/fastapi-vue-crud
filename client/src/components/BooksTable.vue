<template>
  <div class="py-6">
    <h1 class="text-4xl tracking-wide text-gray-800">{{ heading }}</h1>
    <hr class="mb-4" />
    <button
      type="button"
      class="bg-green-500 hover:bg-green-700 text-white px-4 py-2 mb-4 rounded"
    >
      Add Book
    </button>
    <table class="table-fixed">
      <thead>
        <tr>
          <th class="px-4 py-2">Title</th>
          <th class="px-4 py-2">Author</th>
          <th class="px-4 py-2">Read</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <template v-for="book in books">
          <tr v-bind:key="`${book.title}-row`" class="even:bg-gray-200">
            <td v-bind:key="`${book.title}-title`" class="border px-4 py-2">
              {{ book.title }}
            </td>
            <td v-bind:key="`${book.title}-author`" class="border px-4 py-2">
              {{ book.author }}
            </td>
            <td v-bind:key="`${book.title}-read`" class="border px-4 py-2">
              {{ book.read ? "Yes" : "No" }}
            </td>
            <td class="border px-4 py-2">
              <div role="group">
                <button
                  type="button"
                  class="bg-blue-500 rounded text-white text-sm px-3 py-2 mr-3"
                >
                  Update
                </button>
                <button
                  type="button"
                  class="bg-red-500 rounded text-white text-sm px-3 py-2"
                >
                  Delete
                </button>
              </div>
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BooksTable",
  props: {
    heading: String
  },
  data() {
    return {
      books: []
    };
  },
  methods: {
    getBooks() {
      const path = `${process.env.VUE_APP_BACKEND_API}/books`;
      axios
        .get(path)
        .then(res => {
          this.books = res.data.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {
    this.getBooks();
  }
};
</script>
