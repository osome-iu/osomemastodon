<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Hashtag </h1>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Search by keyword - <a href="https://docs.joinmastodon.org/methods/timelines/#public" target="_blank">Documetation</a>
                        </div>
                        <div class="card-body">
                            <div class="row align-items-center">
                                <div class="col-xl-2">
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
                                <div class="col-xl-2">
                                    <label> Hashtag</label>
                                    <input class="form-control" type="text" placeholder="Hashtag" aria-label="Search for..." aria-describedby="btnNavbarSearch" v-model="hashtagSearch"/>
                                </div>
                                <div class="col-xl-2">
                                    <label> Data</label>
                                    <select v-model="dataType"
                                            label="Data Get"
                                            class="form-control">
                                        <option disabled value="">Choose Data</option>
                                        <option value="public">Public</option>
                                        <option value="local">Local</option>
                                    </select>
                                </div>
                                <div class="col-xl-2">
                                    <label> Limit</label>
                                    <select v-model="limitNo"
                                            label="Limit"
                                            class="form-control">
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
                                </div>
                                <div class="col-xl-4" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitHashtagSearch" >Search</button>
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
                            <div class="table-responsive" v-if="!loading">
                                <table class="table table-bordered">
                                    <thead>
                                    <tr>
                                        <th scope="col">ID</th>
                                        <th scope="col" style="width: 10px;">Content</th>
                                        <th scope="col">In reply</th>
                                        <th scope="col">In reply Id </th>
                                        <th scope="col">Created At </th>
                                        <th scope="col">Mentions </th>
                                        <th scope="col">Tags </th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr v-for="hashtag in hashtagArray" :key="key">
                                        <td>{{hashtag.id}}</td>
                                        <td>{{hashtag.content}}</td>
                                        <td>{{hashtag.in_reply_to_account_id}}</td>
                                        <td>{{hashtag.in_reply_to_id}}</td>
                                        <td>{{hashtag.created_at}}</td>
                                        <td>{{hashtag.mentions}}</td>
                                        <td>{{hashtag.tags}}</td>
                                    </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="row" style="margin-top: 23px; float: right;" v-if="!loading && hashtagArray.length">
                                <div class="col-md-12 text-right">
                                    <button type="button" class="btn btn-primary" @click="downloadJSON">Download JSON</button>
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

export default {
    name: 'singleStatus',
    data() {
        return {
            clientKey: null,
            clientSecret: null,
            instanceData:[],
            limitNo: "",
            dataType: "",
            hashtagSearch: "",
            hashtagArray: []
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
        submitHashtagSearch(){
            let dataUrl = constants.url + '/api/hashtag-search?mastodon_instance='+this.instanceId+'&hashtag='+this.hash +'&limit='+this.limitNo +'&data_type='+this.dataType;
            this.clearAllFields()
            axios.get(dataUrl)
                .then(res => {
                    this.hashtagArray = res.data.hashtag
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
            const blob = new Blob([JSON.stringify(this.hashtagArray)], { type: 'application/json' });

            // Create a download link
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'hastag_data-'+this.hashtagSearch+'.json';

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