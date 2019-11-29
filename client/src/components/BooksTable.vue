<template>
  <div class="py-6">
    <!-- Heading line -->
    <h1 class="text-4xl tracking-wide text-gray-800 border-b mb-4">
      {{ heading }}
    </h1>

    <!-- Add book button -->
    <div>
      <button
        type="button"
        class="bg-green-500 hover:bg-green-700 text-white px-4 py-2 mb-4 rounded"
        v-on:click="openModal('Add book', 'Add')"
      >
        Add Book
      </button>
    </div>

    <!-- Books table -->
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
                  class="bg-blue-500 hover:bg-blue-700 rounded text-white text-sm px-3 py-2 mr-3"
                  v-on:click="openModal('Update book details', 'Update')"
                >
                  Update
                </button>
                <button
                  type="button"
                  class="bg-red-500 hover:bg-red-700 rounded text-white text-sm px-3 py-2"
                >
                  Delete
                </button>
              </div>
            </td>
          </tr>
        </template>
      </tbody>
    </table>

    <!-- Modal window -->
    <Modal
      v-if="showModal"
      v-on:closeModal="onCloseModal"
      v-bind:heading="modalHeading"
      v-bind:okText="modalOkText"
    >
    </Modal>
  </div>
</template>

<script>
import axios from "axios";
import Modal from "./Modal.vue";

export default {
  name: "BooksTable",
  components: {
    Modal
  },
  props: {
    heading: String
  },
  data() {
    return {
      modalHeading: "", // text in heading of modal window
      modalOkText: "", // text in ok button of modal window
      books: [], // list of books to display in table
      showModal: false // variable defining visibility of modal window
    };
  },
  methods: {
    /**
     * Open Modal window
     * @param modalHeading Text in heading of modal window
     * @param modalOkText  Text in OK button of modal window
     */
    openModal(modalHeading, modalOkText) {
      this.modalHeading = modalHeading;
      this.modalOkText = modalOkText;
      this.showModal = true;
    },
    /**
     * Close Modal window and deal with payload
     * @param modalPayload object sent back from Modal component
     */
    onCloseModal(modalPayload) {
      this.addBook(modalPayload);
      this.showModal = false;
    },
    /**
     * Get all books from API
     */
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
    /**
     * Add book from API
     * @param payload book details in JSON
     */
    addBook(payload) {
      const path = `${process.env.VUE_APP_BACKEND_API}/books`;
      axios
        .post(path, payload)
        .then(() => {
          this.getBooks();
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    }
  },
  mounted() {
    this.getBooks();
  }
};
</script>
