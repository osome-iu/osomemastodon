<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Hashtags</h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Search for Hashtags.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Search by keyword - <a href="https://docs.joinmastodon.org/methods/search/" target="_blank">Documetation</a>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-4">
                                    <label>Mastodon Instance</label>
                                    <select
                                        v-model="instanceId"
                                        class="form-control"
                                        v-bind:class="{'is-invalid': instanceIdError !== ''}"
                                        v-on:blur="instanceIdBlurred = true"
                                        @input="instanceInputChanged"
                                    >
                                        <option disabled value="">Choose an instance</option>
                                        <option v-for="item in instanceData" :key="item.name" :value="item.name">{{ item.name }}</option>
                                    </select>
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-4">
                                    <label for="keyword">Keyword</label>
                                    <input
                                        v-model="searchKeyword"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchKeywordError !== ''}"
                                        v-on:blur="searchKeywordBlurred = true"
                                        placeholder="keyword"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchKeywordError !== ''" class="invalid-feedback">{{ searchKeywordError }}</div>
                                </div>
                                <div class="col-xl-3" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" @click="submitStatusSearch">Search</button>
                                </div>
                                <div class="row" style="margin-top: 23px; float: right;" v-if="!loading && downloadData.length">
                                    <div class="col-md-12 text-right">
                                        <button type="button" class="btn btn-warning" @click="downloadAccountJSON">Download JSON</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div style="display: flex; justify-content: center; align-items: center; margin-top: 100px" v-if="loading">
                <hollow-dots-spinner
                    :animation-duration="1000"
                    :dot-size="15"
                    :dots-num="3"
                    color="#ff1d5e"
                />
            </div>
            <div class="card-body">
                <div class="table-responsive" v-if="!loading && hashtagData.length>0" style="font-size: 10px;">
                    <table class="table table-bordered">
                        <thead>
                        <tr>
                            <th scope="col">Name</th>
                            <th scope="col">URL</th>
                        </tr>
                        </thead>
                        <tbody>
                            <tr v-for="hashtag in hashtagData" :key="key">
                                <td>{{hashtag.name}}</td>
                                <td><a :href="hashtag.url" target="_blank" style="text-underline: #0a53be">Link</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="alert alert-warning" v-if="instanceData.length === 0 & !loading">
                    <fa icon="exclamation-triangle" /> No data available.
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import axios from "axios";
import * as constants from "@/shared/Constants";
import { HollowDotsSpinner } from 'epic-spinners';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css'

export default {
    name: 'singleStatus',
    components: {
        HollowDotsSpinner,
    },
    data() {
        return {
            clientKey: null,
            clientSecret: null,
            instanceData:[],
            instanceId: "",
            searchKeyword: "",
            searchType: "",
            hashtagData: [],
            loading: false,
            downloadData: [],
            keywordError: "",
            nameError: false,
            errors: [],
            searchKeywordBlurred: false,
            instanceIdBlurred: false,
            searchKeywordError: "",
            instanceIdError: ""
        }
    },
    methods: {
        successShowToast(message){
            toast.success(message, {
                autoClose: 3000,
            })
        },
        errorShowToast(){
            toast.error('Error in retrieving data!', {
                autoClose: 3000,
            })
        },
        isValidKeyword(keyword) {
            return keyword.trim() !== '';
        },
        isValidInstance(instanceId) {
            return instanceId.trim() !== '';
        },
        viewAccountInfo(accountId){
            this.$router.push({
                name: 'Accounts',  // Assuming you have a route name
                params: { accountId: accountId, instanceId: this.instanceId},
            });
        },
        instanceInputChanged(e){
            let valueReceived = e.target.value
            if(valueReceived){
                this.instanceIdError = ""
                this.instanceIdBlurred = false;
            }
            this.instanceId = e.target.value;
        },
        keywordInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.searchKeywordError = ""
                this.searchKeywordBlurred = false;
            }
        },
        fetchAllInstanceData(){
            let dataUrl = constants.url + '/api/get-instance-data-saved'
            axios.get(dataUrl)
                .then(res => {
                    this.instanceData = res.data;
                }).catch(error => {
                console.log(error);
            });
        },
        submitStatusSearch(){
            this.searchKeywordError = "";
            this.instanceIdError = "";

            if (!this.isValidInstance(this.instanceId)) {
                this.instanceIdError = "Please choose a valid Mastodon instance";
            }

            if (!this.isValidKeyword(this.searchKeyword)) {
                this.searchKeywordError = "Keyword is required";
            }

            if(this.isValidInstance(this.instanceId) && this.isValidKeyword(this.searchKeyword)) {
                this.loading = true;
                let dataUrl = constants.url + '/api/search-status-by-keyword?keyword=' + this.searchKeyword + '&mastodon_instance=' + this.instanceId + '&type=hashtags';
                axios.get(dataUrl)
                    .then(res => {
                        console.log(res)
                        this.hashtagData = res.data.hashtags;
                        this.downloadData = this.hashtagData
                        this.loading = false;
                        let message = this.hashtagData.length +" data retrieved"
                        this.successShowToast(message)
                    }).catch(error => {
                    this.errorShowToast();
                    console.log(error);
                });
            }
        },
        stringifyJSON(stringobject) {
            return JSON.stringify(stringobject, function (key, value) {
                return value;
            }, 4);
        },
        downloadAccountJSON(){
            // Create a Blob containing the JSON data
            const blob = new Blob([JSON.stringify(this.downloadData)], { type: 'application/json' });

            // Create a download link
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'hashtag_details-'+this.searchKeyword+'.json';

            let message = "Data downloaded successfully!"
            this.successShowToast(message)
            // Append the link to the document and trigger the click event
            document.body.appendChild(a);
            a.click();

            // Remove the link from the document
            document.body.removeChild(a);
        },
        extractInstanceName(acct){
            const parts = acct.split('@');
            return parts[1];
        },
        extractURLtoGetInstanceName(acct) {
            const parts = acct.split('/');
            return parts[2];
        }
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>