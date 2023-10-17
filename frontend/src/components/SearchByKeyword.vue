<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Status - Search By Keyword</h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Search for content in accounts, statuses and hashtags.</p>
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
                            <div class="row align-items-center">
                                <div class="col-xl-3">
                                    <label>Mastodon Instance</label>
                                    <select v-model="instanceId"
                                            label="Instance"
                                            class="form-control">
                                        <option disabled
                                                value="">Choose an instance
                                        </option>
                                        <option v-for="item in instanceData"
                                                v-text="item.name"
                                                :value="item.name"></option>
                                    </select>
                                </div>
                                <div class="col-xl-3">
                                    <label> Keyword</label>
                                    <input class="form-control" type="text" placeholder="Keyword" aria-label="Search for..." aria-describedby="btnNavbarSearch" v-model="searchKeyword"/>
                                </div>
                                <div class="col-xl-3">
                                    <label> Type</label>
                                    <select v-model="searchType"
                                            label="searchType"
                                            class="form-control">
                                        <option disabled value="">Choose the type</option>
                                        <option value="hashtags">Hashtags</option>
                                        <option value="statuses">Statuses</option>
                                        <option value="accounts">Accounts</option>
                                    </select>
                                </div>
                                <div class="col-xl-3" v-if="searchType == 'all' || searchType== 'statuses'">
                                    <label> Access Token <router-link to="/faq" target="_blank"><i class="fas fa-info-circle"></i></router-link></label>
                                    <input class="form-control" type="text" placeholder="Keyword" aria-label="Search for..." aria-describedby="btnNavbarSearch" v-model="clientKey"/>
                                </div>
                                <div class="col-xl-4" style="margin-top: 23px;">
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
                            <div class="table-responsive" v-if="!loading && accountsData.length>0" style="font-size: 12px;">
                                <table class="table table-bordered">
                                    <thead>
                                    <tr>
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
                                        <td>{{account.display_name}}</td>
                                        <td>{{account.username}}</td>
                                        <td>{{this.extractInstanceName(account.acct)}}</td>
                                        <td>{{account.followers_count}}</td>
                                        <td>{{account.following_count}}</td>
                                        <td>{{account.statuses_count}}</td>
                                        <td><button type="button" class="btn btn-primary btn-sm" @click="viewAccountInfo(account.id)">view</button></td>
                                    </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="table-responsive" v-if="!loading && hashtagData.length>0" style="font-size: 10px;">
                                <table class="table table-bordered">
                                    <thead>
                                    <tr>
                                        <th scope="col">Name</th>
                                        <th scope="col">URL</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr v-for="hashtag in hashtagData" :key="key">
                                        <td>{{hashtag.name}}</td>
                                        <td><a :href="hashtag.url" target="_blank" style="text-underline: #0a53be">Link</a></td>
                                    </tr>
                                    </tbody>
                                </table>
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
                                        <td><div v-html="status.content"></div></td>
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
import { HollowDotsSpinner } from 'epic-spinners'

export default {
    name: 'singleStatus',
    components: {
        HollowDotsSpinner,
    },
    data() {
        return {
            clientKey: null,
            clientSecret: null,
            token: null,
            instanceData:[],
            instanceId: "",
            searchKeyword: "",
            show_json: false,
            searchType: "",
            survey_json: "",
            accountsData: "",
            hashtagData: [],
            statusData: [],
            showDownloadBtn: "",
            isLoading: false,
            downloadData: [],
        }
    },
    methods: {
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
            this.survey_json = ""
            // this.clearAllFields();
            this.isLoading=true;
            let dataUrl = constants.url + '/api/search-status-by-keyword?keyword='+this.searchKeyword+'&mastodon_instance='+this.instanceId+'&type='+this.searchType+'&client_key='+this.clientKey;
            axios.get(dataUrl)
                .then(res => {
                    this.singleStatusData = res;
                    this.show_json = true;
                    this.survey_json = this.stringifyJSON(this.singleStatusData)
                    if(this.searchType == 'accounts'){
                        this.accountsData = res.data.accounts;
                        this.hashtagData = []
                        this.statusData = []
                        this.downloadData = this.accountsData
                    }
                    if(this.searchType == 'hashtags'){
                        this.hashtagData = res.data.hashtags;
                        console.log(this.hashtagData)
                        this.accountsData = []
                        this.statusData = []
                        this.downloadData = this.hashtagData
                    }
                    if(this.searchType == 'statuses'){
                        this.statusData = res.data.statuses;
                        this.hashtagData = []
                        this.accountsData = []
                        this.downloadData = this.statusData
                    }
                    this.isLoading = false;
                }).catch(error => {
                console.log(error);
            });
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