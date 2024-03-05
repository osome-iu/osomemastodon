<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :osomeURL="this.osomeURL" :officialURL="this.officialURL" :header="this.header_text" />
        <InfoModal :isOpen="infoModalIsOpen" @cancel="closeInfoModal" :header="this.info_header_text" :info="this.info_body_text" :isModalError="this.isModalError"/>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Hashtags <span class="subtitle">- Metadata</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Get a list of hashtags that include a given search term and links to statuses including those hashtags.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            Statuses hashtag metadata - <router-link to="/apidocumentation#api-8" target="_blank" class="api-documentation">Documentation</router-link>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-6">
                                    <label for="mastodonInstance">Mastodon instances
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
                                        tag-placeholder="Add as a new instance"
                                        placeholder="Type to search or add"
                                        label="name"
                                        track-by="name"
                                        role="textbox"
                                        :style="{ width: '100%', height: '50%' }"
                                    />
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label for="keyword" >Search term
                                        <button @click="showInfoModal('keyword')" style="padding: 0; border: 0; background: none; outline: none; pointer-events: auto;">
                                            <i class="fas fa-info-circle ml-2" style="color: #0a53be; font-size: inherit;"></i>
                                        </button>
                                    </label>
                                    <input
                                        id="keyword"
                                        v-model="searchKeyword"
                                        :class="{'form-control': true, 'is-invalid': searchKeywordError !== ''}"
                                        @blur="x = true"
                                        placeholder="search term"
                                        @input="keywordInputChanged"
                                    />
                                    <div v-if="searchKeywordError !== ''" class="invalid-feedback">{{ searchKeywordError }}</div>
                                </div>
                                <div class="col-xl-3" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" @click="submitStatusSearch">Search</button>
                                </div>
                                <div class="row" style="margin-top: 23px;" v-if="!loading && downloadData.length">
                                    <div class="col-md-12 text-right">
                                        <button type="button" class="btn btn-warning" @click="downloadAccountJSON" style="margin-right: 20px">Download JSON</button>
                                        <button type="button" class="btn btn-primary" @click="showModal">Show URL</button> <!-- Correct the @click binding -->
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
            <div class="table-responsive" v-if="!loading && hashtagData.length>0" style="font-size: 10px;">
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th scope="col">Hashtag Name</th>
                            <th scope="col">Instance Name</th>
                            <th scope="col">URL</th>
                        </tr>
                    </thead>
                    <tbody>
                    <tr v-for="hashtag in hashtagData" :key="key">
                        <td>{{hashtag.name}}</td>
                        <td>{{ getDomain(hashtag.url) }}</td>
                        <td><a :href="hashtag.url" target="_blank" style="text-underline: #0a53be">Link</a></td>
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
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css'
import Modal from "../components/Modal.vue";
import VueMultiselect from 'vue-multiselect'
import InfoModal from "@/components/InfoModal.vue";

export default {
    name: 'searchHashtags',
    components: {
        InfoModal,
        HollowDotsSpinner,
        Modal,
        VueMultiselect
    },
    data() {
        return {
            clientKey: null,
            clientSecret: null,
            instanceData:[],
            instanceId: "",
            searchKeyword: "",
            hashtagData: [],
            loading: false,
            downloadData: [],
            keywordError: "",
            nameError: false,
            errors: [],
            searchKeywordBlurred: false,
            instanceIdBlurred: false,
            searchKeywordError: "",
            instanceIdError: "",
            modalIsOpen: false,
            osomeURL: "",
            officialURL: "",
            header_text: "",
            selectedMastodonInstances: [],
            infoModalIsOpen: false,
            info_header_text: "",
            info_body_text: "",
            isModalError: false,
            error_search_not_allowed_array: [],
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
        viewAccountInfo(accountId){
            this.$router.push({
                name: 'Accounts',  // Assuming you have a route name
                params: { accountId: accountId, instanceId: this.instanceId},
            });
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

            if (!this.isValidInstance(this.selectedMastodonInstances)) {
                this.instanceIdError = "Please add one or more Mastodon instances";
            }

            if (!this.isValidKeyword(this.searchKeyword)) {
                this.searchKeywordError = "Keyword is required";
            }

            if(this.isValidKeyword(this.searchKeyword) && this.isValidInstance(this.selectedMastodonInstances)) {
                this.header_text = "Hashtags - Metadata"
                this.loading = true;

                let searched_hashtag = this.searchKeyword.charAt(0) === '#' ? this.searchKeyword.slice(1) : this.searchKeyword;
                let dataUrl = constants.url + '/api/search-hashtag-by-keyword';
                let requestData = {
                    keyword: searched_hashtag,
                    instances: this.selectedMastodonInstances,
                };

                let jsonData = JSON.stringify(requestData);
                this.officialURL = "https://"+this.selectedMastodonInstances[0].name+"/api/v2/search?q="+searched_hashtag+"&type=hashtags"
                this.osomeURL = `curl -X POST -H "Content-Type: application/json" -d '${jsonData}' "https://osome.iu.edu/tools/mastodon/api/search-hashtag-by-keyword"`;

                axios.post(dataUrl, requestData)
                    .then(res => {
                        this.hashtagData = []
                        let data_received = res.data;
                        this.hashtagData = data_received[0].searched_status
                        this.error_search_not_allowed_array = data_received[1].error_search_not_allowed
                        this.loading = false;
                        if(this.error_search_not_allowed_array.length >=1){
                            this.infoModalIsOpen = true;
                            this.isModalError = true;
                            this.info_header_text = "Mastodon search error"
                            this.info_body_text = "There is an error with these instance(s): <b>" +this.error_search_not_allowed_array+"</b>. Please go through the instance's policy for further insight. Total "+this.hashtagData.length+" statuses retrieved from other instance(s).";
                        }else{
                            this.downloadData = this.hashtagData;
                            let message = this.hashtagData.length + " data retrieved";
                            this.successShowToast(message);
                        }
                    })
                    .catch(error => {
                        this.errorShowToast();
                        console.log(error);
                    });
                    this.loading = false;
            }
        },
        stringifyJSON(stringobject) {
            return JSON.stringify(stringobject, function (key, value) {
                return value;
            }, 4);
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
        downloadAccountJSON(){
            // Create a Blob containing the JSON data
            const blob = new Blob([JSON.stringify(this.downloadData)], { type: 'application/json' });

            // Create a download link
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'hashtag_details-'+this.searchKeyword+'.json';

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
            if(type == 'keyword'){
                this.info_header_text = "What can I type in the search box?"
                this.info_body_text = "You can use numbers, letters, or a mix of both for the hashtag to find topics you're interested in."
                this.infoModalIsOpen = true;
            }else{
                this.info_header_text = "What Mastodon instances are featured in the dropdown?"
                this.isModalError = true;
                this.info_body_text = `
                          \nIn the dropdown box, there is a list of the top 20 Mastodon instances, each with a minimum of 5000+ active users. Additionally, you can enter any Mastodon instance in the dropdown box and perform a search. View more details about the top 20 instances
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
        getDomain(url) {
            try {
                return new URL(url).hostname;
            } catch (error) {
                console.error("Invalid URL:", url);
                return "";
            }
        }
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>