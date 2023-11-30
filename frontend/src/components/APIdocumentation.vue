<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="page-title">API Documentation</h1>
            <div style="margin-left:50px">
                <h5 style="margin-top:20px">API Endpoints</h5>
                <ol>
                    <li>Instance - Get Mastodon Instances API</li>
                    <li>Status - Search by keyword API</li>
                    <li>Status - Most recent by hashtag API</li>
                    <li>Status - Most recent for instance API</li>
                    <li>Status - Single status by ID API</li>
                    <li>Accounts - Search by keyword</li>
                    <li>Accounts - Single Acccount by Id</li>
                    <li>Status - Single status by ID API</li>
                    <li>Get Hashtag metadata</li>
                </ol>
            </div>
<!--            Instance - Get Mastodon Instances API-->
            <h4 class="mt-4">1. Instance - Get Mastodon Instances API</h4>
            <div style="margin-left:20px">
                <h6>Overview</h6>
                <p>The Mastodon Instances API provides a list of Mastodon instances based on specified criteria, including minimum active users, count, sorting, and authorization. You can access the official documentation from <a href="https://instances.social/api/doc/" target="_blank" class="navigation-link" aria-label="here"> here</a>.</p>
                <h6>Official API Endpoint</h6>
                <div class="code-box">
                    <div class="code-content">
                        <code>
                            GET https://instances.social/api/1.0/instances/list
                        </code>
                    </div>
                </div>
                <div style="margin-left:15px">
                    <h6 style="padding-top: 10px;">Request</h6>
                         <div style="margin-left:20px">
                             <ul>
                                 <li><b>Method</b> : GET</li>
                                 <li><b>URL</b> : https://instances.social/api/1.0/instances/list</li>
                                 <li><b>Headers</b>: </li>
                                <ul>
                                    <li>Authorization: Bearer YOUR_API_KEY</li>
                                </ul>
                             </ul>
                         </div>
                </div>
                <h6>OSoMe API Endpoint</h6>
                <div class="code-box">
                    <div class="code-content">
                        <code>
                            GET https://osome.iu.edu/tools/mastodon/api/get-instance-data
                        </code>
                    </div>
                </div>
                <div style="margin-left:15px">
                    <h6 style="padding-top: 10px;">Request</h6>
                    <div style="margin-left:20px">
                        <ul>
                            <li><b>Method</b> : GET</li>
                            <li><b>URL</b> : https://osome.iu.edu/tools/mastodon/api/get-instance-data</li>
                        </ul>
                    </div>
                </div>
                <h6>Note</h6>
                <ul>
                    <li>Data is returned in JSON format.</li>
                </ul>
            </div>
<!--            Status - Search by keyword API-->
            <h4 class="mt-4">2. Status - Search by keyword API</h4>
            <div style="margin-left:20px">
                <h6>Overview</h6>
                <p>The Search API provides a method to retrieve accounts, statuses, and hashtags based on a specified search keyword. In this API, we get the statuses results as a json format. You can access the official documentation from <a href="https://docs.joinmastodon.org/methods/search/" target="_blank" class="navigation-link" aria-label="here"> here</a>. </p>
                <h6>Official API Endpoint</h6>
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
                    <h6 style="padding-top: 10px;">Headers</h6>
                    <p>The following header must be included in the request:</p>
                    <ul>
                        <li><b>Authorization</b> :Bearer token for authentication</li>
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
                    <h6 style="padding-top: 10px;">Request Example (POST request)</h6>
                    <div class="code-box">
                        <div class="code-content">
                            <code>
                                curl --location 'https://{mastodon_instance}/api/v2/search?q={search_keyword}&type=statuses' --header 'Authorization: Bearer 'TOKEN'
                            </code>
                        </div>
                    </div>
                </div>
                <div style="margin-top:20px">

                </div>

                <h6>Note</h6>
                <ul>
                    <li>Ensure the provided access_token is a valid Bearer token.</li>
                    <li>The response includes lists of accounts, statuses, and hashtags. But only populated statuses as we specifically select it. </li>
                </ul>
            </div>
<!--            Status - Most recent by hashtag API            -->
            <h4 class="mt-4">3. Status - Most recent by hashtag API</h4>
            <div style="margin-left:20px">
                <h6>Overview</h6>
                <p>This API endpoint allows users to retrieve public hashtag information from a Mastodon instance. You can access the official documentation from <a href="https://instances.social/api/doc/" target="_blank" class="navigation-link" aria-label="here"> here</a>.</p>
                <h6>Official API Endpoint</h6>
                <div class="code-box">
                    <div class="code-content">
                        <code>
                            GET https://{mastodon_instance}/api/v1/timelines/tag/{hashtag}?limit={limit}&local={data_type}
                        </code>
                    </div>
                </div>
                <div style="margin-left:15px">
                    <h6 style="padding-top: 10px;">Request</h6>
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
                <h6>OSoMe API Endpoint</h6>
                <p>This API endpoint allows you to search public hashtag information through multiple Mastodon instances.</p>
                <div class="code-box">
                    <div class="code-content">
                        <code>
                            GET curl -X POST -H "Content-Type: application/json" -d '{"hashtag":"indiana","mastodon_instances":[{"name":"mastodon.social","active_users":145442,"all_users":"1716108"}],"data_type":"true","limit_no":"10"}' "https://osome.iu.edu/tools/mastodon/api/hashtag-search"
                        </code>
                    </div>
                </div>
                <div style="margin-left:15px">
                    <h6 style="padding-top: 10px;">Request</h6>
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
                    <p>Example Request Body</p>
                    <div class="code-box">
                        <div class="code-content" >
                            <code>
                                <pre>
                                    {
                                        "mastodon_instances": [
                                            {"name": "instance1"},
                                            {"name": "instance2"}
                                        ],
                                        "hashtag": "example_hashtag",
                                        "data_type": true,
                                        "limit_no": 10
                                    }
                                </pre>
                            </code>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>


<style>
.code-box {
    width: 900px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

.code-content {
    padding: 16px;
    white-space: pre-wrap;
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
</style>
<script setup>
</script>