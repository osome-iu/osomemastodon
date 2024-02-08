<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="page-title"><b>OSoMe Mastodon Search</b></h1>
            <div class="col-12">
                <div>
                    <p>OSoMe Mastodon interface provides diverse functionalities, allowing users to retrieve statuses, explore accounts, access hashtag metadata, discover Mastodon instances, and access comprehensive documentation. This empowers researchers to experiment with Mastodon data, enabling in-depth exploration and analysis for valuable insights.</p>
                </div>
            </div>
            <hr>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-xl-12">
                        <div class="api-section">
                            <h4>Get Statuses</h4>
                            <ul class="api-list">
                                <li><router-link to="/searchbykeyword"  class="home-sub-header">Search by keyword</router-link> - Search statuses across multiple instances using a given keyword. <b>An access token is required</b> for each instance being searched.</li>
                                <li><router-link to="/timelinehashtag"  class="home-sub-header">Search by hashtag</router-link> - Get the most recent statuses that contain the given hashtag.</li>
                                <li><router-link to="/timelinestatus"  class="home-sub-header">Recent for instance</router-link> - A  list of the most recent statuses. </li>
                                <li><router-link to="/searchbyid"  class="home-sub-header">Single status by id</router-link> - Get information about a status by status id.</li>
                            </ul>
                        </div>
                        <div class="api-section">
                            <h4>Get Accounts</h4>
                            <ol class="api-list">
                                <li><router-link to="/searchaccounts" class="home-sub-header">Search by keyword</router-link> - Search for accounts that contain a given keyword in the username or display name.</li>
                                <li><router-link to="/accountsbyId" class="home-sub-header">Single account by id</router-link> - Retrieve information about a profile using the account id.</li>
                            </ol>
                        </div>
                        <div class="api-section">
                            <h4> Get Hashtag Metadata</h4>
                            <ol class="api-list">
                                <li><router-link to="/searchhashtags" class="home-sub-header">Hashtag Metadata</router-link> - Get a list of hashtags that include a given search term and links to statuses including those hashtags.</li>
                            </ol>
                        </div>
                        <div class="api-section">
                            <h4>Instances</h4>
                            <ol class="api-list">
                                <li><router-link to="/instances" class="home-sub-header">Mastodon Instances</router-link> - Retrieves the top 20 Mastodon instances with a minimum of 5000 active users and lists them in descending order by active users. It utilizes the instances.social API to gather the instances.</li>
                            </ol>
                        </div>
                        <div class="api-section">
                            <h4> Documentation</h4>
                            <ol class="api-list">
                                <li><router-link to="/faq" class="home-sub-header">FAQ</router-link> - The FAQ section addresses common questions, providing quick insights and information about the Mastodon interface.</li>
                                <li><router-link to="/apidocumentation" class="home-sub-header">API Documentation</router-link> - Guide to interact with Mastodon APIs, presenting key information on endpoints, request formats, and response structures.</li>
                            </ol>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<style scoped>
/* Add your custom styling here */

/* General Styles */
.container-fluid {
    padding: 20px;
}

/* Page Description */
.page-description {
    font-size: 1.2rem;
    color: #555;
    margin-bottom: 20px;
}

/* Section Title */
.section-title {
    color: #0a53be;
}
/* API Section */
.api-section {
    margin-bottom: 20px;
}
/* API List */
.api-list {
    list-style-type: disc;
    padding: 0;
    margin: 0;
    margin-left:50px;
}
/* API Description */
.api-description {
    color: #555;
}

.home-sub-header{
    text-decoration: underline;
    color: #2c3e50;
}

.home-sub-header:hover{
    text-decoration: underline;
    color: blue
}
</style>