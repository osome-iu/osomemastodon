<template>
    <div>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :url="this.api_call" />
        <div class="container-fluid px-4">
            <h1 class="mt-4">Accounts</h1>
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
                            Search by keyword - <a href="https://docs.joinmastodon.org/methods/search/" target="_blank">Documetation</a>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-4">
                                    <label>Mastodon Instance</label><button id="button_text" :onclick="applymanuallyClick"></button>
                                    <button id="button_text" :onclick="applymanuallyClick" v-if="applymanually"> choose</button>
                                    <select
                                        v-model="instanceId"
                                        class="form-control"
                                        v-bind:class="{'is-invalid': instanceIdError !== ''}"
                                        v-on:blur="instanceIdBlurred = true"
                                        v-if="!applymanually"
                                        @input="instanceInputChanged"
                                    >
                                        <option disabled value="">Choose an instance</option>
                                        <option v-for="item in instanceData" :key="item.name" :value="item.name">{{ item.name }}</option>
                                    </select>
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback" >{{ instanceIdError }}</div>
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
                    <div class="card-body">
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
                                    <td>{{account.display_name}}</td>
                                    <td>{{account.username}}</td>
                                    <td>{{this.extractInstanceName(account.acct)}}</td>
                                    <td>{{account.followers_count}}</td>
                                    <td>{{account.following_count}}</td>
                                    <td>{{account.statuses_count}}</td>
                                    <td><button type="button" class="btn btn-primary btn-sm" @click="viewAccountInfo(account.id)">view</button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="alert alert-warning" v-if="instanceData.length === 0 & !loading">
                            No data available.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import * as constants from "@/shared/Constants";
import { HollowDotsSpinner } from 'epic-spinners';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css'
import Modal from "../components/Modal.vue";

export default {
    name: 'accounts',
    components: {
        HollowDotsSpinner,
        Modal
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
            accountsData: "",
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
            api_call: "",
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
        applymanuallyClick(){
            this.instanceId = "";
            if(this.applymanually){
                this.applymanually = false;
                return
            }
            this.applymanually = true
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

            if (!this.isValidInstance(this.instanceId)) {
                this.instanceIdError = "Please apply a valid Mastodon instance";
            }

            if (!this.isValidKeyword(this.searchKeyword)) {
                this.searchKeywordError = "A keyword is required";
            }

            if(this.isValidInstance(this.instanceId) && this.isValidKeyword(this.searchKeyword)) {
                this.api_call = "https://mastodon.social/api/v2/search?q="+this.searchKeyword+"&type=accounts"
                this.loading = true;
                this.singleStatusData = []
                let dataUrl = constants.url + '/api/search-status-by-keyword?keyword=' + this.searchKeyword + '&mastodon_instance=' + this.instanceId + '&type=accounts';
                axios.get(dataUrl)
                    .then(res => {
                        this.singleStatusData = res;
                        this.accountsData = res.data.accounts;
                        this.downloadData = this.accountsData;
                        this.loading = false;
                        let message = this.accountsData.length +" data retrieved"
                        this.successShowToast(message)
                    }).catch(error => {
                    this.errorShowToast();
                    this.loading = false;
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
        }
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>

<style scoped>
/* Add some basic styles to remove default button styles */
#button_text {
    background: none;
    border: none;
    padding: 0;
    font-family: inherit;
    cursor: pointer;
    text-decoration: underline; /* Add underline to text */
    color: blue; /* Set the color of the text */
}

</style>