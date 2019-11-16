<template>
  <div>
    <button class="button" v-on:click="onButtonPress">
      {{ this.msg }}
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AlertButton",
  props: ["msg"],
  methods: {
    onButtonPress: function() {
      axios
        .get("http://localhost:8000/ping")
        .then(response => {
          alert(response.data.result);
        })
        .catch(error => {
          if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
          } else if (error.request) {
            // The request was made but no response was received
            // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
            // http.ClientRequest in node.js
            console.log(error.request);
            alert("Ping-pong server is not available");
          } else {
            // Something happened in setting up the request that triggered an Error
            console.log("Error", error.message);
          }
          console.log(error.config);
        });
    }
  }
};
</script>

<style scoped>
.button {
  background-color: #4caf50; /* Green */
  border: none;
  color: white;
  padding: 1em 2em;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 1em;
}
</style>
