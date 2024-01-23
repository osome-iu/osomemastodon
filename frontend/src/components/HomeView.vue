<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="page-title">OSoMe Mastodon Search</h1>
            <div class="col-12">
                <div class="alert alert-info">
                    <p>
                        The Mastodon search interface enables users to discover and explore content efficiently. Users can input keywords, including hashtags, to find specific statuses, accounts, or trending topics. </p>
                </div>
            </div>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-xl-12">
                        <div class="api-section">
                            <h3>1. Get Statuses</h3>
                            <ul class="api-list">
                                <li>Search by keyword</li>
                                <li>Most recent by hashtag</li>
                                <li>Recent for instance</li>
                                <li>Single status by Id</li>
                            </ul>
                        </div>
                        <div class="api-section">
                            <h3>2. Get Accounts</h3>
                            <ul class="api-list">
                                <li>Search by keyword</li>
                                <li>Single account by Id</li>
                            </ul>
                        </div>
                        <div class="api-section">
                            <h3>3. Get Hashtag Metadata</h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<style scoped>
/*!* Add your custom styling here *!*/

/*!* General Styles *!*/
/*.container-fluid {*/
/*    padding: 20px;*/
/*}*/


/*!* Page Description *!*/
/*.page-description {*/
/*    font-size: 1.2rem;*/
/*    color: #555;*/
/*    margin-bottom: 20px;*/
/*}*/

/*!* Section Title *!*/
/*.section-title {*/
/*    color: #0a53be;*/
/*}*/

/*!* API Section *!*/
/*.api-section {*/
/*    margin-bottom: 30px;*/
/*}*/

/*!* API List *!*/
/*.api-list {*/
/*    list-style-type: none;*/
/*    padding: 0;*/
/*    margin: 0;*/
/*}*/

/*!* API Description *!*/
/*.api-description {*/
/*    color: #555;*/
/*}*/
</style>
<script setup>
</script>