<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="page-title">Instances</h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>Retrieves the top 20 instances with a minimum of 5000 active users and lists them in descending order by active users. It utilizes the <a href="https://instances.social/api/doc/" target="_blank"  aria-label="here" style="color: #2c3e50;">instances.social</a> API to gather the instances. You can access the documentation <router-link to="/apidocumentation#api-8" target="_blank" class="api-documentation">here</router-link>.</p>
                </div>
            </div>

            <div class="card mb-4">
                <div class="card-header">
                    Results
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
                    <div class="table-responsive" v-if="!loading" style="font-size: 10px">
                        <table class="table table-bordered">
                            <thead>
                            <tr>
                                <th scope="col">Name</th>
                                <th scope="col">Active Users</th>
                                <th scope="col">Users</th>
                                <th scope="col">Statuses</th>
                                <th scope="col">OBS Rank</th>
                                <th scope="col">Open Registration</th>
                                <th scope="col">Checked At</th>
                                <th scope="col">Prohibited Contents</th>
                                <th scope="col">Short Description</th>
                                <th scope="col">Link</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="instance in instanceData" :key="key">
                                <td>{{instance.name}}</td>
                                <td>{{instance.active_users}}</td>
                                <td>{{instance.users}}</td>
                                <td>{{instance.statuses}}</td>
                                <td>{{instance.obs_rank}}</td>
                                <td>{{instance.open_registrations}}</td>
                                <td>{{new Date(instance.checked_at).toLocaleString('en-US')}}</td>
                                <td>{{(instance.info.prohibited_content).join(', ')}}</td>
                                <td>{{instance.info.short_description}}</td>
                                <td><button type="button" class="btn btn-primary btn-sm" @click="navigateToInstance(instance.name)">view</button></td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="alert alert-warning" v-if="instanceData.length === 0 & !loading">
                        <i class="fas fa-exclamation"></i> No data available.
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
    name: 'InstanceData',
    components: {
        HollowDotsSpinner,
    },
    data() {
        return {
           instanceData : [],
           loading: true,
        }
    },
    methods: {
        navigateToInstance(name){
            window.open(
                `https://${name}`,
                "_blank"
            );
        }
    },
    mounted() {
        let dataUrl = constants.url + '/api/get-instance-data';
        axios.get(dataUrl)
            .then(res => {
                this.instanceData = res.data.instances;
                this.instanceData.sort((a, b) => b.active_users - a.active_users);
                this.loading = false
            }).catch(error => {
            console.log(error);
        });
    },
    computed: {
    },
}
</script>

<style scoped>
.api-documentation{
    text-decoration : underline;
}
</style>
