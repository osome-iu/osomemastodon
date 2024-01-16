<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :officialURL="this.officialURL" :osomeURL="this.osomeURL" :header="this.header_text"/>
        <div class="container-fluid px-4">
            <h1 class="page-title">Statuses <span class="subtitle">- Search by keyword</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Search for statuses for a given keyword. This function allows to search across multiple instances with given keyword. </p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Statuses search by keyword - <router-link to="/apidocumentation#api-2" target="_blank" class="api-documentation">Documentation</router-link>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-4">
                                    <label for="mastodonInstance" id="mastodonInstance">Mastodon Instances</label>
                                    <VueMultiselect
                                        aria-labelledby="mastodonInstance"
                                        v-model="selectedMastodonInstances"
                                        v-bind:class="{'is-invalid': instanceIdError !== ''}"
                                        :options="instanceData"
                                        :multiple="true"
                                        :taggable="true"
                                        @tag="addMastodonInstance"
                                        @remove="removeMastodonInstance"
                                        tag-placeholder="Add as a new instance"
                                        placeholder="Type to search or add"
                                        label="name"
                                        track-by="name"
                                        role="textbox"
                                        :style="{ width: '100%', height: '50%' , color: 'black'}"
                                    />
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-2">
                                    <label for="keyword">Keyword</label>
                                    <input
                                        v-model="searchKeyword"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchKeywordError !== ''}"
                                        placeholder="Status keyword"
                                        v-on:blur="searchKeywordBlurred = true"
                                        @input="keywordInputChanged"
                                        id="keyword"
                                    />
                                    <div v-if="searchKeywordError !== ''" class="invalid-feedback">{{ searchKeywordError }}</div>
                                </div>
                                <div class="col-md-3" style="margin-top: 30px; margin-left: 20px;">
                                    <input type="checkbox" id="checkbox" v-model="checkMastodonInstance" @input="changeCheckMastodonInstance"/>
                                    <label for="checkbox">&nbsp;Check instance validity &nbsp;<router-link to="/faq#q-3" target="_blank" aria-label="Check instance validity" ><i class="fas fa-info-circle"></i></router-link></label>
                                </div>
                                <div class="col-xl-1" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitStatusSearch" >Search</button>
                                </div>
                            </div>
                            <div v-if="selectedMastodonInstances.length">
                                <div class="row" style="margin-top: 20px; font-weight: bold;">
                                    <p style="text-decoration: underline;" >Access Tokens <router-link to="/faq" target="_blank"><i class="fas fa-info-circle"></i></router-link></p>
                                </div>
                                <div class="row" v-for="(mastodonInstance, index) in selectedMastodonInstances" :key="index" style="margin-top:10px;">
                                    <div class="col-md-2" style="margin-top:5px;">
                                        <p>{{ mastodonInstance.name }}</p>
                                    </div>
                                    <div class="col-xl-4">
                                        <input
                                            v-model="accessTokenArray[index]"
                                            v-bind:class="{'form-control': true,}"
                                            placeholder="Access Token"
                                            @input="accessTokenInputChangedArray(index)"
                                        />
                                        <div v-if="accessTokenErrorArray[index] !== ''" class="invalid-feedback">{{ accessTokenErrorArray[index] }}</div>
                                    </div>
                                    <div class="col-xl-5">
                                        <button type="button" class="btn btn-danger" @click="removeMastodonInstanceFromBtn(index)" >Remove</button>
                                    </div>
                                </div>
                            </div>
                            <div class="row" style="margin-top: 23px;" v-if="!loading && statusData.length">
                                <div class="col-md-12 text-right">
                                    <button type="button" class="btn btn-warning" @click="downloadAccountJSON" style="margin-right: 20px">Download JSON</button>
                                    <button type="button" class="btn btn-primary" :onclick="showModal" >Show URL</button>
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
            <div class="table-responsive" v-if="!loading && statusData.length>0" style="font-size: 12px;">
                <table class="table table-bordered">
                    <thead>
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Instance Name</th>
                        <th scope="col">Content</th>
                        <th scope="col">In reply to Acc Id</th>
                        <th scope="col">In reply to Id</th>
                        <th scope="col">Created At </th>
                        <th scope="col">Mentions </th>
                        <th scope="col">Tags </th>
                        <th scope="col" v-if="checkMastodonInstance">Instance? </th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="status in statusData">
                        <td>{{status.id}}</td>
                        <td>{{extractURLtoGetInstanceName(status.url)}}</td>
                        <td><div v-html="this.sanitizeHtml(status.content)" ></div></td>
                        <td>{{status.in_reply_to_account_id}}</td>
                        <td>{{status.in_reply_to_id}}</td>
                        <td>{{status.created_at}}</td>
                        <td>
                            <span v-for="(mention, index) in status.mentions">
                                <a :href="mention.url" target="_blank" style="text-underline: #0a53be">{{mention.username}}</a>
                                <span v-if="index < status.mentions.length - 1">, </span>
                            </span>
                        </td>
                        <td>
                            <span v-for="(tag, index) in status.tags">
                                <a :href="tag.url" target="_blank" style="text-underline: #0a53be">{{tag.name}}</a>
                                <span v-if="index < status.tags.length - 1">, </span>
                            </span>
                        </td>
                        <td v-if="checkMastodonInstance">{{ status.mastodon_instance }}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
            <div class="alert alert-warning" v-if="statusData.length === 0 && this.searched">
                <fa icon="exclamation-triangle" /> No data available.
            </div>
        </div>
    </main>
</template>

<script>
import axios from "axios";
import * as constants from "@/shared/Constants";
import { HollowDotsSpinner } from 'epic-spinners';
import DOMPurify from 'dompurify';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import Modal from "../components/Modal.vue";
import VueMultiselect from "vue-multiselect";


export default {
    name: 'searchStatus',
    components: {
        HollowDotsSpinner,
        Modal,
        VueMultiselect
    },
    data() {
        return {
            token: null,
            instanceData:[],
            instanceId: "",
            searchKeyword: "",
            searchType: "",
            statusData: [],
            showDownloadBtn: "",
            loading: false,
            downloadData: [],
            searchKeywordBlurred: false,
            instanceIdBlurred: false,
            searchKeywordError: "",
            instanceIdError: "",
            accessTokenBlurred: false,
            accessTokenError: "",
            modalIsOpen: false,
            officialURL: "",
            osomeURL: "",
            header_text: "",
            searched: false,
            checkMastodonInstance : false,
            selectedMastodonInstances: [],
            accessTokenArray: [], // Array to store access tokens
            accessTokenErrorArray: [], // Array to store access token errors
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
        sanitizeHtml(htmlsending) {
            return DOMPurify.sanitize(htmlsending);
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
        accessTokenInputChangedArray(index){
            const accessToken = this.accessTokenArray[index];

            // Check if the access token is empty
            if (!accessToken.trim()) {
                this.accessTokenErrorArray[index] = 'Access Token cannot be empty';
            } else {
                this.accessTokenErrorArray[index] = ''; // Clear the error if not empty
            }
        },
        viewAccountInfo(accountId){
            this.$router.push({
                name: 'Accounts',  // Assuming you have a route name
                params: { accountId: accountId, instanceId: this.instanceId},
            });
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
            this.accessTokenError = "";
            this.searched = false;

            if (!this.isValidInstance(this.selectedMastodonInstances)) {
                this.instanceIdError = "Please add one or more Mastodon instances";
            }

            if (!this.isValidKeyword(this.searchKeyword)) {
                this.searchKeywordError = "Keyword is required";
            }

            if(this.isValidKeyword(this.searchKeyword) && this.isValidInstance(this.selectedMastodonInstances)) {
                this.statusData = [];
                this.downloadData = [];
                this.header_text = "Search Statuses URL"
                this.loading = true;
                let dataUrl = constants.url + '/api/search-status-by-keyword';


                let requestData = {
                    mastodon_instances: this.selectedMastodonInstances,
                    keyword: this.searchKeyword,
                    access_tokens: this.accessTokenArray
                };

                let jsonData = JSON.stringify(requestData);

                this.osomeURL = `curl -X POST -H "Content-Type: application/json" -d '${jsonData}' "https://osome.iu.edu/tools/mastodon/api/search-status-by-keyword"`;
                this.officialURL = "curl --location 'https://"+this.selectedMastodonInstances[0].name+"/api/v2/search?q="+this.searchKeyword+"&type=statuses' --header 'Authorization: Bearer '" + this.accessTokenArray[0];

                axios.post(dataUrl, requestData)
                    .then(async res => {
                        let data_received = res.data;
                        if(this.checkMastodonInstance){
                            //Assuming res.data is an array containing hashtag data
                            for (let data of data_received) {
                                const mastodonInstanceResult = await this.checkIfMastodonInstance(data.searched_status)
                                this.statusData = this.statusData.concat(mastodonInstanceResult);
                            }
                        }else{
                            for (let data of data_received) {
                                for (let j = 0; j < data.searched_status.statuses.length; j++) {
                                    this.statusData.push(data.searched_status.statuses[j]);
                                }
                            }
                        }
                        this.downloadData = this.statusData;
                        this.loading = false;
                        let message = this.statusData.length + " data retrieved";
                        this.successShowToast(message);
                    })
                    .catch(error => {
                        this.errorShowToast();
                        this.loading = false;
                        console.log(error);
                    });
            }
        },
        async checkIfMastodonInstance(statusData) {
            const updatedStatusData = [];

            for (let status of statusData.statuses) {
                let serverName = this.extractURLtoGetInstanceName(status.url);
                const apiURL = `https://${serverName}/api/v1/instance`;

                try {
                    const response = await fetch(apiURL, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                    });

                    if (response.ok) {
                        const responseData = await response.json();
                        // Assuming you want to add the API response data to each status
                        const updatedStatus = { ...status, "mastodon_instance": "Yes" };
                        updatedStatusData.push(updatedStatus);
                    } else {
                        console.error(`Error: ${response.status} - ${response.statusText}`);
                        // Assuming you want to add an error message to each status in case of an error
                        const updatedStatus = { ...status, "mastodon_instance": "No" };
                        updatedStatusData.push(updatedStatus);
                    }
                } catch (error) {
                    console.error('Error during API request:', error);
                    // Assuming you want to add an error message to each status in case of an error
                    const updatedStatus = { ...status, "mastodon_instance": "No" };
                    updatedStatusData.push(updatedStatus);
                }
            }
            return updatedStatusData;
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

            a.download = 'status_data-'+this.searchKeyword+'.json';

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
        changeCheckMastodonInstance(){
            this.statusData = []
        },
        addMastodonInstance (newInstance) {
            const mastodonInstance = {
                name: newInstance
            }
            this.instanceData.push(mastodonInstance)
            this.selectedMastodonInstances.push(mastodonInstance)
        },
        removeMastodonInstance(removedItem) {
            // Find the index of the removed item
            const index = this.selectedMastodonInstances.findIndex(item => item === removedItem);

            // Remove the corresponding elements from accessTokenArray and accessTokenErrorArray
            this.accessTokenArray.splice(index, 1);
            this.accessTokenErrorArray.splice(index, 1);
        },
        removeMastodonInstanceFromBtn(index){
            console.log(index)
            // Remove the element at the specified index from both arrays
            this.selectedMastodonInstances.splice(index, 1);
            this.accessTokenArray.splice(index, 1);
            this.accessTokenErrorArray.splice(index, 1);
        }
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>