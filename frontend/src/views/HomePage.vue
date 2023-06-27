<template>
    <AppNavBar/>
    <div id="app" style="margin-top: 100px">
        <div class="container">
            <div class="inner-div">
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
                    <label for="search_string">Search</label>
                    <input id="search_string" v-model="searchString" placeholder="Enter search string">
                </div>
                <div>
                    <button @click="submitSearch" class="btn btn-success" style="margin-top: 30px">Search</button>
                </div>
            </div>
            <div v-if="loading" class="loading-icon">Loading...</div>

            <div v-if="searchResults.length > 0" style="margin-top: 40px" id="home_table">
                <table class="table table-bordered">
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
    </div>
    <AppFooter/>
</template>

<script>
import axios from 'axios';
import AppNavBar from "../components/AppNavbar.vue";
import AppFooter from "../components/AppFooter.vue"
import * as constants from "@/shared/constant";

export default {
    name: 'HomePage',
    components: {
        AppNavBar,
        AppFooter
    },
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
                const response = await axios.post(constants.url+'/search', {
                    instance: this.selectedInstance,
                    search_string: this.searchString,
                    search_type: this.searchType,
                });
                if (response.data) {
                    this.searchResults = response.data;
                    console.log(this.searchResults)
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
            const response = await axios.get(constants.url+'/instances');
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

.inner-div {
    width: 60%;
    margin: 0 auto;
}

#home_table{
    font-size: 10px;
}
</style>
