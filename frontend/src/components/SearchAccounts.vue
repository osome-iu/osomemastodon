<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :osomeURL="this.osomeURL" :officialURL="this.officialURL" :header="this.header_text" />
        <InfoModal :isOpen="infoModalIsOpen" @cancel="closeInfoModal" :header="this.info_header_text" :info="this.info_body_text" :isModalError="this.isModalError"/>
        <div class="container-fluid px-4">
            <h1 class="page-title">Accounts <span class="subtitle">- Search by keywords</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Search for accounts that contain the given keywords in the username or display name. You can access the documentation <router-link to="/apidocumentation#api-5" target="_blank" class="api-documentation">here</router-link>.</p>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            Query
                        </div>
                        <div class="card-body">
                            <div a class="row">
                                <div class="col-xl-6">
                                    <label for="mastodonInstance">Mastodon instances
                                        <button @click="showInfoModal('instance')" style="padding: 0; border: 0; background: none; outline: none; pointer-events: auto;" aria-label="Open Mastodon instances modal">
                                            <i class="fas fa-info-circle ml-2" style="color: #0a53be; font-size: inherit;"></i>
                                        </button>
                                    </label>
                                    <VueMultiselect
                                        id="mastodonInstance"
                                        aria-labelledby="mastodonInstance"
                                        v-model="selectedMastodonInstances"
                                        v-bind:class="{'is-invalid': instanceIdError !== ''}"
                                        :options="instanceData"
                                        :multiple="true"
                                        :taggable="true"
                                        @tag="addMastodonInstance"
                                        tag-placeholder="Add as a new instance"
                                        placeholder="Type to search or select"
                                        label="name"
                                        track-by="name"
                                        role="textbox"
                                        :style="{ width: '100%', height: '40%' }"
                                    />
                                    <!-- Check if instanceIdError is used correctly -->
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-4">
                                    <label for="keyword" >Keywords
                                        <button @click="showInfoModal('keyword')" style="padding: 0; border: 0; background: none; outline: none; pointer-events: auto;" aria-label="Open keyword info modal">
                                            <i class="fas fa-info-circle ml-2" style="color: #0a53be; font-size: inherit;"></i>
                                        </button>
                                    </label>
                                    <input
                                        v-model="searchKeyword"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchKeywordError !== ''}"
                                        v-on:blur="searchKeywordBlurred = true"
                                        placeholder="keywords"
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
                                        <button type="button" class="btn btn-primary" :onclick="showModal">Show URL</button>
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
            <div class="col-xl-12" v-if="!loading && accountsData.length>0">
                <div class="card mb-4">
                    <div class="card-header">
                        Results
                    </div>
                    <div class="table-responsive"  style="font-size: 12px;">
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
                </div>
            </div>
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
import InfoModal from "@/components/InfoModal.vue";


export default {
    name: 'accounts',
    components: {
        InfoModal,
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
            selectedMastodonInstances: [],
            infoModalIsOpen: false,
            info_header_text: "",
            info_body_text: "",
            isModalError: false,
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
        viewAccountInfo(accountId, instance_name){
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

            if (!this.isValidInstance(this.selectedMastodonInstances)) {
                this.instanceIdError = "Please add one or more Mastodon instances";
            }

            if (!this.isValidKeyword(this.searchKeyword) ) {
                this.searchKeywordError = "A keyword is required";
            }

            if(this.isValidKeyword(this.searchKeyword) && this.isValidInstance(this.selectedMastodonInstances) ) {
                this.header_text = "Accounts - Search by keyword"
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
                        this.accountsData = data_received[0].searched_accounts
                        this.error_search_not_allowed_array = data_received[1].error_search_not_allowed
                        this.loading = false;
                        if(this.error_search_not_allowed_array.length >=1){
                            this.infoModalIsOpen = true;
                            this.isModalError = true;
                            this.info_header_text = "Mastodon search error"
                            this.info_body_text = "There is an error with these instance(s): <b>" +this.error_search_not_allowed_array+"</b>. Please go through the instance's policy for further insight. Total <b>"+this.accountsData.length+"</b> accounts retrieved from other instance(s) searched.";
                        }else{
                            this.downloadData = this.accountsData;
                            let message = this.accountsData.length + " data retrieved";
                            this.successShowToast(message);
                        }
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
        async checkEnteredMastodonInstance(enteredMastodonInstance){
            const apiURL = `https://${enteredMastodonInstance}/api/v1/instance`;
            try {
                const response = await fetch(apiURL, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });
                if (response.ok) {
                    return true;
                }
                return false
            } catch (error) {
                console.error('Error during API request:', error);
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
        closeInfoModal() {
            this.infoModalIsOpen = false;
        },
        showInfoModal(type) {
            if (type == 'keyword') {

                this.info_header_text = "What can I type in the search box?"
                this.info_body_text = "You can use any numbers, letters, or a mix of both to find specific users across multiple Mastodon servers. Keywords are separated by spaces and the search will return accounts containing those keywords."
                this.infoModalIsOpen = true;
            }else{
                this.info_header_text = "What Mastodon instances are featured in the dropdown?"
                this.isModalError = true;
                this.info_body_text = `
                          \nIn the dropdown box, there is a list of the top 20 Mastodon instances, each with a minimum of 5000 active users. Additionally, you can enter any Mastodon instance in the dropdown box and perform a search. View more details about the top 20 instances
                          <a href="https://osome.iu.edu/tools/mastodon/instances/" target="_blank" class="navigation-link" aria-label="instances">here</a>.
                        `;
                this.infoModalIsOpen = true;
            }
        },
        async addMastodonInstance (newInstance) {
            if(await this.checkEnteredMastodonInstance(newInstance)) {
                const mastodonInstance = {
                    name: newInstance
                }
                this.instanceData.push(mastodonInstance)
                this.selectedMastodonInstances.push(mastodonInstance)
            }else{
                this.infoModalIsOpen = true;
                this.info_header_text = "Error in adding Mastodon instance"
                this.info_body_text = "<strong>" + newInstance + "</strong> is not a valid Mastodon instance. Please add a valid instance name."
                this.isModalError = true;
                this.infoModalIsOpen = true;
            }
        },
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style scoped>
.api-documentation{
    text-decoration : underline;
}
</style>

