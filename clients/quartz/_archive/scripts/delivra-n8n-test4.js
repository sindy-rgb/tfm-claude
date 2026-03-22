// TEST — trying every possible HTTP helper n8n might expose
var results = [];

// Test 1: $http
try {
  await $http.request({ method: "GET", url: "https://httpbin.org/get" });
  results.push("$http works");
} catch (e) {
  results.push("$http FAILED: " + e.message);
}

// Test 2: this.$http
try {
  await this.$http.request({ method: "GET", url: "https://httpbin.org/get" });
  results.push("this.$http works");
} catch (e) {
  results.push("this.$http FAILED: " + e.message);
}

// Test 3: helpers
try {
  await helpers.request({ method: "GET", url: "https://httpbin.org/get" });
  results.push("helpers.request works");
} catch (e) {
  results.push("helpers.request FAILED: " + e.message);
}

// Test 4: $helpers
try {
  await $helpers.request({ method: "GET", url: "https://httpbin.org/get" });
  results.push("$helpers.request works");
} catch (e) {
  results.push("$helpers.request FAILED: " + e.message);
}

// Test 5: axios
try {
  var axios = require("axios");
  await axios.get("https://httpbin.org/get");
  results.push("axios works");
} catch (e) {
  results.push("axios FAILED: " + e.message);
}

return [{ json: { tests: results } }];
