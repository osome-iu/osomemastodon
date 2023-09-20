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
                                    <input class="form-control" type="password" placeholder="Client Key" aria-label="Search for..." aria-describedby="btnNavbarSearch" v-model="clientKey" @keyup.enter="getBearerTokenResearchAPI"/>
                                </div>
                                <div class="col-xl-3">
                                    <label> Client Secret</label>
                                    <input class="form-control" type="password" placeholder="Client Secret" aria-label="Search for..." aria-describedby="btnNavbarSearch" v-model="clientSecret" @keyup.enter="getBearerTokenResearchAPI"/>
                                </div>
                                <div class="col-xl-3">
                                    <label> &nbsp;Search Keyword</label>
                                    <input class="form-control" type="password" placeholder="Client Secret" aria-label="Search for..." aria-describedby="btnNavbarSearch" v-model="clientSecret" @keyup.enter="getBearerTokenResearchAPI"/>
                                </div>
                                <div class="col-xl-2">
                                    <label> &nbsp;Search Type</label>
                                    <input class="form-control" type="password" placeholder="Client Secret" aria-label="Search for..." aria-describedby="btnNavbarSearch" v-model="clientSecret" @keyup.enter="getBearerTokenResearchAPI"/>
                                </div>
                                <div class="col-xl-3" style="margin-top: 23px;">
                                    <button type="button" class="btn btn-success" :onclick="getBearerTokenResearchAPI">Search</button>
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
import {mapActions, mapGetters} from 'vuex';

export default {
    name: 'VideoAccountInfo',
    data() {
        return {
            clientKey: null,
            clientSecret: null,
            token: null,
        }
    },
    methods: {
        ...mapActions(['updateBearerToken']),
        getBearerTokenResearchAPI() {
            let dataUrl = constants.url + '/getbearertoken?client_key=' + this.clientKey + '&client_secret=' + this.clientSecret;
            axios.get(dataUrl)
                .then(res => {
                    let response = res.data.bearer_token
                    this.updateBearerToken(response);
                    this.token = response
                }).catch(error => {
                    console.log(error);
            });
        }
    },
    mounted() {
        this.token = this.getBearerToken;
    },
    computed: {
        ...mapGetters(['getBearerToken']),
    },
}
</script>