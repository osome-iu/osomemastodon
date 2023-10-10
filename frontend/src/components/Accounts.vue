<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Accounts</h1>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Search by keyword - <a href="https://docs.joinmastodon.org/methods/accounts/#get" target="_blank">Documetation</a>
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
                                    <label> Account Id</label>
                                    <input class="form-control" type="text" placeholder="Account Id" aria-label="Search for..." aria-describedby="btnNavbarSearch" v-model="accountId"/>
                                </div>
                                <div class="col-xl-4" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitAccountSearch" >Search</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-table me-1"></i>
                            Account Information
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
                                    <textarea class="form-control" placeholder="Note" v-model="this.note" readonly></textarea>
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
        </div>
    </main>
</template>

<script>
import axios from "axios";
import * as constants from "@/shared/Constants";

export default {
    name: 'singleStatus',
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
            survey_json: "",
            displayName: "",
            followersCount: "",
            followingCount: "",
            statusCount: "",
            lastStatusAt: "",
            username: "",
            bot: "",
            avatarLink: "",
            note: "",
        }
    },
    methods: {
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
            this.survey_json = ""
            let dataUrl = constants.url + '/api/account-search-by-id?mastodon_instance='+this.instanceId+'&account_id='+this.accountId;
            this.clearAllFields()
            axios.get(dataUrl)
                .then(res => {
                    this.accountData = res.data;
                    this.username = res.data.username;
                    this.displayName = res.data.display_name;
                    this.followersCount = res.data.followers_count;
                    this.followingCount = res.data.following_count;
                    this.statusCount = res.data.statuses_count;
                    this.bot = res.data.bot;
                    this.avatarLink = res.data.avatar;
                    this.note = res.data.note;
                }).catch(error => {
                console.log(error);
            });
        },
        stringifyJSON(stringobject) {
            return JSON.stringify(stringobject, function (key, value) {
                return value;
            }, 4);
        },
        downloadJSON(){
            // Create a Blob containing the JSON data
            const blob = new Blob([JSON.stringify(this.accountData)], { type: 'application/json' });

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