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
            <h4 class="mt-4">1. Instance - Get Mastodon Instances API</h4>
            <div style="margin-left:20px">
                <h6>Overview</h6>
                <p>The Mastodon Instances API provides a list of Mastodon instances based on specified criteria, including minimum active users, count, sorting, and authorization. You can access the official documentation from <a href="https://instances.social/api/doc/" target="_blank" class="navigation-link" aria-label="here"> here.</a></p>
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
                            GET https://osome.iu.edu/mastodon/api/get-instance-data
                        </code>
                    </div>
                </div>
                <div style="margin-left:15px">
                    <h6 style="padding-top: 10px;">Request</h6>
                    <div style="margin-left:20px">
                        <ul>
                            <li><b>Method</b> : GET</li>
                            <li><b>URL</b> : https://osome.iu.edu/mastodon/api/get-instance-data</li>
                        </ul>
                    </div>
                </div>
                <h6>Note</h6>
                <ul>
                    <li>Data is returned in JSON format.</li>
                </ul>
            </div>
            <h4 class="mt-4">2. Status - Search by keyword API</h4>
        </div>
    </main>
</template>
<script setup>
</script>


<style>
.code-box {
    width: 800px;
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