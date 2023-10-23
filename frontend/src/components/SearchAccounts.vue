<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Accounts</h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Search for content in accounts.</p>
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
                                <div class="col-xl-4">
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
                                <div class="col-xl-4">
                                    <label for="keyword">Keyword</label>
                                    <input
                                        v-model="searchKeyword"
                                        v-bind:class="{'form-control': true, 'is-invalid': searchKeywordError !== ''}"
                                        v-on:blur="searchKeywordBlurred = true"
                                        placeholder="Keyword"
                                    />
                                    <div v-if="searchKeywordError !== ''" class="invalid-feedback">{{ searchKeywordError }}</div>
                                </div>
                                <div class="col-xl-4" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitAccountSearch" >Search</button>
                                </div>
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
    </main>
</template>

<script>
import axios from "axios";
import * as constants from "@/shared/Constants";
import { HollowDotsSpinner } from 'epic-spinners'


export default {
    name: 'accounts',
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
            searchType: "",
            accountsData: "",
            showDownloadBtn: "",
            loading: false,
            downloadData: [],
            searchKeywordBlurred: false,
            instanceIdBlurred: false,
            searchKeywordError: "",
            instanceIdError: ""
        }
    },
    methods: {
        isValidKeyword(keyword) {
            return keyword.trim() !== '';
        },
        isValidInstance(instanceId) {
            return instanceId.trim() !== '';
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
        submitAccountSearch(){
            this.searchKeywordError = "";
            this.instanceIdError = "";

            if (!this.isValidInstance(this.instanceId)) {
                this.instanceIdError = "Please choose a valid Mastodon instance";
            }

            if (!this.isValidKeyword(this.searchKeyword)) {
                this.searchKeywordError = "A keyword is required";
            }

            if(this.isValidInstance(this.instanceId) && this.isValidKeyword(this.searchKeyword)) {
                this.loading = true;
                let dataUrl = constants.url + '/api/search-status-by-keyword?keyword=' + this.searchKeyword + '&mastodon_instance=' + this.instanceId + '&type=accounts';
                axios.get(dataUrl)
                    .then(res => {
                        this.singleStatusData = res;
                        this.accountsData = res.data.accounts;
                        console.log(this.accountsData)
                        this.downloadData = this.accountsData
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