<template>
    <main>
        <div class="container-fluid px-4">
            <h2 class="page-title">API Documentation</h2>
            <div style="margin-left:30px">
                <h4 style="margin-top:20px">Our custom Mastodon search endpoints</h4>
                <ol>
                    <li class= "list-item" v-scroll-to="'#api-1'">Statuses - Search by keyword</li>
                    <li class= "list-item" v-scroll-to="'#api-2'">Statuses - Search by hashtag</li>
                    <li class= "list-item" v-scroll-to="'#api-3'">Statuses - Most recent</li>
                    <li class= "list-item" v-scroll-to="'#api-4'">Status - Single status by id</li>
                    <li class= "list-item" v-scroll-to="'#api-5'" >Accounts - Search by keyword</li>
                    <li class= "list-item" v-scroll-to="'#api-6'">Account - Single Account by id</li>
                    <li class= "list-item" v-scroll-to="'#api-7'">Get hashtag metadata</li>
                    <li class= "list-item" v-scroll-to="'#api-8'" >Mastodon instances - Get Mastodon instances</li>
                </ol>
            </div>



<!--            1. Status - Search by keyword API-->
            <div id="api-1">
                <h4 class="mt-4">1. Statuses - Search by keyword</h4>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>The OSoMe Mastodon Search API for statuses search by keyword, facilitates the search for statuses across multiple Mastodon instances for a given keyword. You can access the official Mastodon documentation <a href="https://docs.joinmastodon.org/methods/search/" target="_blank" class="navigation-link" aria-label="here">here</a> for further insight. </p>

                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                curl -X POST -H "Content-Type: application/json" -d '{"mastodon_instances":[{"name":"INSTANCE_NAME_1"},{"name":"INSTANCE_NAME_2"}],"keyword":"SEARCH_KEYWORD","access_keys":["ACCESS_KEY_1","ACCESS_KEY_2"]}' "https://osome.iu.edu/tools/mastodon/api/search-status-by-keyword"
                            </code>
                        </div>
                    </div>
                    <div style="margin-left:15px">
                        <p style="padding-top: 10px;"><b>Request</b></p>
                        <div style="margin-left:20px">
                            <ul>
                                <li><b>Headers</b></li>
                                <ul>
                                    <li>Content-Type: application/json</li>
                                </ul>
                                <li><b>Parameters</b></li>
                                <ul>
                                    <li><b>mastodon_instances</b> (array): List of Mastodon instances with their names.</li>
                                    <li><b>keyword</b> (string): (Required) The search keyword.</li>
                                    <li><b>access_tokens</b> (array): List of access tokens for each mastodon instance.</li>
                                </ul>
                            </ul>
                        </div>
                        <p><b>Note</b></p>
                        <ul>
                            <li>Data is returned in JSON format.</li>
                        </ul>
                    </div>
                </div>
            </div>


<!--            2. Status - Most recent by hashtag API            -->
            <div id="api-2">
                <h4 class="mt-4">2. Statuses - Search by hashtag</h4>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>The OSoMe Mastodon Search API for statuses search by hashtag, allows users to retrieve most recent statuses that contain a given hashtag across multiple Mastodon instances. You can access the official Mastodon documentation <a href="https://docs.joinmastodon.org/methods/timelines/#tag" target="_blank" class="navigation-link" aria-label="here"> here</a> for further insight.</p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                curl -X POST -H "Content-Type: application/json" -d '{"hashtag":"HASHTAG_NAME","mastodon_instances":[{"name":"MASTODON_INSTANCE"}],"data_type":"true/false","limit_no":"LIMIT_NO"}' "https://osome.iu.edu/tools/mastodon/api/hashtag-search"
                            </code>
                        </div>
                    </div>
                    <div style="margin-left:15px">
                        <p style="padding-top: 10px;"><b>Request</b></p>
                        <div style="margin-left:20px">
                            <ul>
                                <li><b>Headers</b></li>
                                <ul>
                                    <li>Content-Type: application/json</li>
                                </ul>
                                <li><b>Parameters</b></li>
                                <ul>
                                    <li><b>mastodon_instances</b> (array): List of Mastodon instances with their names.</li>
                                    <li><b>hashtag</b> (string): The hashtag to fetch data for.</li>
                                    <li><b>data_type</b> (boolean): Indicates whether to include local data (true/false).</li>
                                    <li><b>limit_no</b> (integer): The maximum number of statuses to retrieve.</li>
                                </ul>
                            </ul>
                        </div>
                        <p><b>Note</b></p>
                        <ul>
                            <li>Data is returned in JSON format.</li>
                        </ul>
                    </div>
                </div>
            </div>

<!--            3. Status - Most recent for instance API-->
            <div id="api-3">
                <h4 class="mt-4">3. Statuses - Most recent</h4>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>The OSoMe Mastodon Search API for the most recent statuses for instances, allows you to retrieve a list of public statuses that users on the platform have shared across multiple Mastodon instances. You can access the official Mastodon documentation <a href="https://docs.joinmastodon.org/methods/timelines/#public" target="_blank" class="navigation-link" aria-label="here"> here</a> for further insight. </p>

                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                curl -X POST -H "Content-Type: application/json" -d '{"mastodon_instances":[{"name":"MASTODON_INSTANCE"}],"data_type":"TRUE/FALSE","limit_no":"LIMIT"}' "https://osome.iu.edu/tools/mastodon/api/timeline-statuses"
                            </code>
                        </div>
                    </div>
                    <div style="margin-left:15px">
                        <p style="padding-top: 10px;"><b>Request</b></p>
                        <div style="margin-left:20px">
                            <ul>
                                <li><b>Headers</b></li>
                                <ul>
                                    <li>Content-Type: application/json</li>
                                </ul>
                                <li><b>Parameters</b></li>
                                <ul>
                                    <li><b>mastodon_instances</b> (array): List of Mastodon instances with their names.</li>
                                    <li><b>limit_no</b> (integer): The maximum number of statuses to retrieve.</li>
                                    <li><b>data_type</b> (boolean): Indicates whether to include local data (true/false). [true - Local data, false - Federated data]</li>
                                </ul>
                            </ul>
                        </div>
                        <p><b>Note</b></p>
                        <ul>
                            <li>Data is returned in JSON format.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!--            4. Status - Single status by Id API            -->
            <div id="api-4">
                <h4 class="mt-4">4. Status - Single status by id</h4>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>The OSoMe Mastodon Search API for status search by status by id, facilitates searching for a status from a Mastodon instance using a given status id. You can access the official Mastodon documentation <a href="https://docs.joinmastodon.org/methods/statuses/#get" target="_blank" class="navigation-link" aria-label="here"> here</a> for further insight. </p>
                </div>
                <div style="margin-left:20px">

                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://osome.iu.edu/tools/mastodon/api/search-status-by-id?status_id={STATUS_ID}&mastodon_instance={MASTODON_INSTANCE}
                            </code>
                        </div>
                    </div>
                    <div style="margin-left:15px">
                        <p style="padding-top: 10px;"><b>Request</b></p>
                        <div style="margin-left:20px">
                            <ul>
                                <li><b>Headers</b></li>
                                <ul>
                                    <li>Content-Type: application/json</li>
                                </ul>
                                <li><b>Parameters</b></li>
                                <ul>
                                    <li><b>mastodon_instance</b> (string): The Mastodon instance name.</li>
                                    <li><b>status_id</b>: The mastodon specific status id you want to search.</li>
                                </ul>
                            </ul>
                        </div>
                        <p><b>Note</b></p>
                        <ul>
                            <li>Data is returned in JSON format.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!--            5. Accounts - Search by keyword            -->
            <div id="api-5">
                <h4 class="mt-4">5. Accounts - Search by keyword</h4>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>The OSoMe Mastodon Search API for accounts search by keyword, facilitates to retrieve accounts across multiple Mastodon instances for a given keyword. You can access the official Mastodon documentation <a href="https://docs.joinmastodon.org/methods/search/" target="_blank" class="navigation-link" aria-label="here"> here</a> for futher insight.</p>

                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                curl -X POST -H "Content-Type: application/json" -d '{"keyword":"SEARCH_KEYWORD","instances":[{"name":"INSTANCE_1"},{"name":"INSTANCE_2"}]}' "https://osome.iu.edu/tools/mastodon/api/search-accounts-by-keyword"
                            </code>
                        </div>
                    </div>
                    <div style="margin-left:20px">
                        <p style="padding-top: 10px;"><b>Request</b></p>
                        <div style="margin-left:20px">
                            <ul>
                                <li><b>Headers</b></li>
                                <ul>
                                    <li>Content-Type: application/json</li>
                                </ul>
                                <li><b>Parameters</b></li>
                                <ul>
                                    <li><b>instances</b> (array): List of Mastodon instances with their names.</li>
                                    <li><b>keyword</b> (string): (Required) The search keyword.</li>
                                </ul>
                            </ul>
                        </div>
                        <p><b>Note</b></p>
                        <ul>
                            <li>Data is returned in JSON format.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!--            6. Accounts - Single Account by Id           -->
            <div id="api-6">
                <h4 class="mt-4">6. Account - Single Account by id</h4>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>The OSoMe Mastodon Search API for account search by account id, allows you to retrieve account information from a Mastodon instance for the given account id. You can access the official Mastodon documentation <a href="https://docs.joinmastodon.org/methods/accounts/#get" target="_blank" class="navigation-link" aria-label="here"> here</a> for further insight. </p>

                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://osome.iu.edu/api/account-search-by-id?mastodon_instance={mastodon_instance}&account_id={account_id}
                            </code>
                        </div>
                    </div>
                    <div style="margin-left:15px">
                        <p style="padding-top: 10px;"><b>Request</b></p>
                        <div style="margin-left:20px">
                            <ul>
                                <li><b>Headers</b></li>
                                <ul>
                                    <li>Content-Type: application/json</li>
                                </ul>
                                <li><b>Parameters</b></li>
                                <ul>
                                    <li><b>mastodon_instance</b> (string): The Mastodon instance name.</li>
                                    <li><b>account_id</b> (string): The unique identifier for the Mastodon account.</li>
                                </ul>
                            </ul>
                        </div>
                        <p><b>Note</b></p>
                        <ul>
                            <li>When retrieving some of the account information, there may be instances where certain data is not available or not returned by the Mastodon API because of their privacy policies.</li>
                            <li>Data is returned in JSON format.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!--            7. Get Hashtag metadata          -->
            <div id="api-7">
                <h4 class="mt-4">7. Get hashtag metadata</h4>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>The OSoMe Mastodon Search API for get hashtag metadata, facilitates to get a list of hashtags that include a given search term and links to statuses including those hashtags.  You can access the official Mastodon documentation <a href="https://docs.joinmastodon.org/methods/search/" target="_blank" class="navigation-link" aria-label="here"> here</a> for further insight. </p>

                    <div class="code-content">
                        <code>
                            curl -X POST -H "Content-Type: application/json" -d '{"keyword":"SEARCH_KEYWORD","instances":[{"name":"MASTODON_INSTANCE}}' "https://osome.iu.edu/tools/mastodon/api/search-hashtag-by-keyword"
                        </code>
                    </div>
                    <div style="margin-left:15px">
                        <p style="padding-top: 10px;"><b>Request</b></p>
                        <div style="margin-left:20px">
                            <ul>
                                <li><b>Headers</b></li>
                                <ul>
                                    <li>Content-Type: application/json</li>
                                </ul>
                                <li><b>Parameters</b></li>
                                <ul>
                                    <li><b>mastodon_instances</b> (array): List of Mastodon instances with their names.</li>
                                    <li><b>search_keyword</b> (string): The search keyword.</li>
                                </ul>
                            </ul>
                        </div>
                    </div>
                    <p><b>Note</b></p>
                    <ul>
                        <li>Data is returned in JSON format.</li>
                    </ul>
                </div>
            </div>



            <!--            8. Instance - Get Mastodon Instances API-->
            <div id="api-8">
                <h4 class="mt-4">8. Mastodon Instances - Get Mastodon instances</h4>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>The OSoMe Mastodon Search API to retrieve Mastodon instances, allows to grab the top 20 Mastodon instances with a minimum of 5000 active users and lists them in descending order by active users. Please visit <a href="https://instances.social/api/doc/" target="_blank" class="navigation-link" aria-label="instances.social">instances.social</a> for further insight.</p>

                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://osome.iu.edu/tools/mastodon/api/get-instance-data
                            </code>
                        </div>
                    </div>
                    <div style="margin-left:15px">
                        <p style="padding-top: 10px;"><b>Request</b></p>
                        <div style="margin-left:20px">
                            <ul>
                                <li><b>Headers</b></li>
                                <ul>
                                    <li>Content-Type: application/json</li>
                                </ul>
                            </ul>
                            <p><b>Note</b></p>
                            <ul>
                                <li>Data is returned in JSON format.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import VueScrollTo from 'vue-scrollto';
export default {
    name: "FAQ",
    mounted() {
        const id = this.$route.hash.slice(1);
        if (id) {
            if (id) {
                VueScrollTo.scrollTo('#' + id, 500, { offset: -65 });
            }
        }
    }
}
</script>


<style>
.code-box {
    width: 100%;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

.code-content {
    white-space: pre-wrap;
    overflow-x: auto; /* Enable horizontal scrolling on small screens if necessary */
    font-size: 14px; /* Adjust font size for better readability */
    padding: 16px; /* Add padding for spacing */
    border: 1px solid #ddd; /* Add a border for better visibility */
    border-radius: 5px;
    width: 100%/* Add rounded corners for aesthetics */
}


.navigation-link {
    text-decoration: underline;
    color: #2c3e50; /* Adjust the color as needed */
    /* Adding a transition for a smoother effect */
    transition: text-decoration 0.3s;
}
.navigation-link:hover {
    color: blue;
    text-decoration: none;
}

.list-item{
    cursor: pointer;
}
.list-item:hover {
    color: blue;
    text-decoration: underline;
}
</style>
<script setup>
</script>