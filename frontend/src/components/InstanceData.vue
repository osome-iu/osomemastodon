<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">Mastodon Instances</h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>To get the mastodon instance, call <a href="">here</a>. This will grab the top 20 mastodon instances and with minimum 5000 active users in each instance and order in statuses descending.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-12">
                    <div class="card mb-4">
                        <div class="card-header">
                            <i class="fas fa-search"></i>
                            Get the instance data <a href="https://instances.social/api/doc/" target="_blank">Documetation</a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card mb-4">
                <div class="card-header">
                    <i class="fas fa-table me-1"></i>
                    Instances
                </div>
                <div class="card-body">
                    <div class="table-responsive">
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
                    <div class="alert alert-warning" v-if="instanceData.length === 0">
                        <fa icon="exclamation-triangle" /> No data available.
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
    name: 'InstanceData',
    data() {
        return {
           instanceData : [],
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
                this.instanceData = res.data.instances
            }).catch(error => {
            console.log(error);
        });
    },
    computed: {
    },
}
</script>