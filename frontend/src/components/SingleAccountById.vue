<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :url="this.api_call" :header="this.header_text"/>
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
                            Search accounts by Id - <a href="https://docs.joinmastodon.org/methods/accounts/AccountById.vue" target="_blank" class="black-link">Documentation</a>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-5">
                                    <label>Mastodon Instance</label>
                                    <VueMultiselect
                                        v-model="selectedMastodonInstances"
                                        :options="instanceData"
                                        :multiple="true"
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
                        </div>
                    </div>
                    <div class="card mb-4">
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
                                <Modal :isOpen="modalIsOpen" @cancel="closeModal"/>
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
                            <div class="row justify-content-center" style="margin-top: 10px"> <!-- Center the first row -->
                                <div class="col-xl-2" >
                                    JSON :
                                </div>
                                <div class="col-xl-5">
                                    <button type="button" class="btn btn-primary" :onclick="downloadJSON">Download</button>
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

export default {
    name: 'AccountsById',
    components: {Modal,VueMultiselect},
    data() {
        return {
            clientKey: null,
            clientSecret: null,
            token: null,
            instanceData:[],
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
            header_text: "",
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
        // isValidAccountId(accountId) {
        //     return accountId.trim() !== '';
        // },
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
            console.log("This is calling......")
            this.searchAccountIdError = "";
            this.instanceIdError = "";

            // if (!this.isValidInstance(this.selectedMastodonInstances)) {
            //     this.instanceIdError = "Please choose a Mastodon instance.";
            // }

            // if (!this.isValidAccountId(this.accountId)) {
            //     this.searchAccountIdError = "Account Id is required.";
            // }

            // if(this.isValidAccountId(this.accountId)) {
                let dataUrl = constants.url + '/api/account-search-by-id?mastodon_instance=' + this.selectedMastodonInstances[0].name + '&account_id=' + this.accountId;
                this.clearAllFields()
                axios.get(dataUrl)
                    .then(res => {
                        this.accountData = res.data;
                        this.username = res.data.username;
                        this.displayName = res.data.display_name;
                        this.followersCount = res.data.followers_count;
                        this.followingCount = res.data.following_count;
                        this.statusCount = res.data.statuses_count;
                        this.bot = res.data.bot;
                        this.avatarLink = res.data.avatar;
                        this.note = res.data.note;
                        let message = "Account :" + this.displayName+ " retrieved successfully"
                        this.successShowToast(message)
                    }).catch(error => {
                        console.log(error);
                        let message = "Error in retrieving account : " + this.displayName;
                        this.errorShowToast(message)
                });
            // }
        },
        stringifyJSON(stringobject) {
            return JSON.stringify(stringobject, function (key, value) {
                return value;
            }, 4);
        },
        downloadJSON(){
            // Create a Blob containing the JSON data
            const blob = new Blob([JSON.stringify(this.accountData)], { type: 'application/json' });

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
        this.fetchAllInstanceData();
    },
    created() {
        this.accountId = this.$route.params.accountId;
        this.addMastodonInstance(this.$route.params.instanceId)

        if(this.selectedMastodonInstances.length < 0){
            this.selectedMastodonInstances = []
            this.accountId = ""
        } else{
            this.submitAccountSearch();
        }
    },
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