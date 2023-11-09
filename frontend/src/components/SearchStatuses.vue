<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :url="this.api_call" :header="this.header_text"/>
        <div class="container-fluid px-4">
            <h1 class="page-title">Statuses <span class="subtitle">- Search by keyword</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Search for Statuses.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Statuses search by keyword - <a href="https://docs.joinmastodon.org/methods/search/" target="_blank" class="black-link">Documentation</a>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-2">
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
                                <div class="col-xl-3">
                                    <label for="keyword">Keyword</label>
                                    <input
                                        v-model="searchKeyword"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchKeywordError !== ''}"
                                        placeholder="Keyword"
                                        v-on:blur="searchKeywordBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchKeywordError !== ''" class="invalid-feedback">{{ searchKeywordError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Access Token <router-link to="/faq" target="_blank"><i class="fas fa-info-circle"></i></router-link></label>
                                    <input
                                        v-model="accessToken"
                                        v-bind:class="{'form-control': true, 'is-invalid': accessTokenError !== ''}"
                                        v-on:blur="accessTokenBlurred = true"
                                        placeholder="Access Token"
                                        @input="accessTokenInputChanged"
                                    />
                                    <div v-if="accessTokenError !== ''" class="invalid-feedback">{{ accessTokenError }}</div>
                                </div>
                                <div class="col-xl-3" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitStatusSearch" >Search</button>
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
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="status in statusData" :key="key">
                        <td>{{status.id}}</td>
                        <td>{{extractURLtoGetInstanceName(status.url)}}</td>
                        <td><div v-html="this.sanitizeHtml(status.content)" ></div></td>
                        <td>{{status.in_reply_to_account_id}}</td>
                        <td>{{status.in_reply_to_id}}</td>
                        <td>{{status.created_at}}</td>
                        <td>
                            <span v-for="(mention, index) in status.mentions" :key="index">
                                <a :href="mention.url" target="_blank" style="text-underline: #0a53be">{{mention.username}}</a>
                                <span v-if="index < status.mentions.length - 1">, </span>
                            </span>
                        </td>
                        <td>
                            <span v-for="(tag, index) in status.tags" :key="index">
                                <a :href="tag.url" target="_blank" style="text-underline: #0a53be">{{tag.name}}</a>
                                <span v-if="index < status.tags.length - 1">, </span>
                            </span>
                        </td>
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

export default {
    name: 'searchStatus',
    components: {
        HollowDotsSpinner,
        Modal
    },
    data() {
        return {
            accessToken: "",
            token: null,
            instanceData:[],
            instanceId: "",
            searchKeyword: "",
            searchType: "",
            survey_json: "",
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
            api_call: "",
            header_text: "",
            searched: false,
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
        isValidAccessToken(accessToken) {
            return accessToken.trim() !== '';
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
        accessTokenInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.accessTokenError = ""
                this.accessTokenBlurred = false;
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

            if (!this.isValidInstance(this.instanceId)) {
                this.instanceIdError = "Mastodon instance is required";
            }

            if (!this.isValidKeyword(this.searchKeyword)) {
                this.searchKeywordError = "Keyword is required";
            }

            if (!this.isValidAccessToken(this.accessToken)) {
                this.accessTokenError = "Access token is required";
            }
            if(this.isValidInstance(this.instanceId) && this.isValidKeyword(this.searchKeyword) && this.isValidAccessToken(this.accessToken)) {
                this.api_call = "curl --location 'https://"+this.instanceId+"/api/v2/search?q="+this.searchKeyword+"&type=statuses' --header 'Authorization: Bearer '" + this.accessToken;
                this.header_text = "Search Statuses URL"
                this.loading = true;
                let dataUrl = constants.url + '/api/search-status-by-keyword?keyword=' + this.searchKeyword + '&mastodon_instance=' + this.instanceId + '&type=statuses&client_key=' + this.accessToken;
                axios.get(dataUrl)
                    .then(res => {
                        this.searched = true;
                        this.singleStatusData = res;
                        this.show_json = true;
                        this.survey_json = this.stringifyJSON(this.singleStatusData)
                        this.statusData = res.data.statuses;
                        this.downloadData = this.statusData
                        this.loading = false;
                        let message = this.statusData.length +" data retrieved"
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
        }
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>

