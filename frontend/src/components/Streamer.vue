<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Streamer</h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>This is the mastodon aggregated streamer. Here is how to setup.</p>
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
            show_json: false
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
            let dataUrl = constants.url + '/api/search-status-by-keyword?keyword='+this.searchKeyword+'&mastodon_instance='+this.instanceId;
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