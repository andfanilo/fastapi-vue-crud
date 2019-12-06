<template>
  <div>
    <transition>
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="modal-container">
            <!-- Header -->
            <div class="mt-0 text-xl text-gray-800 mb-2">
              {{ heading }}
            </div>

            <div class="w-full max-w-xs">
              <!-- Form -->
              <form
                v-if="showForm"
                class="bg-white rounded px-8 pt-6 pb-8 shadow mb-4"
              >
                <div class="mb-2">
                  <label
                    class="block text-gray-700 text-sm font-bold mb-2"
                    for="title"
                  >
                    Enter book title
                  </label>
                  <input
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="title"
                    type="text"
                    placeholder="Book title"
                    v-model="titleIn"
                  />
                </div>
                <div class="mb-4">
                  <label
                    class="block text-gray-700 text-sm font-bold mb-2"
                    for="author"
                  >
                    Enter book author
                  </label>
                  <input
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="author"
                    type="text"
                    placeholder="Book author"
                    v-model="authorIn"
                  />
                </div>
                <div>
                  <label for="read" class="mr-2">Have you read it ?</label>
                  <input type="checkbox" id="read" v-model="readIn" />
                </div>
              </form>

              <!-- Buttons -->
              <div class="flex items-center">
                <button
                  class="text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  v-bind:class="okButtonStyle"
                  v-bind:disabled="!formCompleted() && showForm"
                  type="button"
                  v-on:click="sendPayload()"
                >
                  {{ buttonText }}
                </button>
                <button
                  class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline ml-4"
                  type="button"
                  v-on:click="closeModal()"
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "Modal",
  props: {
    heading: String,
    buttonText: String,
    buttonColor: String,
    showForm: Boolean
  },
  data() {
    return {
      titleIn: "",
      authorIn: "",
      readIn: false
    };
  },
  computed: {
    okButtonStyle: function() {
      let colorClass = `bg-${this.buttonColor}-500 hover:bg-${this.buttonColor}-700`;
      if (!this.formCompleted() && this.showForm) {
        colorClass += " opacity-50 cursor-not-allowed";
      }
      return colorClass;
    }
  },
  methods: {
    resetForm() {
      this.titleIn = "";
      this.authorIn = "";
      this.readIn = false;
    },
    closeModal() {
      this.$emit("closeModal", {});
      this.resetForm();
    },
    sendPayload() {
      let payload = {
        title: this.titleIn,
        author: this.authorIn,
        read: this.readIn
      };
      this.$emit("closeModal", payload);
      this.resetForm();
    },
    formCompleted() {
      return this.titleIn !== "" && this.authorIn !== "";
    }
  }
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 999;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}
.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.modal-container {
  width: 300px;
  margin: 0 auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  font-family: "Helvetica", Arial, sans-serif;
}
.modal-enter {
  opacity: 0;
}
.modal-leave-active {
  opacity: 0;
}
.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
