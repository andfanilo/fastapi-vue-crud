<template>
  <div>
    <transition>
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="modal-container">
            <!-- Header -->
            <div class="mt-0 text-xl text-gray-800 border-b">
              {{ heading }}
            </div>

            <!-- Form -->
            <div class="flex justify-between items-center">
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
            <hr />

            <!-- Buttons -->
            <div class="modal-footer">
              <button
                type="button"
                class="bg-green-500 rounded text-white text-sm px-3 py-2"
                v-on:click="sendPayload()"
              >
                {{ okText }}
              </button>
              <button
                type="button"
                class="bg-gray-500 rounded text-white text-sm px-3 py-2"
                v-on:click="closeModal()"
              >
                Close
              </button>
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
    okText: String
  },
  data() {
    return {
      titleIn: "",
      authorIn: "",
      readIn: false
    };
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
