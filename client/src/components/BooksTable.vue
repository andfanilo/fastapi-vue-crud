<template>
  <div class="py-6">
    <h1 class="text-4xl tracking-wide text-gray-800">{{ heading }}</h1>
    <hr class="mb-4" />

    <div class="flex justify-between items-center">
      <div>
        <div class="py-2">
          <label for="title" class="mr-2">Enter book title</label>
          <input
            v-model="titleIn"
            id="title"
            placeholder="Title"
            class="border"
          />
        </div>
        <div class="py-2">
          <label for="author" class="mr-2">Enter book author</label>
          <input
            v-model="authorIn"
            id="author"
            placeholder="Author"
            class="border"
          />
        </div>
        <div class="py-2">
          <label for="read" class="mr-2">Have you read it ?</label>
          <input type="checkbox" id="read" v-model="readIn" />
        </div>
      </div>

      <div>
        <button
          type="button"
          class="bg-green-500 hover:bg-green-700 text-white px-4 py-2 mb-4 rounded"
          v-on:click="addBook()"
        >
          Add Book
        </button>
      </div>
    </div>

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
      titleIn: "",
      authorIn: "",
      readIn: false,
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
    },
    resetForm() {
      this.titleIn = "";
      this.authorIn = "";
      this.readIn = false;
    },
    addBook() {
      const path = `${process.env.VUE_APP_BACKEND_API}/books`;
      let payload = {
        title: this.titleIn,
        author: this.authorIn,
        read: this.readIn
      };
      axios
        .post(path, payload)
        .then(() => {
          this.resetForm();
          this.getBooks();
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
          this.resetForm();
          this.getBooks();
        });
    }
  },
  mounted() {
    this.getBooks();
  }
};
</script>
