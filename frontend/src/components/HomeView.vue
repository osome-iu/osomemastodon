<template>
    <main>
        <div class="container-fluid px-4">
            <h4 class="page-title">OSoMe Mastodon Search</h4>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>The Mastodon search interface enables users to discover and explore content efficiently. Users can input keywords, including hashtags, to find specific statuses, accounts, or trending topics. </p>
                </div>
            </div>
            <hr>
            <div class="main-content">
                <div class="row">
                    <div class="col-xl-12">
                        <div class="api-section">
                            <p class="api-header-section">Documentation</p>
                            <ul class="api-list">
                                <li class="api-element">FAQ</li>
                                <li class="api-element">API Documentation</li>
                            </ul>
                        </div>
                        <div class="api-section">
                            <p class="api-header-section">Get statuses</p>
                            <ul class="api-list">
                                <li class="api-element">Search by keyword</li>
                                <li class="api-element">Most recent by hashtag</li>
                                <li class="api-element">Recent for instance</li>
                                <li class="api-element">Single status by Id</li>
                            </ul>
                        </div>
                        <div class="api-section">
                            <p class="api-header-section">Get accounts</p>
                            <ul class="api-list">
                                <li class="api-element">Search by keyword</li>
                                <li class="api-element">Single account by Id</li>
                            </ul>
                        </div>
                        <div class="api-section">
                            <p class="api-header-section">Get hashtag metadata</p>
                            <ul class="api-list">
                                <li class="api-element">Hashtag Metadata</li>
                            </ul>
                        </div>
                        <div class="api-section">
                            <p class="api-header-section">Instances</p>
                            <ul class="api-list">
                                <li class="api-element">Mastodon Instances</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<style scoped>

.main-content{
    margin-left:200px;
    margin-top:20px;
}
.page-title{
}

.api-header-section {
    font-size: 16px;
    font-weight: bold;
    position: relative;
    background-color: #4BB543; /* Green color */
    color: #fff; /* White text color */
    padding: 10px 12px; /* Adjust padding as needed */
    border-radius: 0 0 10px 0; /* Rounded corners */
    display: inline-block;
}

.api-header-section::after {
    content: "";
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    left: 100%;
    margin-left: -6px; /* Adjust as needed */
    width: 0;
    height: 0;
    border-style: solid;
    border-width: 6px 0 6px 6px; /* Adjust size of the arrow */
    border-color: transparent transparent transparent #4CAF50; /* Arrow color */
}

.api-list {
    list-style-type: none; /* Remove default list styles */
    padding: 0; /* Remove default padding */
}

.api-element {
    display: block;
    padding: 10px;
    margin: 5px;
    border: none;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
    border-radius: 5px;
    color: #dde0e3; /* Text color */
    background-color: #151C62; /* Button color */
    transition: background-color 0.3s ease;
    min-width:150px;
    max-width: 300px;
}

/* Change button background color on hover */
.api-element:hover {
    background-color: #0056b3; /* Updated button color on hover */
}

@media (max-width: 768px) {
    .main-content {
        margin-left: 20px; /* Adjust the margin for smaller screens */
    }
}
</style>
<script setup>
</script>