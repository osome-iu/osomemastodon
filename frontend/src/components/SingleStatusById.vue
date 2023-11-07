<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :url="this.api_call" :header="this.header_text"/>
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
                            Search a single status by Id - <a href="https://docs.joinmastodon.org/methods/statuses/#get" target="_blank" class="black-link">Documentation</a>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-3">
                                    <label>Mastodon Instance</label>
                                    <select
                                        v-model="instanceId"
                                        class="form-control"
                                        v-bind:class="{'is-invalid': instanceIdError !== ''}"
                                        v-on:blur="instanceIdBlurred = true"
                                    >
                                        <option disabled value="">Choose an instance</option>
                                        <option v-for="item in instanceData" :key="item.name" :value="item.name">{{ item.name }}</option>
                                    </select>
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
                                    <button type="button" class="btn btn-primary" :onclick="showModal" v-if="this.statusReceivedId">Show URL</button>
                                </div>
                            </div>
                        </div>
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
                            <div class="row justify-content-center" style="margin-top: 10px"> <!-- Center the first row -->
                                <div class="col-xl-2" >
                                    JSON :
                                </div>
                                <div class="col-xl-5">
                                    <button type="button" class="btn btn-primary" :onclick="downloadJSON" >Download</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row" v-if="show_json">
                <div class="col-xl-12">
                    <textarea class="form-control" v-model="survey_json" style="height:600px "></textarea>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import axios from "axios";
import * as constants from "@/shared/Constants";
import Modal from "@/components/Modal.vue";

export default {
    name: 'SearchByIdStatus',
    components: {Modal},
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

            if (!this.isValidInstance(this.instanceId)) {
                this.instanceIdError = "Please choose a Mastodon instance";
            }

            if (!this.isValidStatusId(this.statusId)) {
                this.searchStatusIdError = "A keyword is required";
            }

            if(this.isValidInstance(this.instanceId) && this.isValidStatusId(this.statusId)) {
                this.api_call = "https://"+this.instanceId+"/api/v1/statuses/"+this.statusId;
                this.header_text = "Search Account URL"

                let dataUrl = constants.url + '/api/search-status-by-id?status_id=' + this.statusId + '&mastodon_instance=' + 'https://' + this.instanceId;
                axios.get(dataUrl)
                    .then(res => {
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
                    }).catch(error => {
                    console.log(error);
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
        }
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>


<style>
#readonly-textbox {
    background-color: #f2f2f2; /* Light gray background */
    border: 1px solid #ccc;   /* Light gray border */
    padding: 8px;             /* Some padding for better appearance */
    font-size: 14px;          /* Adjust font size */
    color: #333;              /* Text color */
}
</style>
