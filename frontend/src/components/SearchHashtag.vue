<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :osomeURL="this.osomeURL" :officialURL="this.officialURL" :header="this.header_text" />
        <div class="container-fluid px-4">
            <h1 class="mt-4">Hashtags <span class="subtitle">- Metadata</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Retrieve detailed metadata information for hashtags with the given keyword.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Statuses hashtag metadata -<router-link to="/apidocumentation#api-8" target="_blank" class="api-documentation">Documentation</router-link>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-6">
                                    <label for="mastodonInstance">Mastodon Instances</label>
                                    <VueMultiselect
                                        aria-labelledby="mastodonInstance"
                                        v-model="selectedMastodonInstances"
                                        v-bind:class="{'is-invalid': instanceIdError !== ''}"
                                        :options="instanceData"
                                        :multiple="true"
                                        :taggable="true"
                                        @tag="addMastodonInstance"
                                        tag-placeholder="Add as a new instance"
                                        placeholder="Type to search or add"
                                        label="name"
                                        track-by="name"
                                        role="textbox"
                                        :style="{ width: '100%', height: '50%' }"
                                    />
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label for="keyword">Keyword</label>
                                    <input
                                        id="keyword"
                                        v-model="searchKeyword"
                                        :class="{'form-control': true, 'is-invalid': searchKeywordError !== ''}"
                                        @blur="searchKeywordBlurred = true"
                                        placeholder="Hashtag keyword"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchKeywordError !== ''" class="invalid-feedback">{{ searchKeywordError }}</div>
                                </div>
                                <div class="col-xl-3" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" @click="submitStatusSearch">Search</button>
                                </div>
                                <div class="row" style="margin-top: 23px;" v-if="!loading && downloadData.length">
                                    <div class="col-md-12 text-right">
                                        <button type="button" class="btn btn-warning" @click="downloadAccountJSON" style="margin-right: 20px">Download JSON</button>
                                        <button type="button" class="btn btn-primary" @click="showModal">Show URL</button> <!-- Correct the @click binding -->
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
            <div class="table-responsive" v-if="!loading && hashtagData.length>0" style="font-size: 10px;">
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th scope="col">Hashtag Name</th>
                            <th scope="col">Instance Name</th>
                            <th scope="col">URL</th>
                        </tr>
                    </thead>
                    <tbody>
                    <tr v-for="hashtag in hashtagData" :key="key">
                        <td>{{hashtag.name}}</td>
                        <td>{{ getDomain(hashtag.url) }}</td>
                        <td><a :href="hashtag.url" target="_blank" style="text-underline: #0a53be">Link</a></td>
                    </tr>
                    </tbody>
                </table>
            </div>
            <div class="alert alert-warning" v-if="!hashtagData.length && this.searched">
                <fa icon="exclamation-triangle" /> No data available.
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
import Modal from "../components/Modal.vue";
import VueMultiselect from 'vue-multiselect'

export default {
    name: 'searchHashtags',
    components: {
        HollowDotsSpinner,
        Modal,
        VueMultiselect
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
            instanceIdError: "",
            modalIsOpen: false,
            osomeURL: "",
            officialURL: "",
            header_text: "",
            searched: false,
            selectedMastodonInstances: [],
        }
    },
    watch: {
        selectedMastodonInstances: function (newInstances) {
            // Check if the array is not empty, reset the error
            if (newInstances.length > 0) {
                this.instanceIdError = '';
            }
        },
    },
    methods: {
        successShowToast(message){
            toast.success(message, {
                autoClose: 8000,
            })
        },
        errorShowToast(){
            toast.error('Error in retrieving data!', {
                autoClose: 8000,
            })
        },
        isValidKeyword(keyword) {
            return keyword.trim() !== '';
        },
        isValidInstance(instanceArray) {
            return instanceArray.length >= 1;
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

            if (!this.isValidInstance(this.selectedMastodonInstances)) {
                this.instanceIdError = "Please add one or more Mastodon instances";
            }

            if (!this.isValidKeyword(this.searchKeyword)) {
                this.searchKeywordError = "Keyword is required";
            }

            if(this.isValidKeyword(this.searchKeyword) && this.isValidInstance(this.selectedMastodonInstances)) {
                this.header_text = "Search Statuses URL"
                this.loading = true;

                let dataUrl = constants.url + '/api/search-hashtag-by-keyword';
                let requestData = {
                    keyword: this.searchKeyword,
                    instances: this.selectedMastodonInstances,
                };

                let jsonData = JSON.stringify(requestData);
                this.officialURL = "https://"+this.selectedMastodonInstances[0].name+"/api/v2/search?q="+this.searchKeyword+"&type=hashtags"
                this.osomeURL = `curl -X POST -H "Content-Type: application/json" -d '${jsonData}' "https://osome.iu.edu/tools/mastodon/api/search-hashtag-by-keyword"`;

                axios.post(dataUrl, requestData)
                    .then(res => {
                        let data_received = res.data;

                        // Assuming res.data is an array containing hashtag data
                        for (let data of data_received) {
                            for (let j=0;j<data.hashtags.length; j++){
                                this.hashtagData.push(data.hashtags[j]);
                            }
                        }

                        this.downloadData = this.hashtagData;
                        this.loading = false;


                        let message = this.hashtagData.length + " data retrieved";
                        this.successShowToast(message);
                    })
                    .catch(error => {
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
        },
        closeModal() {
            this.modalIsOpen = false;
        },
        showModal() {
            this.modalIsOpen = true;
        },
        addMastodonInstance (newInstance) {
            const mastodonInstance = {
                name: newInstance
            }
            this.instanceData.push(mastodonInstance)
            this.selectedMastodonInstances.push(mastodonInstance)
        },
        getDomain(url) {
            try {
                return new URL(url).hostname;
            } catch (error) {
                console.error("Invalid URL:", url);
                return "";
            }
        }
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>