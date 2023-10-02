<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Single Status</h1>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Search a single status - <a href="https://docs.joinmastodon.org/methods/statuses/#get" target="_blank">Documetation</a>
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
                                    <label> Status Id</label>
                                    <input class="form-control" type="text" placeholder="Status ID" aria-label="Search for..." aria-describedby="btnNavbarSearch" v-model="statusId"/>
                                </div>
                                <div class="col-xl-4" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="submitSingleStatus">Search</button>
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
            instanceId: null,
            statusId: null,
            singleStatusData:[],
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
        submitSingleStatus(){
            let dataUrl = constants.url + '/api/search-status-by-id?status_id='+this.statusId+'&mastodon_instance='+'https://'+this.instanceId;
            axios.get(dataUrl)
                .then(res => {
                    this.singleStatusData = res;
                    console.log(this.singleStatusData)
                }).catch(error => {
                console.log(error);
            });
        }
    },
    mounted() {
        this.fetchAllInstanceData();
    },
}
</script>