<template>
  <div id="app">
    <h1>Mastodon Search</h1>
    <div>
      <label for="instance">Instance:</label>
      <select id="instance" v-model="selectedInstance">
        <option v-for="instance in instances" :key="instance" :value="instance">{{ instance }}</option>
      </select>
    </div>
    <div>
      <label for="search_type">Search Type:</label>
      <select id="search_type" v-model="searchType">
        <option value="user">User</option>
        <option value="post">Post</option>
        <option value="hashtag">Hashtag</option>
      </select>
    </div>
    <div>
      <label for="search_string">Search String:</label>
      <input id="search_string" v-model="searchString" placeholder="Enter search string">
    </div>
    <button @click="submitSearch">Search</button>
    <div v-if="loading" class="loading-icon">Loading...</div>
    <div v-if="searchResults.length > 0">
      <table class="results-table">
        <thead>
          <tr>
            <th v-for="(value, key) in searchResults[0]" :key="key">{{ key }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(result, index) in searchResults" :key="index">
            <td v-for="(value, key) in result" :key="key">
              <div v-if="key === 'post'" v-html="value"></div>
              <a v-else-if="key === 'url'" :href="value" target="_blank">{{ value }}</a>
              <div v-else>{{ value }}</div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      instance: '',
      searchType: 'user',
      searchString: '',
      searchResults: [],
      instances: [],
      selectedInstance: '',
      loading: false
    };
  },
  methods: {
    async submitSearch() {
      try {
        this.loading = true;
        const response = await axios.post('http://127.0.0.1:7000/search', {
          instance: this.selectedInstance,
          search_string: this.searchString,
          search_type: this.searchType,
        });



        if (response.data) {
          this.searchResults = response.data;
        } else {
          this.searchResults = [];
          alert('Error: Could not fetch search results.');
        }
      } catch (error) {
        this.downloadLink = '';
        alert('Error: ' + error);
      } finally {
        this.loading = false;
      }
    }
  },
  async created() {
      try {
        const response = await axios.get('http://127.0.0.1:7000/instances');
        this.instances = response.data;
        this.selectedInstance = this.instances[0];
      } catch (error) {
        console.error('Error fetching instances:', error);
      }
    }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}

label {
  display: block;
  margin-top: 20px;
}

input,
select {
  width: 100%;
  margin-top: 5px;
  padding: 5px;
  font-size: 16px;
}

button {
  display: block;
  width: 100%;
  margin-top: 20px;
  padding: 10px;
  font-size: 18px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #2c3e50;
}

.results-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
}

.results-table th,
.results-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.results-table th {
  background-color: #f2f2f2;
  color: #333;
}

.results-table tr:nth-child(even) {
  background-color: #f8f8f8;
}

.results-table tr:hover {
  background-color: #ddd;
}

a {
  margin-top: 20px;
  display: inline-block;
  text-decoration: none;
  color: #42b983;
}

a:hover {
  text-decoration: underline;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}
</style>
