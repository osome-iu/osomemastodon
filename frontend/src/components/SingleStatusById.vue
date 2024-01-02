<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :osomeURL="this.osomeURL" :officialURL="this.officialURL" :header="this.header_text"/>
        <div class="container-fluid px-4">
            <h1 class="page-title">Statuses <span class="subtitle">- Single Status by Id</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Obtain information about a status by status Id.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Search a single status by Id - <router-link to="/apidocumentation#api-5" target="_blank" class="api-documentation">Documentation</router-link>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-4">
                                    <label>Mastodon Instance</label>
                                    <VueMultiselect
                                        v-model="selectedMastodonInstances"
                                        :options="instanceData"
                                        :taggable="true"
                                        @tag="addMastodonInstance"
                                        tag-placeholder="Add as a new instance"
                                        placeholder="Type to search or add"
                                        label="name"
                                        track-by="name"
                                        :style="{ width: '100%', height: '50%' }"
                                    />
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Status Id</label>
                                    <input
                                        v-model="statusId"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchStatusIdError !== ''}"
                                        v-on:blur="searchStatusIdBlurred = true"
                                        placeholder="Status ID"
                                    />
                                    <div v-if="searchStatusIdError !== ''" class="invalid-feedback">{{ searchStatusIdError }}</div>
                                </div>
                                <div class="col-xl-4" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitSingleStatus" style="margin-right: 20px">Search</button>
                                </div>
                                <div class="row" style="margin-top: 23px;" v-if="!loading && statusContent">
                                    <div class="col-md-12 text-right">
                                        <button type="button" class="btn btn-warning" @click="downloadJSON" style="margin-right: 20px">Download JSON</button>
                                        <button type="button" class="btn btn-primary" :onclick="showModal" >Show URL</button>
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
                    <div class="card mb-4" v-if="this.statusReceivedId">
                        <div class="card-header">
                            <i class="fas fa-table me-1"></i>
                            Status Data
                        </div>
                        <div class="card-body">
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2" >
                                    Status Id  :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Display Name" v-model="this.statusReceivedId" aria-label="Search for..." aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2" >
                                    Instance  :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Instance Name" v-model="this.instanceName" aria-label="Search for..." aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Status Content :
                                </div>
                                <div class="col-xl-5">
                                    <div class="form-control" v-html="this.statusContent" style="font-size: 10px;" id="readonly-textbox"></div>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Reply to account Id :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="In reply to account Id" v-model="this.inReplyToAccountId" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Reblog Status:
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Reblog Status" v-model="this.statusReblog" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Reblog Count :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Reblog Count" v-model="this.statusReblogCount" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Replies Count :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Replies Count" v-model="this.statusReplyCount" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px">
                                <div class="col-xl-2">
                                    Sensitive Data :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Sensitive Data" v-model="this.statusSensitiveData" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px"> <!-- Center the first row -->
                                <div class="col-xl-2" >
                                    Visibility :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Status Visibility" v-model="this.statusVisibility" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px"> <!-- Center the first row -->
                                <div class="col-xl-2" >
                                    Status Created At :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Status Created At" v-model="this.statusCreatedAt" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                            <div class="row justify-content-center" style="margin-top: 10px"> <!-- Center the first row -->
                                <div class="col-xl-2" >
                                    Status Updated At :
                                </div>
                                <div class="col-xl-5">
                                    <input class="form-control" type="text" placeholder="Status Edited At" v-model="this.statusEditedAt" aria-describedby="btnNavbarSearch" readonly/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="alert alert-warning" v-if="singleStatusData.length && this.searched">
                <fa icon="exclamation-triangle" /> No data available.
            </div>
        </div>
    </main>
</template>

<script>
import axios from "axios";
import * as constants from "@/shared/Constants";
import Modal from "@/components/Modal.vue";
import {HollowDotsSpinner} from "epic-spinners";
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import VueMultiselect from 'vue-multiselect'

export default {
    name: 'SearchByIdStatus',
    components: {
        Modal,
        HollowDotsSpinner,
        VueMultiselect
    },
    data() {
        return {
            singleStatusData: [],
            clientSecret: null,
            token: null,
            instanceData:[],
            instanceId: "",
            statusId: "",
            statusReceivedId: "",
            statusContent: "",
            inReplyToAccountId: "",
            statusEmojis: "",
            statusFavoriteCount: "",
            statusReblog: "",
            statusReblogCount: "",
            statusReplyCount: "",
            statusVisibility: "",
            statusMentions: [],
            statusAccountId: "",
            statusTags: [],
            statusSensitiveData: "",
            statusPoll: "",
            statusCreatedAt: "",
            statusEditedAt: "",
            instanceName: "",
            searchStatusId: false,
            searchStatusIdBlurred: false,
            instanceIdBlurred: false,
            searchStatusIdError: "",
            instanceIdError: "",
            modalIsOpen: false,
            loading: false,
            searched:false,
            selectedMastodonInstances: [],
            osomeURL: "",
            officialURL: "",
        }
    },
    methods: {
        isValidStatusId(statusId) {
            return statusId.trim() !== '';
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
        submitSingleStatus(){
            this.searchStatusIdError = "";
            this.instanceIdError = "";

            if (!this.isValidStatusId(this.statusId)) {
                this.searchStatusIdError = "A keyword is required";
            }

            if(this.isValidStatusId(this.statusId)) {
                this.loading = true;
                this.officialURL = "https://"+this.selectedMastodonInstances.name+"/api/v1/statuses/"+this.statusId;
                this.osomeURL = constants.url + '/api/search-status-by-id?status_id=' + this.statusId + '&mastodon_instance=' + this.selectedMastodonInstances.name;
                this.header_text = "Search Account URL"
                let dataUrl = constants.url + '/api/search-status-by-id?status_id=' + this.statusId + '&mastodon_instance=' + this.selectedMastodonInstances.name;
                axios.get(dataUrl)
                    .then(res => {
                        this.searched = true;
                        this.singleStatusData = res;
                        this.statusReceivedId = res.data.id;
                        this.statusContent = res.data.content;
                        this.inReplyToAccountId = res.data.in_reply_to_account_id;
                        this.statusReblog = res.data.reblog;
                        this.statusReblogCount = res.data.reblogs_count;
                        this.statusReplyCount = res.data.replies_count;
                        this.statusSensitiveData = res.data.sensitive;
                        this.statusVisibility = res.data.visibility;
                        this.statusCreatedAt = res.data.created_at;
                        this.statusEditedAt = res.data.edited_at;
                        this.instanceName = this.extractURLtoGetInstanceName(res.data.url);
                        let message = "Data retrieved successfully."
                        this.successShowToast(message)
                        this.loading = false;
                    }).catch(error => {
                    console.log(error);
                    this.singleStatusData = []
                    this.errorShowToast();
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
            const blob = new Blob([JSON.stringify(this.singleStatusData)], { type: 'application/json' });

            // Create a download link
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'status_data-'+this.statusId+'.json';

            // Append the link to the document and trigger the click event
            document.body.appendChild(a);
            a.click();

            // Remove the link from the document
            document.body.removeChild(a);
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
        errorShowToast(){
            toast.error('Error in retrieving data!', {
                autoClose: 3000,
            })
        },
        successShowToast(message){
            toast.success(message, {
                autoClose: 3000,
            })
        },
        addMastodonInstance (newInstance) {
            const mastodonInstance = {
                name: newInstance
            }
            this.instanceData.push(mastodonInstance)
            this.selectedMastodonInstances.push(mastodonInstance)
        },
    },
    mounted() {
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
