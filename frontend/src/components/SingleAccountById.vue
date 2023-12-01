<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :officialURL="this.officialURL" :osomeURL="this.osomeURL" :header="this.header_text"/>
        <div class="container-fluid px-4">
            <h1 class="page-title">Accounts <span class="subtitle">- Single Account by Id</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>View information about a profile.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Search accounts by Id - <a href="https://docs.joinmastodon.org/methods/accounts" target="_blank" class="black-link">Documentation</a>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-5">
                                    <label>Mastodon Instance</label>
                                    <VueMultiselect
                                        v-model="selectedMastodonInstances"
                                        :options="instanceData"
                                        :taggable="false"
                                        @tag="addMastodonInstance"
                                        tag-placeholder="Add as a new instance"
                                        placeholder="Type to search or add"
                                        label="name"
                                        track-by="name"
                                        :style="{ width: '100%', height: '40%' }"
                                    />
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Account Id</label>
                                    <input
                                        v-model="accountId"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="Account Id"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchAccountIdError !== ''" class="invalid-feedback">{{ searchAccountIdError }}</div>
                                </div>
                                <div class="col-xl-4" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitAccountSearch" >Search</button>
                                </div>
                            </div>
                            <div class="row" style="margin-top: 23px;" v-if="!loading && username">
                                <div class="col-md-12 text-right">
                                    <button type="button" class="btn btn-warning" @click="downloadJSON" style="margin-right: 20px">Download JSON</button>
                                    <button type="button" class="btn btn-primary" :onclick="showModal" >Show URL</button>
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
                    <div class="card mb-4" v-if="!loading && username">
                        <div class="card-header">
                            <i class="fas fa-table me-1"></i>
                            Account Information
                        </div>
                        <div class="card-body">
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2" >
                                    Display Name :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Display Name" v-model="this.displayName" aria-label="Search for..." aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Username :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Username" v-model="this.username" aria-describedby="btnNavbarSearch" readonly />
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Status Count :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Status Count" v-model="this.statusCount" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Followers count :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Followers Count" v-model="this.followersCount" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Following Count :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Following Count" v-model="this.followingCount" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Bot :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Bot" v-model="this.bot" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px"> <!-- Center the first row -->
                                <div class="col-xl-2" >
                                    Avatar URL :
                                </div>
                                <div class="col-xl-5">
                                    <a :href="avatarLink" target="_blank" style="text-underline: #0a53be">Open Link</a>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px"> <!-- Center the first row -->
                                <div class="col-xl-2" >
                                    Note :
                                </div>
                                <div class="col-xl-5">
                                    <div class="form-control" v-html="this.note" style="font-size: 10px;" id="readonly-textbox"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import axios from "axios";
import * as constants from "@/shared/Constants";
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css'
import Modal from "@/components/Modal.vue";
import VueMultiselect from 'vue-multiselect'
import {HollowDotsSpinner} from "epic-spinners";

export default {
    name: 'AccountsById',
    components: {Modal,VueMultiselect,HollowDotsSpinner},
    data() {
        return {
            clientKey: null,
            clientSecret: null,
            token: null,
            instanceData:[],
            accountData:[],
            instanceId: "",
            accountId: "",
            show_json: false,
            searchType: "",
            displayName: "",
            followersCount: "",
            followingCount: "",
            statusCount: "",
            lastStatusAt: "",
            username: "",
            bot: "",
            avatarLink: "",
            note: "",
            searchAccountId: false,
            searchAccountIdBlurred: false,
            instanceIdBlurred: false,
            searchAccountIdError: "",
            instanceIdError: "",
            modalIsOpen: false,
            modalTitle: 'Info',
            api_call: "",
            header_text: "Search Account by Id",
            selectedMastodonInstances: [],
            loading: false,
            officialURL: "",
            osomeURL:"",
            downloadData: []
        }
    },
    methods: {
        successShowToast(message){
            toast.success(message, {
                autoClose: 3000,
            })
        },
        errorShowToast(message){
            toast.error(message, {
                autoClose: 3000,
            })
        },
        isValidAccountId(accountId) {
            return accountId.trim() !== '';
        },
        isValidInstance(instanceId) {
            return instanceId.trim() !== '';
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
            this.searchAccountIdError = "";
            this.instanceIdError = "";

            if (!this.isValidAccountId(this.accountId)) {
                this.searchAccountIdError = "Account Id is required.";
            }

            if(this.isValidAccountId(this.accountId)) {
                this.loading = true;
                this.accountData = []
                this.clearAllFields();
                this.officialURL = 'https://'+this.selectedMastodonInstances.name+'/api/v1/accounts/'+this.accountId;
                this.osomeURL = constants.url + '/api/search-status-by-id?status_id=' + this.statusId + '&mastodon_instance=' + this.selectedMastodonInstances.name;
                let dataUrl = constants.url + '/api/account-search-by-id?mastodon_instance=' + this.selectedMastodonInstances.name + '&account_id=' + this.accountId;
                axios.get(dataUrl)
                    .then(res => {
                        this.accountData = res.data;
                        this.username = this.accountData.username;
                        this.displayName = this.accountData.display_name;
                        this.followersCount = this.accountData.followers_count;
                        this.followingCount = this.accountData.following_count;
                        this.statusCount = this.accountData.statuses_count;
                        this.bot = this.accountData.bot;
                        this.avatarLink = this.accountData.avatar;
                        this.note = this.accountData.note;
                        this.loading = false;
                        this.downloadData = res.data;
                        let message = "Account data retrieved successfully!"
                        this.successShowToast(message)
                    }).catch(error => {
                        this.loading = false;
                        console.log(error);
                        let message = "No data found or error in retrieving data!";
                        this.errorShowToast(message)
                });
            }
        },
        stringifyJSON(stringobject) {
            return JSON.stringify(stringobject, function (key, value) {
                return value;
            }, 4);
        },
        downloadJSON(){
            // Create a Blob containing the JSON data
            const blob = new Blob([JSON.stringify(this.downloadData)], { type: 'application/json' });

            // Create a download link
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'profile_data_'+this.username+'.json';

            // Append the link to the document and trigger the click event
            document.body.appendChild(a);
            a.click();

            // Remove the link from the document
            document.body.removeChild(a);
        },
        clearAllFields(){
            this.note = null,
            this.username = null,
            this.statusCount = null,
            this.followersCount= null,
            this.followingCount = null,
            this.bot = null,
            this.avatarLink = null,
            this.displayName = null
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
        closeModal() {
            this.modalIsOpen = false;
        },
        showModal() {
            this.modalIsOpen = true;
        },
        addMastodonInstance (newInstance) {
            this.fetchAllInstanceData();
            const mastodonInstance = {
                name: newInstance,
                active_users: "",
                all_users: ""
            }
            this.instanceData.push(mastodonInstance);
            this.selectedMastodonInstances.push(mastodonInstance);
        },
    },
    mounted() {
        const instanceId = this.$route.params.instanceId;
        if(instanceId){
            const mastodonInstance = {
                name: instanceId
            }
            this.instanceData.push(mastodonInstance);
            this.selectedMastodonInstances.push(mastodonInstance);
            this.accountId = this.$route.params.accountId;
        }
        this.fetchAllInstanceData();
    }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>
<style>
#readonly-textbox {
    background-color: #f2f2f2; /* Light gray background */
    border: 1px solid #ccc;   /* Light gray border */
    padding: 8px;             /* Some padding for better appearance */
    font-size: 14px;          /* Adjust font size */
    color: #333;              /* Text color */
}
</style>