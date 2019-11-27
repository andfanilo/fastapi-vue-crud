<template>
  <div>
    <h1>{{ heading }}</h1>
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
                <button type="button" class="bg-blue-500 rounded">
                  Update
                </button>
                <button type="button" class="bg-red-500 rounded">Delete</button>
              </div>
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "BooksTable",
  props: {
    heading: String
  },
  data() {
    return {
      books: [
        { title: "Intro to CSS", author: "Adam", read: true },
        {
          title:
            "A Long and Winding Tour of the History of UI Frameworks and Tools and the Impact on Design",
          author: "Adam",
          read: false
        },
        { title: "Into to JavaScript", author: "Chris", read: false }
      ]
    };
  }
};
</script>
