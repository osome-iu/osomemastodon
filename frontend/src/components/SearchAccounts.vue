<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :osomeURL="this.osomeURL" :officialURL="this.officialURL" :header="this.header_text" />
        <div class="container-fluid px-4">
            <h1 class="page-title">Accounts <span class="subtitle">- Search by keyword</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Search for content in accounts.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Search accounts by keyword - <a href="https://docs.joinmastodon.org/methods/search/" target="_blank" class="black-link">Documentation</a>
                        </div>
                        <div class="card-body">
                            <div a class="row">
                                <div class="col-xl-6">
                                    <label class="typo__label">Mastodon Instances</label>
                                    <VueMultiselect
                                        v-model="selectedMastodonInstances"
                                        :options="instanceData"
                                        :multiple="true"
                                        :taggable="true"
                                        @tag="addMastodonInstance"
                                        tag-placeholder="Add as a new instance"
                                        placeholder="Type to search or add"
                                        label="name"
                                        track-by="name"
                                        :style="{ width: '100%', height: '40%' }"
                                    />
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-4">
                                    <label for="keyword">Keyword</label>
                                    <input
                                        v-model="searchKeyword"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchKeywordError !== ''}"
                                        v-on:blur="searchKeywordBlurred = true"
                                        placeholder="Keyword"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchKeywordError !== ''" class="invalid-feedback">{{ searchKeywordError }}</div>
                                </div>
                                <div class="col-xl-1" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitAccountSearch" >Search</button>
                                </div>
                                <div class="row" style="margin-top: 23px;" v-if="!loading && downloadData.length">
                                    <div class="col-md-12 text-right">
                                        <button type="button" class="btn btn-warning" @click="downloadAccountJSON" style="margin-right: 20px">Download JSON</button>
                                        <button type="button" class="btn btn-primary" :onclick="showModal" >Show URL</button>
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
            <div class="table-responsive" v-if="!loading && accountsData.length>0" style="font-size: 12px;">
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th scope="col">ID</th>
                            <th scope="col">Display Name</th>
                            <th scope="col">Username</th>
                            <th scope="col">Instance</th>
                            <th scope="col">Followers Count</th>
                            <th scope="col">Following Count</th>
                            <th scope="col">Status Count </th>
                            <th scope="col">Profile Info </th>
                        </tr>
                    </thead>
                        <tbody>
                            <tr v-for="account in accountsData" :key="key">
                                <td>{{account.id}}</td>
                                <td>{{account.display_name}}</td>
                                <td>{{account.username}}</td>
                                <td>{{this.extractInstanceName(account.acct)}}</td>
                                <td>{{account.followers_count}}</td>
                                <td>{{account.following_count}}</td>
                                <td>{{account.statuses_count}}</td>
                                <td><button type="button" class="btn btn-primary btn-sm" @click="viewAccountInfo(account.id,this.extractInstanceName(account.acct) )">view</button></td>
                            </tr>
                        </tbody>
                </table>
            </div>
            <div class="alert alert-warning" v-if="!accountsData.length && this.searched">
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
import vSelect from 'vue-select';
import 'vue-select/dist/vue-select.css';
import VueMultiselect from 'vue-multiselect'


export default {
    name: 'accounts',
    components: {
        HollowDotsSpinner,
        Modal,
        vSelect,
        VueMultiselect
    },
    data() {
        return {
            clientKey: null,
            clientSecret: null,
            token: null,
            instanceData:[],
            instanceId: "",
            searchKeyword: "",
            searchType: "",
            accountsData: [],
            showDownloadBtn: "",
            loading: false,
            downloadData: [],
            searchKeywordBlurred: false,
            instanceIdBlurred: false,
            searchKeywordError: "",
            instanceIdError: "",
            applymanually: false,
            mastodonsearchManual : "",
            modalIsOpen: false,
            osomeURL: "",
            officialURL: "",
            selectedItem: null,
            header_text: "",
            searched: false,
            selectedMastodonInstances: [],
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
        viewAccountInfo(accountId, instance_name){
            console.log(accountId)
            console.log(instance_name)
            this.$router.push({
                name: 'singleAccountById', // Assuming you have a route name
                params: { accountId: accountId, instanceId: instance_name},
            });
        },
        keywordInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.searchKeywordError = ""
                this.searchKeywordBlurred = false;
            }
        },
        instanceInputChanged(e){
            this.instanceId = e.target.value;
            let valueReceived = e.target.value;
            if(valueReceived){
                this.instanceIdError = ""
                this.instanceIdBlurred = false;
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
        submitAccountSearch(){
            this.searchKeywordError = "";
            this.instanceIdError = "";
            this.searched = false;

            if (!this.isValidInstance(this.instanceId)) {
                this.instanceIdError = "Please apply a valid Mastodon instance";
            }

            if (!this.isValidKeyword(this.searchKeyword)) {
                this.searchKeywordError = "A keyword is required";
            }

            if(this.isValidKeyword(this.searchKeyword)) {
                this.header_text = "Search Account URL"
                this.loading = true;

                let dataUrl = constants.url + '/api/search-accounts-by-keyword';
                let requestData = {
                    keyword: this.searchKeyword,
                    instances: this.selectedMastodonInstances,
                };

                let jsonData = JSON.stringify(requestData);
                this.officialURL = "https://"+this.selectedMastodonInstances[0].name+"/api/v2/search?q="+this.searchKeyword+"&type=accounts"
                this.osomeURL = `curl -X POST -H "Content-Type: application/json" -d '${jsonData}' "https://osome.iu.edu/tools/mastodon/api/search-accounts-by-keyword"`;

                axios.post(dataUrl, requestData)
                    .then(res => {
                        let data_received = res.data;

                        // Assuming res.data is an array containing hashtag data
                        for (let data of data_received) {
                            for (let j=0;j<data.accounts.length; j++){
                                this.accountsData.push(data.accounts[j]);
                            }
                        }

                        this.downloadData = this.accountsData;
                        this.loading = false;

                        let message = this.accountsData.length + " data retrieved";
                        this.successShowToast(message);
                    })
                    .catch(error => {
                        this.loading = false;
                        this.errorShowToast();
                        console.log(error);
                    });
            }
            this.accountsData = []
            this.downloadData = []
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
            if(this.accountsData.length > 0){
                a.download = 'Account_details-'+this.searchKeyword+'.json';
            }
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
                name: newInstance,
                active_users: "",
                all_users: ""
            }
            this.instanceData.push(mastodonInstance)
            this.selectedMastodonInstances.push(mastodonInstance)
        },
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

