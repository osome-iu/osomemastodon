<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :url="this.api_call" :header="this.header_text"/>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Timeline Status</h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>A chronological list of public statuses that users on the platform have shared. This timeline is visible to all users and provides a way to explore and discover content that is openly shared by others. </p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Search by keyword - <a href="https://docs.joinmastodon.org/methods/timelines/#public" target="_blank">Documentation</a>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-3">
                                    <label>Mastodon Instance</label>
                                    <select v-model="instanceId"
                                            label="Instance"
                                            class="form-control"
                                            v-bind:class="{'is-invalid': instanceIdError !== ''}"
                                            v-on:blur="instanceIdBlurred = true"
                                            @input="instanceInputChanged">
                                        <option disabled
                                                value="">Choose an instance
                                        </option>
                                        <option v-for="item in instanceData"
                                                v-text="item.name"
                                                :value="item.name"></option>
                                    </select>
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-2">
                                    <label> Data</label>
                                    <select v-model="dataType"
                                            label="Choose Data"
                                            class="form-control"
                                            v-bind:class="{'is-invalid': dataTypeError !== ''}"
                                            v-on:blur="dataTypeBlurred = true"
                                            @input="dataTypeInputChanged"
                                    >
                                        <option disabled value="">Choose Data</option>
                                        <option value="false">Federated</option>
                                        <option value="true">Local</option>
                                    </select>
                                    <div v-if="dataTypeError !== ''" class="invalid-feedback">{{ dataTypeError }}</div>
                                </div>
                                <div class="col-xl-2">
                                    <label> Limit</label>
                                    <select v-model="limitNo"
                                            label="Limit"
                                            class="form-control"
                                            v-bind:class="{'is-invalid': limitNoError !== ''}"
                                            v-on:blur="limitNoBlurred = true"
                                            @input="limitNoInputChanged">
                                        <option disabled value="">Limit</option>
                                        <option value="5">5</option>
                                        <option value="10">10</option>
                                        <option value="15">15</option>
                                        <option value="20">20</option>
                                        <option value="25">25</option>
                                        <option value="30">30</option>
                                        <option value="35">35</option>
                                        <option value="40">40</option>
                                    </select>
                                    <div v-if="limitNoError !== ''" class="invalid-feedback">{{ limitNoError }}</div>
                                </div>
                                <div class="col-xl-4" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitStatusesSearch" >Search</button>
                                </div>
                                <div class="row" style="margin-top: 23px; float: right;" v-if="!loading && statusesArray.length">
                                    <div class="col-md-12 text-right">
                                        <button type="button" class="btn btn-warning" @click="downloadJSON" style="margin-right: 20px">Download JSON</button>
                                        <button type="button" class="btn btn-primary" :onclick="showModal" >Show URL</button>
                                    </div>
                                </div>
                            </div>
                            <div class="row align-items-center">
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
                    <div class="table-responsive" v-if="!loading && this.statusesArray.length" style="font-size: 8px;">
                        <table class="table table-bordered">
                            <thead>
                            <tr>
                                <th scope="col">ID</th>
                                <th scope="col">Instance</th>
                                <th scope="col" style="width: 10px;">Content</th>
                                <th scope="col">In reply</th>
                                <th scope="col">In reply Id </th>
                                <th scope="col">Created At </th>
                                <th scope="col">Mentions </th>
                                <th scope="col">Tags </th>
                                <th scope="col">View Status </th>
                                <th scope="col">Profile </th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="status in statusesArray" :key="key">
                                <td>{{status.id}}</td>
                                <td>{{extractURLtoGetInstanceName(status.url)}}</td>
                                <td><div v-html="status.content" style="font-size: 10px;"></div></td>
                                <td>{{status.in_reply_to_account_id}}</td>
                                <td>{{status.in_reply_to_id}}</td>
                                <td>{{status.created_at}}</td>
                                <td>
                                    <div style="font-size: 8px;">
                                                <span v-for="(mention, index) in status.mentions" :key="index">
                                                      <a :href="mention.url" target="_blank" style="text-underline: #0a53be">{{mention.username}}</a>
                                                      <span v-if="index < status.mentions.length - 1">, </span>
                                                </span>
                                    </div>
                                </td>
                                <td>
                                    <span v-for="(extractedURL, index) in status.tags" :key="index">
                                        <a :href="extractedURL.url" target="_blank" style="text-underline: #0a53be">{{extractedURL.name}}</a>
                                        <span v-if="index < status.tags.length - 1">, </span>
                                    </span>
                                </td>
                                <td>
                                    <a :href="status.url" target="_blank" style="text-underline: #0a53be">Status</a>
                                </td>
                                <td><button type="button" class="btn btn-primary btn-sm" @click="viewAccountInfo(status.id)">view</button></td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import axios from "axios";
import * as constants from "@/shared/Constants";
import { HollowDotsSpinner } from 'epic-spinners'
import {toast} from "vue3-toastify";
import Modal from "@/components/Modal.vue";

export default {
    name: 'timelinestatus',
    components: {
        HollowDotsSpinner,
        Modal
    },
    data() {
        return {
            instanceId: "",
            clientKey: null,
            clientSecret: null,
            instanceData:[],
            limitNo: "",
            dataType: "",
            statusesArray: [],
            loading: false,

            instanceIdError: "",
            instanceIdBlurred: false,
            limitNoBlurred: false,
            limitNoError: "",
            dataTypeError: "",
            dataTypeBlurred: false,
            modalIsOpen: false,
            api_call: "",
            header_text: ""
        }
    },
    methods: {
        instanceInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.instanceIdError = ""
                this.instanceIdBlurred = false;
            }
            this.instanceId = e.target.value;
        },
        isValidInput(inputValue) {
            return inputValue.trim() !== '';
        },
        limitNoInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.limitNoError = "";
                this.limitNoBlurred = false;
            }
            this.limitNo = e.target.value;
        },
        dataTypeInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.dataTypeError = "";
                this.dataTypeBlurred = false;
            }
            this.dataType = e.target.value;
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
        submitStatusesSearch(){
            if (!this.isValidInput(this.instanceId)) {
                this.instanceIdError = "Please choose a Mastodon instance.";
            }
            if (!this.isValidInput(this.limitNo)) {
                this.limitNoError = "Please enter limit No";
            }
            if (!this.isValidInput(this.dataType)) {
                this.dataTypeError = "Please enter data type";
            }
            if(this.isValidInput(this.instanceId) && this.isValidInput(this.limitNo) && this.isValidInput(this.dataType)){
                https://{mastodon_instance}/api/v1/timelines/public?limit={limit}&local={data_type}
                this.api_call = "https://"+this.instanceId+ "/api/v1/timelines/public?limit="+ this.limitNo+ "&local="+this.dataType;
                this.header_text = "Search Statuses URL"
                this.statusesArray = []
                this.loading = true;
                let dataUrl = constants.url + '/api/hashtag-search?mastodon_instance=' + this.instanceId + '&limit=' + this.limitNo + '&data_type=' + this.dataType;
                this.clearAllFields()
                axios.get(dataUrl)
                    .then(res => {
                        this.statusesArray = res.data.hashtag;
                        this.loading = false;
                        let message = this.statusesArray.length +" data retrieved"
                        this.successShowToast(message)
                    }).catch(error => {
                        console.log(error);
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
            const blob = new Blob([JSON.stringify(this.statusesArray)], { type: 'application/json' });

            // Create a download link
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'hastag_data-'+new Date() +'.json';

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
        viewAccountInfo(accountId){
            this.$router.push({
                name: 'AccountsById',
                params: { accountId: accountId, instanceId: this.instanceId},
            });
        },
        extractURLtoGetInstanceName(acct) {
            const parts = acct.split('/');
            return parts[2];
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
    created() {
        this.accountId = this.$route.params.accountId;
        this.instanceId = this.$route.params.instanceId;
        if(!this.instanceId){
            this.instanceId = ""
        }
        else{
            this.submitAccountSearch();
        }
    },
}
</script>