<template>
    <main>
        <Modal :isOpen="modalIsOpen" @cancel="closeModal" :officialURL="this.officialURL" :osomeURL="this.osomeURL" :header="this.header_text"/>
        <InfoModal :isOpen="infoModalIsOpen" @cancel="closeInfoModal" :header="this.info_header_text" :info="this.info_body_text" :isModalError="this.isModalError"/>
        <div class="container-fluid px-4">
            <h1 class="page-title">Statuses <span class="subtitle">- Search by hashtag</span></h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Get the most recent statuses that contain the given hashtag.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            Statuses search by hashtag - <router-link to="/apidocumentation#api-3" target="_blank" class="api-documentation">Documentation</router-link>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-xl-4">
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
                                        :style="{ width: '100%', height: '40%' }"
                                    />
                                    <div v-if="instanceIdError !== ''" class="invalid-feedback">{{ instanceIdError }}</div>
                                </div>
                                <div class="col-xl-2">
                                    <label for="keyword" >Hashtag
                                        <button @click="showInfoModal('keyword')" style="padding: 0; border: 0; background: none; outline: none; pointer-events: auto;">
                                            <i class="fas fa-info-circle ml-2" style="color: #0a53be; font-size: inherit;"></i>
                                        </button>
                                    </label>
                                    <input
                                        v-model="hashtagSearch"
                                        v-bind:class="{'form-control': true, 'is-invalid': hashtagKeywordError !== ''}"
                                        placeholder="hashtag"
                                        v-on:blur="searchAccountIdBlurred = true"
                                        @input="hashtagInputChanged"
                                    />
                                    <div v-if="hashtagKeywordError !== ''" class="invalid-feedback">{{ hashtagKeywordError }}</div>
                                </div>
                                <div class="col-xl-2">
                                    <label for="keyword" >Data
                                        <button @click="showInfoModal('data')" style="padding: 0; border: 0; background: none; outline: none; pointer-events: auto;">
                                            <i class="fas fa-info-circle ml-2" style="color: #0a53be; font-size: inherit;"></i>
                                        </button>
                                    </label>
                                    <select v-model="dataType"
                                            id="datatype"
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
                                    <label for="limit"> Limit</label>
                                    <select v-model="limitNo"
                                            id="limit"
                                            label="Limit"
                                            class="form-control"
                                            v-bind:class="{'is-invalid': limitNoError !== ''}"
                                            v-on:blur="limitNoBlurred = true"
                                            @input="limitNoInputChanged">
                                        <option disabled value="">Limit</option>
                                        <option value="5">5 Statuses</option>
                                        <option value="10">10 Statuses</option>
                                        <option value="15">15 Statuses</option>
                                        <option value="20">20 Statuses</option>
                                        <option value="25">25 Statuses</option>
                                        <option value="30">30 Statuses</option>
                                        <option value="35">35 Statuses</option>
                                        <option value="40">40 Statuses</option>
                                    </select>
                                    <div v-if="limitNoError !== ''" class="invalid-feedback">{{ limitNoError }}</div>
                                </div>
                                <div class="col-xl-1" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitHashtagSearch" >Search</button>
                                </div>
                                <div class="row" style="margin-top: 23px; float: right;" v-if="!loading && hashtagArray.length">
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
                    <div class="table-responsive" v-if="!loading && hashtagArray.length" style="font-size: 8px;">
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
                            <tr v-for="hashtag in hashtagArray" :key="key">
                                <td>{{hashtag.id}}</td>
                                <td>{{extractURLtoGetInstanceName(hashtag.url)}}</td>
                                <td><div v-html="hashtag.content" style="font-size: 10px;"></div></td>
                                <td>{{hashtag.in_reply_to_account_id}}</td>
                                <td>{{hashtag.in_reply_to_id}}</td>
                                <td>{{hashtag.created_at}}</td>
                                <td>
                                    <div style="font-size: 8px;">
                                                <span v-for="(mention, index) in hashtag.mentions" :key="index">
                                                      <a :href="mention.url" target="_blank" style="text-underline: #0a53be">{{mention.username}}</a>
                                                      <span v-if="index < hashtag.mentions.length - 1">, </span>
                                                </span>
                                    </div>
                                </td>
                                <td>
                                          <span v-for="(extractedURL, index) in hashtag.tags" :key="index">
                                              <a :href="extractedURL.url" target="_blank" style="text-underline: #0a53be">{{extractedURL.name}}</a>
                                              <span v-if="index < hashtag.tags.length - 1">, </span>
                                          </span>
                                </td>
                                <td><a :href="hashtag.url" target="_blank" style="text-underline: #0a53be">Status</a></td>
                                <td><button type="button" class="btn btn-primary btn-sm" @click="viewAccountInfo(hashtag.id)">view</button></td>
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
import { HollowDotsSpinner } from 'epic-spinners';
import Modal from "@/components/Modal.vue";
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import VueMultiselect from 'vue-multiselect'
import InfoModal from "@/components/InfoModal.vue";

export default {
    name: 'singleStatus',
    components: {
        InfoModal,
        HollowDotsSpinner,
        Modal,
        VueMultiselect
    },
    data() {
        return {
            instanceId: "",
            clientKey: null,
            clientSecret: null,
            instanceData:[],
            limitNo: 40,
            dataType: false,
            hashtagSearch: "",
            hashtagArray: [],
            loading: false,
            instanceIdError: "",
            instanceIdBlurred: false,
            hashtagKeywordError: "",
            hashtagSearchBlurred: false,
            dataTypeError: "",
            dataTypeBlurred: false,
            limitNoError: "",
            limitNoBlurred: false,
            modalIsOpen: false,
            osomeURL: "",
            officialURL: "",
            header_text: "",
            selectedMastodonInstances: [],
            infoModalIsOpen: false,
            info_header_text: "",
            info_body_text: "",
            isModalError: false,
            success_searched_array: [],
            error_search_not_allowed_array: []
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
        isValidInstance(instanceArray) {
            return instanceArray.length >= 1;
        },
        hashtagInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.hashtagKeywordError = ""
                this.hashtagSearchBlurred = false;
            }
        },
        instanceInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.instanceIdError = ""
                this.instanceIdBlurred = false;
            }
            this.instanceId = e.target.value;
        },
        dataTypeInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.dataTypeError = "";
                this.dataTypeBlurred = false;
            }
            this.dataType = e.target.value;
        },
        limitNoInputChanged(e){
            let valueReceived = e.target.value;
            if(valueReceived){
                this.limitNoError = "";
                this.limitNoBlurred = false;
            }
            this.limitNo = e.target.value;
        },
        isValidInput(inputValue) {
            return inputValue !== '';
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
        errorShowToast(){
            toast.error('Error in retrieving data!', {
                autoClose: 8000,
            })
        },
        successShowToast(message){
            toast.success(message, {
                autoClose: 8000,
            })
        },
        submitHashtagSearch(){

            if (!this.isValidInstance(this.selectedMastodonInstances)) {
                this.instanceIdError = "Please add one or more Mastodon instances";
            }

            if (!this.isValidInput(this.hashtagSearch)) {
                this.hashtagKeywordError = "Hashtag is required.";
            }

            if (!this.isValidInput(this.dataType)) {
                this.dataTypeError = "Data type is required.";
            }

            if (!this.isValidInput(this.limitNo)) {
                this.limitNoError = "Limit no is required.";
            }

            if(this.isValidInstance(this.selectedMastodonInstances) && this.isValidInput(this.hashtagSearch) && this.isValidInput(this.dataType) && this.isValidInput(this.limitNo)) {

                this.header_text = "Search Statuses URL"
                this.loading = true;
                this.hashtagArray = [];
                let dataUrl = constants.url + '/api/hashtag-search';

                let searched_hashtag = this.hashtagSearch.charAt(0) === '#' ? this.hashtagSearch.slice(1) : this.hashtagSearch;

                let requestData = {
                    hashtag: searched_hashtag,
                    mastodon_instances: this.selectedMastodonInstances,
                    data_type: this.dataType,
                    limit_no: this.limitNo
                };

                let jsonData = JSON.stringify(requestData);

                this.osomeURL = `curl -X POST -H "Content-Type: application/json" -d '${jsonData}' "https://osome.iu.edu/tools/mastodon/api/hashtag-search"`;
                this.officialURL = "https://"+this.selectedMastodonInstances[0].name+ "/api/v1/timelines/tag/"+ searched_hashtag+ "?limit="+this.limitNo+"&local="+ this.dataType;

                axios.post(dataUrl, requestData)
                    .then(res => {
                        let data_received = res.data;
                        this.success_searched_array = data_received[0].timeline_status
                        this.error_search_not_allowed_array = data_received[1].error_search_not_allowed
                        this.loading = false;
                        for (let statuses_array of this.success_searched_array){
                            for (let single_status of statuses_array.statuses_timeline){
                                this.hashtagArray.push(single_status)
                            }
                        }
                        if(this.error_search_not_allowed_array.length >=1){
                            this.infoModalIsOpen = true;
                            this.isModalError = true;
                            this.info_header_text = "Mastodon search error"
                            this.info_body_text = "There was an error while retrieving data from the following instance(s): <b>" +this.error_search_not_allowed_array+"</b>. Please review its/their instance policies for further insight. Total <b>"+this.hashtagArray.length+"</b> statuses retrieved from other instance(s) searched. ";
                        }else{
                            this.downloadData = this.hashtagArray;
                            let message = this.hashtagArray.length + " data retrieved";
                            this.successShowToast(message);
                        }
                    })
                    .catch(error => {
                        this.errorShowToast();
                        this.loading = false;
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
            const blob = new Blob([JSON.stringify(this.hashtagArray)], { type: 'application/json' });

            // Create a download link
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'hastag_data-'+this.hashtagSearch+'.json';

            let message = "Data downloaded successfully!"
            this.successShowToast(message)

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
                name: 'Accounts',
                params: { accountId: accountId, instanceId: this.instanceId},
            });
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
            if(type === 'keyword'){
                this.info_header_text = "What can I type in the search box?"
                this.info_body_text = "You can use numbers, letters, or a mix of both to find topics you're interested in as the hashtag to search."
                this.infoModalIsOpen = true;
            }else if(type == 'data'){
                this.info_header_text = "Difference between the local and federated timelines"
                this.info_body_text = "The local timeline displays statuses from all users on a specified server, while the federated timeline includes public statuses from users across the Mastodon network who are followed by users on the specified server."
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

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

