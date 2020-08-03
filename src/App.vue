<template>
  <div id="app">
    <div class="container">
      <h1>{{picker()}} {{chosenQuote.en}}</h1>
      <h2>-{{chosenQuote.author}}</h2>
      <h3>{{simQuote}}</h3>
      <div class="col-3">
        <p>
          <rate v-model="myCurrentRate" :length="5" :ratedesc="desc"></rate>
        </p>
      </div>
    </div>
  </div>
</template>


<script>
import json from "./data/quotes.json";
import rate from "./components/Rate.vue";

export default {
  name: "App",
  data() {
    return {
      myJson: json,
      chosenQuote: [],
      myCurrentRate: 0,
      desc: ["Very Bad", "Bad", "Normal", "Good", "Very Good"]
    };
  },
  components: {
    rate
  },
  methods: {
    picker: function() {
      var chosenNumber = Math.floor(Math.random() * this.myJson.length);
      this.chosenQuote = this.myJson[chosenNumber];
    }
  }
};
</script>

<style>
* {
  box-sizing: border-box;
}
body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.container {
  max-width: 1200px;
  padding: 0 20px;
  margin: 0 auto;
}
.grid {
  display: flex;
  flex-wrap: wrap;
}
.code {
  text-align: left;
  background-color: #efefef;
  border-radius: 10px;
  padding: 20px;
  overflow: auto;
  max-width: 100%;
}
.code pre {
  margin: 0;
}
.Rate.RateCustom .icon {
  width: 25px;
  height: 25px;
}
.Rate.RateCustom .Rate__star.filled {
  color: teal;
}
.Rate.RateCustom .Rate__star.hover {
  color: red;
}
.flex-primary {
  flex: 1;
  width: 100%;
}
.grid [class*="col-"] {
  padding: 0 20px;
}
.grid .col-3 {
  width: 100%;
}
@media screen and (min-width: 768px) {
  .grid .col-3 {
    width: 50%;
  }
  .grid .col-2 {
    width: 50%;
  }
}
@media screen and (min-width: 992px) {
  .grid .col-3 {
    width: 25%;
  }
}
</style>
