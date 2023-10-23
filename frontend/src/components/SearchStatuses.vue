<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Statuses</h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Search for Statuses.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Search by keyword - <a href="https://docs.joinmastodon.org/methods/search/" target="_blank">Documetation</a>
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
                                    <label for="keyword">Keyword</label>
                                    <input
                                        v-model="searchKeyword"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchKeywordError !== ''}"
                                        placeholder="Keyword"
                                        v-on:blur="searchKeywordBlurred = true"
                                    />
                                    <div v-if="searchKeywordError !== ''" class="invalid-feedback">{{ searchKeywordError }}</div>
                                </div>
                                <div class="col-xl-3">
                                    <label> Access Token <router-link to="/faq" target="_blank"><i class="fas fa-info-circle"></i></router-link></label>
                                    <input
                                        v-model="accessToken"
                                        v-bind:class="{'form-control': true, 'is-invalid': accessTokenError !== ''}"
                                        v-on:blur="accessTokenBlurred = true"
                                        placeholder="Access Token"
                                    />
                                    <div v-if="accessTokenError !== ''" class="invalid-feedback">{{ accessTokenError }}</div>
                                </div>
                                <div class="col-xl-3" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitStatusSearch" >Search</button>
                                </div>
                            </div>
                        </div>
                        <div class="card-body">
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
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr v-for="status in statusData" :key="key">
                                        <td>{{status.id}}</td>
                                        <td>{{extractURLtoGetInstanceName(status.url)}}</td>
                                        <td><div v-html="this.sanitizeHtml(status.content)"></div></td>
                                        <td>{{status.in_reply_to_account_id}}</td>
                                        <td>{{status.in_reply_to_id}}</td>
                                        <td>{{status.created_at}}</td>
                                        <td>
                                          <span v-for="(mention, index) in status.mentions" :key="index">
                                              <a :href="mention.url" target="_blank" style="text-underline: #0a53be">{{mention.username}}</a>
                                              <span v-if="index < status.mentions.length - 1">, </span>
                                          </span>
                                        </td>
                                        <td>
                                          <span v-for="(tag, index) in status.tags" :key="index">
                                              <a :href="tag.url" target="_blank" style="text-underline: #0a53be">{{tag.name}}</a>
                                              <span v-if="index < status.tags.length - 1">, </span>
                                          </span>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="row" style="margin-top: 23px; float: right;" v-if="!loading && downloadData.length">
                                <div class="col-md-12 text-right">
                                    <button type="button" class="btn btn-primary" @click="downloadAccountJSON">Download JSON</button>
                                </div>
                            </div>
                            <div class="alert alert-warning" v-if="instanceData.length === 0 & !loading">
                                <fa icon="exclamation-triangle" /> No data available.
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
import { HollowDotsSpinner } from 'epic-spinners';
import DOMPurify from 'dompurify';

export default {
    name: 'singleStatus',
    components: {
        HollowDotsSpinner,
    },
    data() {
        return {
            accessToken: "",
            token: null,
            instanceData:[],
            instanceId: "",
            searchKeyword: "",
            searchType: "",
            survey_json: "",
            statusData: [],
            showDownloadBtn: "",
            loading: false,
            downloadData: [],
            searchKeywordBlurred: false,
            instanceIdBlurred: false,
            searchKeywordError: "",
            instanceIdError: "",
            accessTokenBlurred: false,
            accessTokenError: ""
        }
    },
    methods: {
        isValidKeyword(keyword) {
            return keyword.trim() !== '';
        },
        isValidInstance(instanceId) {
            return instanceId.trim() !== '';
        },
        isValidAccessToken(accessToken) {
            return accessToken.trim() !== '';
        },
        sanitizeHtml(htmlsending) {
            return DOMPurify.sanitize(htmlsending);
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
        submitStatusSearch(){
            this.searchKeywordError = "";
            this.instanceIdError = "";
            this.accessTokenError = "";

            if (!this.isValidInstance(this.instanceId)) {
                this.instanceIdError = "Please choose a valid Mastodon instance";
            }

            if (!this.isValidKeyword(this.searchKeyword)) {
                this.searchKeywordError = "Keyword is required";
            }

            if (!this.isValidAccessToken(this.accessToken)) {
                this.accessTokenError = "Access token is required";
            }
            if(this.isValidInstance(this.instanceId) && this.isValidKeyword(this.searchKeyword) && this.isValidAccessToken(this.accessToken)) {
                this.loading = true;
                let dataUrl = constants.url + '/api/search-status-by-keyword?keyword=' + this.searchKeyword + '&mastodon_instance=' + this.instanceId + '&type=statuses&client_key=' + this.accessToken;
                axios.get(dataUrl)
                    .then(res => {
                        this.singleStatusData = res;
                        this.show_json = true;
                        this.survey_json = this.stringifyJSON(this.singleStatusData)
                        this.statusData = res.data.statuses;
                        this.downloadData = this.statusData
                        this.loading = false;
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
        downloadAccountJSON(){
            // Create a Blob containing the JSON data
            const blob = new Blob([JSON.stringify(this.downloadData)], { type: 'application/json' });

            // Create a download link
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            if(this.accountsData.length > 0){
                a.download = 'Account_details-'+this.searchKeyword+'.json';
            }
            else if(this.hashtagData.length > 0){
                a.download = 'hashtag_details-'+this.searchKeyword+'.json';
            }
            else if(this.statusData.length > 0){
                a.download = 'status_details-'+this.searchKeyword+'.json';
            }
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
        }
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>