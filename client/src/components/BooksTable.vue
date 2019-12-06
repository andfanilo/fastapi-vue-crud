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
        v-on:click="openModal('add')"
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
        <template v-for="[index, book] in books.entries()">
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
                  v-on:click="openModal('edit', index)"
                >
                  Update
                </button>
                <button
                  type="button"
                  class="bg-red-500 hover:bg-red-700 rounded text-white text-sm px-3 py-2"
                  v-on:click="openModal('delete', index)"
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
    <Modal v-if="showModal" v-on:closeModal="onCloseModal" v-bind="modalState">
    </Modal>
  </div>
</template>

<script>
import axios from "axios";
import Modal from "./Modal.vue";

const modalStates = {
  NORMAL: {},
  ADD: {
    heading: "Add book",
    buttonText: "Add",
    buttonColor: "green",
    showForm: true
  },
  EDIT: {
    heading: "Update book details",
    buttonText: "Update",
    buttonColor: "blue",
    showForm: true
  },
  DELETE: {
    heading: "Are you sure you want to delete the book ?",
    buttonText: "Delete",
    buttonColor: "red",
    showForm: false
  }
};

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
      books: [], // list of books to display in table
      showModal: false, // variable defining visibility of modal window,
      modalState: {}, // state modal window is currently in
      rowEdited: -1 // row currently edited or deleted
    };
  },
  methods: {
    /**
     * Open Modal window
     * @param m which state button generated
     * @param index of button row selected
     */
    openModal(m, index = -1) {
      this.rowEdited = index;
      switch (m) {
        case "add":
          this.modalState = modalStates.ADD;
          break;
        case "edit":
          this.modalState = modalStates.EDIT;
          break;
        case "delete":
          this.modalState = modalStates.DELETE;
          break;
        default:
          throw new TypeError(
            `State was ${m} which is not add, edit or delete`
          );
      }
      this.showModal = true;
    },
    /**
     * Close Modal window and deal with payload
     * @param modalPayload object sent back from Modal component
     */
    onCloseModal(modalPayload) {
      let currentState = this.modalState;
      let editedId = this.rowEdited;
      this.modalState = modalStates.NORMAL;
      this.rowEdited = -1;
      this.showModal = false;
      // first check that object is not empty
      if (
        Object.keys(modalPayload).length === 0 &&
        modalPayload.constructor === Object
      ) {
        return;
      }
      // switch on modal state
      switch (currentState) {
        case modalStates.ADD:
          this.addBook(modalPayload);
          break;
        case modalStates.EDIT:
          this.editBook(modalPayload, editedId);
          break;
        case modalStates.DELETE:
          this.removeBook(editedId);
      }
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
    },
    /**
     * Edit book from API
     * @param payload book details in JSON
     * @param id of book
     */
    editBook(payload, id) {
      const path = `${process.env.VUE_APP_BACKEND_API}/books/${id}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getBooks();
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    /**
     * Remove book from API
     * @param id of book
     */
    removeBook(id) {
      const path = `${process.env.VUE_APP_BACKEND_API}/books/${id}`;
      axios
        .delete(path)
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
