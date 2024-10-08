<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :officialURL="this.officialURL" :osomeURL="this.osomeURL" :header="this.header_text"/>
        <InfoModal :isOpen="infoModalIsOpen" @cancel="closeInfoModal" :header="this.info_header_text" :info="this.info_body_text" :isModalError="this.isModalError"/>
        <div class="container-fluid px-4">
            <h1 class="page-title">Accounts <span class="subtitle">- Single Account by id</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Retrieve information about a profile using the account id. You must select a single Mastodon instance for the search. Please access the documentation <a @click.prevent="scrollToSection('/apidocumentation', '#api-6')" href="#" class="api-documentation">here</a>.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            Query
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-5">
                                    <label for="mastodonInstance">Mastodon instance
                                        <button @click="showInfoModal('instance')" style="padding: 0; border: 0; background: none; outline: none; pointer-events: auto;" aria-label="Open Mastodon instances info modal">
                                            <i class="fas fa-info-circle ml-2" style="color: #0a53be; font-size: inherit;"></i>
                                        </button>
                                    </label>
                                    <VueMultiselect
                                        id="mastodonInstance"
                                        aria-labelledby="mastodonInstance"
                                        v-model="selectedMastodonInstances"
                                        v-bind:class="{'is-invalid': instanceIdError !== ''}"
                                        :options="instanceData"
                                        :multiple="false"
                                        :taggable="true"
                                        @tag="addMastodonInstance"
                                        tag-placeholder="Add as a new instance"
                                        placeholder="Type to search or select"
                                        label="name"
                                        track-by="name"
                                        role="textbox"
                                        :style="{ width: '100%', height: '50%' }"
                                    />
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label for="keyword" >Account id
                                        <button @click="showInfoModal('keyword')" style="padding: 0; border: 0; background: none; outline: none; pointer-events: auto;" aria-label="Open keyword info modal">
                                            <i class="fas fa-info-circle ml-2" style="color: #0a53be; font-size: inherit;"></i>
                                        </button>
                                    </label>
                                    <input
                                        v-model="accountId"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchAccountIdError !== ''}"
                                        placeholder="account id"
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
                            Result
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
import InfoModal from "@/components/InfoModal.vue";

export default {
    name: 'AccountsById',
    components: {InfoModal, Modal,VueMultiselect,HollowDotsSpinner},
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
            header_text: "Accounts - Single Account by id",
            selectedMastodonInstances: [],
            loading: false,
            officialURL: "",
            osomeURL:"",
            downloadData: [],
            infoModalIsOpen: false,
            info_header_text: "",
            info_body_text: "",
            isModalError: false,
        }
    },
    watch: {
        selectedMastodonInstances: function (newInstances) {
            // Check if the array is not empty, reset the error
            if (newInstances.name) {
                this.instanceIdError = '';
            }
        },
    },
    methods: {
        scrollToSection(route, hash) {
            this.$router.push(route).then(() => {
                this.$scrollTo(hash, 500);
            });
        },
        successShowToast(message){
            toast.success(message, {
                autoClose: 8000,
            })
        },
        errorShowToast(message){
            toast.error(message, {
                autoClose: 8000,
            })
        },
        isValidAccountId(accountId) {
            return accountId.trim() !== '';
        },
        isValidInstance(instanceName) {
            // Check if instanceName exists and has a truthy name property
            const isValid = typeof instanceName === 'string' && instanceName.trim() !== '';

            // Set error message based on validity
            this.instanceIdError = isValid ? '' : 'Invalid instance name';

            return isValid;
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
            let mastodon_instance_name = this.selectedMastodonInstances
                ? (Array.isArray(this.selectedMastodonInstances)
                    ? (this.selectedMastodonInstances[0] ? this.selectedMastodonInstances[0].name : null)
                    : this.selectedMastodonInstances.name)
                : null;

            if (!this.isValidInstance(mastodon_instance_name)) {
                this.instanceIdError = "Please add one or more Mastodon instances";
            }

            if (!this.isValidAccountId(this.accountId)) {
                this.searchAccountIdError = "Account id is required";
            }

            if(this.isValidAccountId(this.accountId) && this.isValidInstance(mastodon_instance_name)) {
                this.loading = true;
                this.accountData = []
                this.clearAllFields();
                this.officialURL = 'https://'+mastodon_instance_name+'/api/v1/accounts/'+this.accountId;
                this.osomeURL = constants.url + '/api/account-search-by-id?account_id=' + this.accountId + '&mastodon_instance=' + mastodon_instance_name;
                let dataUrl = constants.url + '/api/account-search-by-id?mastodon_instance=' + mastodon_instance_name + '&account_id=' + this.accountId;
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
                        this.downloadData = res.data;
                        let message = "Account data retrieved successfully!"
                        this.successShowToast(message)
                    }).catch(error => {
                        this.infoModalIsOpen = true;
                        this.isModalError = true;
                        this.info_header_text = "Mastodon search error"
                        this.info_body_text = "Please check the accuracy of the account id you're using, and be aware that Mastodon users can set privacy settings for their accounts. As a result, you might not be able to retrieve the desired account data.";
                });
                this.loading = false;
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
        closeInfoModal() {
            this.infoModalIsOpen = false;
        },
        showInfoModal(type) {
            if(type == 'keyword'){
                this.info_header_text = "What can I use as an account id?"
                this.info_body_text = "You can use any alphanumeric characters for the account id. Each account has a different id for each server that it can be found on."
                this.infoModalIsOpen = true;
            }else{
                this.info_header_text = "What Mastodon instances are featured in the dropdown?"
                this.isModalError = true;
                this.info_body_text = `
                          \nIn the dropdown box, there is a list of the top 20 Mastodon instances, each with a minimum of 5000 active users. You can also type the url of any other Mastodon instance to add it to the instances list and perform a search. View more details about the top 20 instances
                          <a href="https://osome.iu.edu/tools/mastodon/instances/" target="_blank" class="navigation-link" aria-label="instances">here</a>.
                        `;
                this.infoModalIsOpen = true;
            }
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
.api-documentation{
    text-decoration : underline;
}
.container-fluid.px-4 {
    padding-top: 0; /* Adjust as needed */
}
.row {
    margin-top: 0; /* Adjust as needed */
    padding-top: 0; /* Adjust as needed */
}
</style>