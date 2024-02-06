<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :officialURL="this.officialURL" :osomeURL="this.osomeURL" :header="this.header_text"/>
        <InfoModal :isOpen="infoModalIsOpen" @cancel="closeInfoModal" :header="this.info_header_text" :info="this.info_body_text" :isModalError="this.isModalError"/>
        <div class="container-fluid px-4">
            <h1 class="page-title">Statuses <span class="subtitle">- Search by keyword</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Search statuses across multiple instances using a given keyword. An <b>access token is required</b> for each instance being searched.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            Statuses search by keyword - <router-link to="/apidocumentation#api-2" target="_blank" class="api-documentation">Documentation</router-link>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-4">
                                    <label for="mastodonInstance">Mastodon Instances
                                        <button @click="showInfoModal('instance')" style="padding: 0; border: 0; background: none; outline: none; pointer-events: auto;">
                                            <i class="fas fa-info-circle ml-2" style="color: #0a53be; font-size: inherit;"></i>
                                        </button>
                                    </label>
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
                                        :style="{ width: '100%', height: '50%', color: 'black' }"
                                        input-class="custom-input-class"
                                        ref="multiselectRef"
                                    />
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-2">
                                    <label for="keyword" >Keyword
                                        <button @click="showInfoModal('keyword')" style="padding: 0; border: 0; background: none; outline: none; pointer-events: auto;">
                                            <i class="fas fa-info-circle ml-2" style="color: #0a53be; font-size: inherit;"></i>
                                        </button>
                                    </label>
                                    <input
                                        v-model="searchKeyword"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchKeywordError !== ''}"
                                        placeholder="keyword"
                                        v-on:blur="searchKeywordBlurred = true"
                                        @input="keywordInputChanged"
                                        id="keyword"
                                    />
                                    <div v-if="searchKeywordError !== ''" class="invalid-feedback">{{ searchKeywordError }}</div>
                                </div>
                                <div class="col-md-3 col-12" style="margin-top: 20px; margin-left: 20px; display: flex; align-items: center;">
                                    <input type="checkbox" id="checkbox" v-model="checkMastodonInstance" @input="changeCheckMastodonInstance"/>
                                    <label class="col-12 d-flex align-items-center" style="white-space: nowrap; pointer-events: none;">
                                        <span>&nbsp;Check instance validity</span>&nbsp;
                                        <button @click="showInfoModal('validity')" style="padding: 0; border: 0; background: none; outline: none; pointer-events: auto;">
                                            <i class="fas fa-info-circle ml-2" style="color: #0a53be; font-size: inherit;"></i>
                                        </button>
                                    </label>
                                </div>
                                <div class="col-xl-2" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitStatusSearch" >Search</button>
                                </div>
                            </div>
                            <div v-if="selectedMastodonInstances.length">
                                <div class="row" style="margin-top: 20px; font-weight: bold;">
                                    <p style="text-decoration: underline;" >Access Tokens <router-link to="/faq" target="_blank"><i class="fas fa-info-circle"></i></router-link></p>
                                </div>
                                <div class="row" v-for="(mastodonInstance, index) in selectedMastodonInstances" :key="index" style="margin-top: 10px;">
                                    <div class="col-md-1 col-xl-2 col-md-4 col-sm-6" style="margin-top: 5px;">
                                        <p>{{ mastodonInstance.name }}</p>
                                    </div>
                                    <div class="col-md-1 col-xl-5 col-md-4 col-sm-6">
                                        <input
                                            v-model="accessTokenArray[index]"
                                            v-bind:class="{'form-control': true, 'is-invalid': formSubmit && !accessTokenArray[index]}"
                                            class="form-control"
                                            placeholder="access token"
                                        />
                                        <div class="invalid-feedback" v-if="formSubmit">
                                            {{ accessTokenArray[index] ? "" : "Please enter an access token" }}
                                        </div>
                                    </div>
                                    <div class="col-md-1 col-xl-4 col-md-4 col-sm-12 mt-md-0 mt-2" style="margin-top: 30px;">
                                        <button type="button" class="btn btn-danger" @click="removeMastodonInstanceFromBtn(index)">Remove</button>
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
import InfoModal from "../components/InfoModal.vue";
import VueMultiselect from "vue-multiselect";

export default {
    name: 'searchStatus',
    components: {
        HollowDotsSpinner,
        Modal,
        InfoModal,
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
            checkMastodonInstance : false,
            selectedMastodonInstances: [],
            accessTokenArray: [], // Array to store access tokens
            infoModalIsOpen: false,
            info_header_text: "",
            info_body_text: "",
            isModalError: false,
            formSubmit: false,
            success_searched_array: [],
            error_access_key_searched_array: [],
            error_search_not_allowed_array: []
        }
    },
    watch: {
        selectedMastodonInstances: function (newInstances) {
            // Check if the array is not empty, reset the error
            if (newInstances.length > 0) {
                this.instanceIdError = '';
            }
            this.formSubmit = false;
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
        isValidAccessTokens(){
            if(this.selectedMastodonInstances.length == this.accessTokenArray.length){
                return !this.accessTokenArray.some(token => token.trim() === '');
            }else{
                return false;
            }
        },
        submitStatusSearch(){
            this.searchKeywordError = "";
            this.instanceIdError = "";
            this.accessTokenError = "";
            this.formSubmit =true;

            if (!this.isValidInstance(this.selectedMastodonInstances)) {
                this.instanceIdError = "Please add one or more Mastodon instances";
            }

            if (!this.isValidKeyword(this.searchKeyword)) {
                this.searchKeywordError = "Keyword is required";
            }
            if(this.isValidKeyword(this.searchKeyword) && this.isValidInstance(this.selectedMastodonInstances) && this.isValidAccessTokens()) {
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
                        this.success_searched_array = res.data[1].searched_status
                        this.error_search_not_allowed_array = res.data[2].error_search_not_allowed_instances
                        this.error_access_key_searched_array = res.data[3].error_search_access_key_instances
                            if(this.success_searched_array) {
                                if (this.checkMastodonInstance) {
                                    //Assuming res.data is an array containing hashtag data
                                    for (let data of data_received) {
                                        const mastodonInstanceResult = await this.checkIfMastodonInstance(data.searched_status)
                                        this.statusData = this.statusData.concat(mastodonInstanceResult);
                                    }
                                } else {
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
                            }
                        this.loading = false;
                        if(this.this.error_access_key_searched_array.length >= 1)
                        {
                            this.infoModalIsOpen = true;
                            this.info_header_text = "Error in Mastodon search"
                            this.isModalError = true;
                            this.info_body_text = "The access tokens provided for the Mastodon instances - <b>" + this.error_search_not_allowed_array.join(', ') + "</b> are incorrect. Please enter valid access tokens.";
                        }
                    })
                    .catch(error => {
                        this.loading = false;
                        console.log(error);
                        if(this.error_search_not_allowed_array.length >= 1)
                        {
                            this.infoModalIsOpen = true;
                            this.isModalError = true;
                            this.info_header_text = "Error in Mastodon search"
                            this.info_body_text = "The access tokens provided for the Mastodon instances - <b>" + this.error_access_key_searched_array.join(', ') + "</b> are incorrect. Please enter valid access tokens.";
                        }
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
                            // Assuming you want to add the API response data to each status
                            const updatedStatus = {...status, "mastodon_instance": "Yes"};
                            updatedStatusData.push(updatedStatus);
                        } else {
                            console.error(`Error: ${response.status} - ${response.statusText}`);
                            // Assuming you want to add an error message to each status in case of an error
                            const updatedStatus = {...status, "mastodon_instance": "No"};
                            updatedStatusData.push(updatedStatus);
                        }
                    } catch (error) {
                        console.error('Error during API request:', error);
                        // Assuming you want to add an error message to each status in case of an error
                        const updatedStatus = {...status, "mastodon_instance": "No"};
                        updatedStatusData.push(updatedStatus);
                    }
            }
            return updatedStatusData;
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
        stringifyJSON(stringObject) {
            return JSON.stringify(stringObject, function (key, value) {
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
        closeInfoModal() {
            this.infoModalIsOpen = false;
        },
        showInfoModal(type) {
            if(type =='keyword'){
                this.info_header_text = "What can I type in the search box?"
                this.info_body_text = "In Mastodon status keyword search, you can use numbers, letters, or a mix of both to find topics you're interested in as the search keyword."
                this.infoModalIsOpen = true;
            }
            else if(type == 'validity'){
                this.info_header_text = "What does \"Check instance validity\" mean?"
                this.info_body_text = "This option will list whether or not the status comes from a valid Mastodon Instance. Mastodon uses the ActivityPub protocol, which allows non-Mastodon applications (such as wordpress plugins) to submit status updates that do not originate from an actual, valid Mastodon Instance."
                this.infoModalIsOpen = true;
            }
            else{
                this.info_header_text = "What Mastodon instances are featured in the dropdown?"
                this.isModalError = true;
                this.info_body_text = `
                          \nIn the dropdown box, there is a list of the top 20 Mastodon instances, each with a minimum of 5000+ active users. Additionally, you can enter any Mastodon instance in the dropdown box and perform a search. View more details about the top 20 instances
                          <a href="https://osome.iu.edu/tools/mastodon/instances/" target="_blank" class="navigation-link" aria-label="instances">here</a>.
                        `;
                this.infoModalIsOpen = true;
            }
        },
        changeCheckMastodonInstance(){
            this.statusData = []
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
                this.info_body_text = "<strong>" + newInstance + "</strong> is not a valid Mastodon instance. Please add a valid Mastodon instance."
                this.isModalError = true;
                this.infoModalIsOpen = true;
            }
        },
        removeMastodonInstance(removedItem) {
            // Find the index of the removed item
            const index = this.selectedMastodonInstances.findIndex(item => item === removedItem);

            // Remove the corresponding elements from accessTokenArray
            this.accessTokenArray.splice(index, 1);
            this.statusData = []
        },
        removeMastodonInstanceFromBtn(index){
            // Remove the element at the specified index from both arrays
            this.selectedMastodonInstances.splice(index, 1);
            this.accessTokenArray.splice(index, 1);
            this.statusData = []
        }
    },
    mounted() {
        this.fetchAllInstanceData();
        this.$refs.multiselectRef.$el.querySelector('input').style.setProperty('color', 'black', 'important');
    },
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style scoped>
.custom-input-class::placeholder {
    color: black;
}
</style>