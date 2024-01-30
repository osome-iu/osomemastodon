<template>
    <main>
        <div class="container-fluid px-4">
            <h2 class="page-title">API Documentation</h2>
            <div style="margin-left:50px">
                <h3 style="margin-top:20px">API Endpoints</h3>
                <ol>
                    <li class= "list-item" v-scroll-to="'#api-1'" >Instance - Get Mastodon Instances API</li>
                    <li class= "list-item" v-scroll-to="'#api-2'">Status - Search by keyword API</li>
                    <li class= "list-item" v-scroll-to="'#api-3'">Status - Most recent by hashtag API</li>
                    <li class= "list-item" v-scroll-to="'#api-4'">Status - Most recent for instance API</li>
                    <li class= "list-item" v-scroll-to="'#api-5'">Status - Single status by Id API</li>
                    <li class= "list-item" v-scroll-to="'#api-6'" >Accounts - Search by keyword</li>
                    <li class= "list-item" v-scroll-to="'#api-7'">Accounts - Single Account by Id</li>
                    <li class= "list-item" v-scroll-to="'#api-8'">Get Hashtag metadata</li>
                </ol>
            </div>

<!--            Instance - Get Mastodon Instances API-->
            <div id="api-1">
                <h3 class="mt-4">1. Instance - Get Mastodon Instances API</h3>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>The Mastodon Instances API provides a list of Mastodon instances based on specified criteria, including minimum active users, count, sorting, and authorization. You can access the official documentation <a href="https://instances.social/api/doc/" target="_blank" class="navigation-link" aria-label="here"> here</a>.</p>
                    <p><b>Official API Endpoint</b></p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://instances.social/api/1.0/instances/list
                            </code>
                        </div>
                    </div>
                    <div style="margin-left:15px">
                        <p style="padding-top: 10px;"><b>Request</b></p>
                             <div style="margin-left:20px">
                                 <ul>
                                     <li><b>Method</b>: GET</li>
                                     <li><b>URL</b>: https://instances.social/api/1.0/instances/list</li>
                                     <li><b>Headers</b>: </li>
                                    <ul>
                                        <li>Authorization: Bearer access_token</li>
                                    </ul>
                                 </ul>
                             </div>
                    </div>
                    <p><b>OSoMe API Endpoint</b></p>
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
                                <li><b>Method</b>: GET</li>
                                <li><b>URL</b>: https://osome.iu.edu/tools/mastodon/api/get-instance-data</li>
                            </ul>
                        </div>
                    </div>
                    <p><b>Note</b></p>
                    <ul>
                        <li>Data is returned in JSON format.</li>
                    </ul>
                </div>
            </div>

<!--            Status - Search by keyword API-->
            <div id="api-2">
                <h3 class="mt-4">2. Status - Search by keyword API</h3>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>The Search API provides a method to retrieve accounts, statuses, and hashtags based on a specified search keyword. In this API, we get the statuses results as a json format. You can access the official documentation <a href="https://docs.joinmastodon.org/methods/search/" target="_blank" class="navigation-link" aria-label="here"> here</a>. </p>
                    <p><b>Official API Endpoint</b></p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://{mastodon_instance}/api/v2/search?q={search_keyword}&type=statuses&resolve=true
                            </code>
                        </div>
                    </div>
                    <div class="table-responsive" style="font-size: 12px; width:600px; margin-top:20px;">
                        <table class="table table-bordered">
                            <thead>
                            <tr>
                                <th scope="col">Name</th>
                                <th scope="col">Type</th>
                                <th scope="col">Description</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <td>access_token</td>
                                <td>string</td>
                                <td>(Required) Bearer token for retrieving statuses.</td>
                            </tr>
                            <tr>
                                <td>search_keyword</td>
                                <td>string</td>
                                <td>(Required) The search keyword.</td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                    <div style="margin-left:15px">
                        <p style="padding-top: 10px;"><b>Request</b></p>
                        <div style="margin-left:20px">
                            <ul>
                                <li><b>Method</b>: GET</li>
                                <li><b>URL</b>: https://instances.social/api/1.0/instances/list</li>
                                <li><b>Headers</b>: </li>
                                <ul>
                                    <li>Authorization: Bearer access_token</li>
                                </ul>
                            </ul>
                        </div>
                    </div>
                    <div style="margin-left:15px">
                        <p style="padding-top: 10px;"><b>Headers</b></p>
                        <p>The following header must be included in the request:</p>
                        <ul>
                            <li><b>Authorization</b>:Bearer token for authentication</li>
                        </ul>
                        <div class="code-box">
                            <div class="code-content">
                                <code>
                                    Authorization: Bearer {access_token}
                                </code>
                            </div>
                        </div>
                    </div>
                    <div>
                        <p style="padding-top: 10px;">Request Example (POST request)</p>
                        <div class="code-box">
                            <div class="code-content">
                                <code>
                                    curl --location 'https://{mastodon_instance}/api/v2/search?q={search_keyword}&type=statuses' --header 'Authorization: Bearer 'TOKEN'
                                </code>
                            </div>
                        </div>
                    </div>
                    <p><b>Note</b></p>
                    <ul>
                        <li>Ensure the provided access_token is a valid Bearer token.</li>
                        <li>The response includes lists of accounts, statuses, and hashtags. But only populated statuses as we specifically select it. </li>
                    </ul>
                    <p><b>OSoMe API Endpoint</b></p>
                    <p>The API endpoint facilitates the search for statuses across multiple Mastodon instances using a specified keyword. </p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                curl -X POST -H "Content-Type: application/json" -d '{"mastodon_instances":[{"name":"INSTANCE_NAME_1"},{"name":"INSTANCE_NAME_2"}],"keyword":"SEARCH_KEYWORD","access_tokens":["ACCESS_TOKEN_1","ACCESS_TOKEN_2"]}' "https://osome.iu.edu/tools/mastodon/api/search-status-by-keyword"
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
                    </div>
                </div>
            </div>


<!--            Status - Most recent by hashtag API            -->
            <div id="api-3">
                <h3 class="mt-4">3. Status - Most recent by hashtag API</h3>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>This API endpoint allows users to retrieve public hashtag information from a Mastodon instance. You can access the official documentation <a href="https://instances.social/api/doc/" target="_blank" class="navigation-link" aria-label="here"> here</a>.</p>
                    <p><b>Official API Endpoint</b></p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://{mastodon_instance}/api/v1/timelines/tag/{hashtag}?limit={limit}&local={data_type}
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
                                    <li><b>hashtag</b> (string): The hashtag to fetch data for.</li>
                                    <li><b>data_type</b> (boolean): Indicates whether to include local data (true/false).</li>
                                    <li><b>limit</b> (integer): The maximum number of statuses to retrieve.</li>
                                </ul>
                            </ul>
                        </div>
                    </div>
                    <p><b>OSoMe API Endpoint</b></p>
                    <p>This API endpoint allows you to search public hashtag information through multiple Mastodon instances.</p>
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
                    </div>
                </div>
            </div>

<!--            Status - Most recent for instance API-->
            <div id="api-4">
                <h3 class="mt-4">4. Most recent for instance API</h3>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>This API endpoint retrieves public timeline statuses from a Mastodon instance. You can access the official documentation <a href="https://docs.joinmastodon.org/methods/timelines/#public" target="_blank" class="navigation-link" aria-label="here"> here</a>. </p>
                    <p><b>Official API Endpoint</b></p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://{mastodon_instance}/api/v1/timelines/public?limit={limit}&local={data_type}
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
                                    <li><b>limit</b> (integer): The maximum number of statuses to retrieve.</li>
                                    <li><b>data_type</b> (boolean): Indicates whether to include local data (true/false). [true - Local data, false - Federated data]</li>
                                </ul>
                            </ul>
                        </div>
                    </div>
                    <p><b>OSoMe API Endpoint</b></p>
                    <p>This API endpoint retrieves public timeline statuses across multiple Mastodon instances. It accepts a JSON payload containing Mastodon instances and a search keyword.</p>
                    <p style="font-weight:bold">(POST Request)</p>
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
                    </div>
                </div>
            </div>

            <!--            Status - Single status by Id API            -->
            <div id="api-5">
                <h3 class="mt-4">5. Status - Single status by Id API</h3>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>This API method is used to search for statuses from a Mastodon instance based on a specific status Id. You can access the official documentation <a href="https://docs.joinmastodon.org/methods/statuses/#get" target="_blank" class="navigation-link" aria-label="here"> here</a>. </p>
                    <p><b>Official API Endpoint</b></p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://{mastodon_instance}/api/v1/statuses/{status_id}
                            </code>
                        </div>
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
                                <li><b>mastodon_instance</b>: This should be replaced with the domain of the Mastodon instance you are working with (e.g., mastodon.social)</li>
                                <li><b>status_Id</b> (string): This should be replaced with the ID of the specific status you want to retrieve</li>
                            </ul>
                        </ul>
                    </div>
                    <p><b>OSoMe API Endpoint</b></p>
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
                    </div>
                </div>
            </div>

            <!--            Accounts - Search by keyword            -->
            <div id="api-6">
                <h3 class="mt-4">6. Accounts - Search by keyword</h3>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>This API retrieves account data from a Mastodon instance based on a search keyword. You can access the official documentation <a href="https://docs.joinmastodon.org/methods/search/" target="_blank" class="navigation-link" aria-label="here"> here</a>. </p>
                    <p><b>Official API Endpoint</b></p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://{mastodon_instance}/api/v2/search?q={search_keyword}&type=accounts&resolve=true
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
                    </div>
                    <div>
                        <p style="padding-top: 10px;"><b>Request Example (POST request)</b></p>
                        <div class="code-box">
                            <div class="code-content">
                                <code>
                                    curl --location 'https://{mastodon_instance}/api/v2/search?q={search_keyword}&type=accounts' --header 'Authorization: Bearer 'TOKEN'
                                </code>
                            </div>
                        </div>
                    </div>
                    <p><b>Note</b></p>
                    <ul>
                        <li>Ensure the provided access_token is a valid Bearer token.</li>
                        <li>The response includes lists of accounts, statuses, and hashtags. But only get populated accounts as we specifically select it. </li>
                    </ul>
                    <p><b>OSoMe API Endpoint</b></p>
                    <p>The API endpoint facilitates the search for accounts across multiple Mastodon instances using a specified keyword. </p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                curl -X POST -H "Content-Type: application/json" -d '{"keyword":"SEARCH_KEYWORD","instances":[{"name":"INSTANCE_1"},{"name":"INSTANCE_2"}]}' "https://osome.iu.edu/tools/mastodon/api/search-accounts-by-keyword"
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
                                    <li><b>instances</b> (array): List of Mastodon instances with their names.</li>
                                    <li><b>keyword</b> (string): (Required) The search keyword.</li>
                                </ul>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <!--            Accounts - Single Account by Id           -->
            <div id="api-7">
                <h3 class="mt-4">7. Accounts - Single Account by Id</h3>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>This API endpoint retrieves account information from the Mastodon API based on the account ID and Mastodon instance name.  You can access the official documentation <a href="https://docs.joinmastodon.org/methods/search/" target="_blank" class="navigation-link" aria-label="here"> here</a>. </p>
                    <p><b>Official API Endpoint</b></p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://{mastodon_instance}/api/v1/accounts/{account_id}
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
                    </div>
                    <p><b>OSoMe API Endpoint</b></p>
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
                    </div>
                    <p><b>Note</b></p>
                    <ul>
                        <li>When retrieving some of the account information, there may be instances where certain data is not available or not returned by the Mastodon API.</li>
                    </ul>
                </div>
            </div>

            <!--            Get Hashtag metadata          -->
            <div id="api-8">
                <h3 class="mt-4">8. Get Hashtag metadata</h3>
                <div style="margin-left:20px">
                    <p><b>Overview</b></p>
                    <p>This API endpoint retrieves account information from the Mastodon API based on the account ID and Mastodon instance name.  You can access the official documentation <a href="https://docs.joinmastodon.org/methods/search/" target="_blank" class="navigation-link" aria-label="here"> here</a>. </p>
                    <p><b>Official API Endpoint</b></p>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                GET https://{mastodon_instance}/api/v2/search?q={search_keyword}&type=hashtags
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
                                    <li><b>search_keyword</b> (string): (Required) The search keyword.</li>
                                </ul>
                            </ul>
                        </div>
                    </div>
                    <p><b>OSoMe API Endpoint</b></p>
                    <p>This API endpoint for searching hashtag data through a hashtag keyword across multiple Mastodon instances. It accepts a JSON payload containing Mastodon instances and a search keyword.</p>
                    <p style="font-weight:bold">(POST Request)</p>
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
    width: 900px;
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
    border-radius: 5px; /* Add rounded corners for aesthetics */
}


.navigation-link {
    text-decoration: underline;
    color: #2c3e50; /* Adjust the color as needed */
    /* Adding a transition for a smoother effect */
    transition: text-decoration 0.3s;
}
.navigation-link:hover {
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