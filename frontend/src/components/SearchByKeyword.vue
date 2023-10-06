<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Status - Search By Keyword</h1>
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
                                        <option disabled value="">Choose the type
                                        </option>
                                        <option value="all">All</option>
                                        <option value="hashtags">Hashtags</option>
                                        <option value="statuses">Statuses</option>
                                        <option value="accounts">Accounts</option>
                                    </select>
                                </div>
                                <div class="col-xl-4" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitStatusSearch" >Search</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row" v-if="show_json">
                <div class="col-xl-12">
                    <textarea class="form-control" v-model="survey_json" style="height:600px "></textarea>
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
            instanceId: "",
            searchKeyword: "",
            show_json: false,
            searchType: "",
            survey_json: ""
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
        submitStatusSearch(){
            this.survey_json = ""
            let dataUrl = constants.url + '/api/search-status-by-keyword?keyword='+this.searchKeyword+'&mastodon_instance='+this.instanceId+'&type='+this.searchType;
            axios.get(dataUrl)
                .then(res => {
                    this.singleStatusData = res;
                    this.show_json = true;
                    this.survey_json = this.stringifyJSON(this.singleStatusData)
                }).catch(error => {
                console.log(error);
            });
        },
        stringifyJSON(stringobject) {
            return JSON.stringify(stringobject, function (key, value) {
                return value;
            }, 4);
        },
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>