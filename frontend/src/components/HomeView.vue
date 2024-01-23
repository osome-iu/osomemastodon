<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="page-title"><b>OSoMe Mastodon Search</b></h1>
            <div class="col-12">
                <div>
                    <p>OSoMe Mastodon interface provides diverse functionalities, allowing users to retrieve statuses, explore accounts, access hashtag metadata, discover Mastodon instances, and access comprehensive documentation.This empowers researchers to experiment with Mastodon data, enabling in-depth exploration and analysis for valuable insights.</p>
                </div>
            </div>
            <hr>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-xl-12">
                        <div class="api-section">
                            <h4>1. Get Statuses</h4>
                            <ul class="api-list">
                                <li><router-link to="/searchbykeyword"  class="api-documentation">Search by keyword</router-link> - Search for statuses for a given keyword. This function allows to search across multiple instances with given keyword.</li>
                                <li><router-link to="/timelinehashtag"  class="api-documentation">Most recent by hashtag</router-link> - Retrieve detailed metadata information for hashtags with the given keyword.</li>
                                <li><router-link to="/timelinestatus"  class="api-documentation">Recent for instance</router-link> - A chronological list of public statuses that users on the platform have shared. This timeline is visible to all users and provides a way to explore and discover content that is openly shared by others. </li>
                                <li><router-link to="/searchbyid"  class="api-documentation">Single status by Id</router-link> - Get information about a status by status Id</li>
                            </ul>
                        </div>
                        <div class="api-section">
                            <h4>2. Get Accounts</h4>
                            <ol class="api-list">
                                <li><router-link to="/searchaccounts" class="api-documentation">Search by keyword</router-link> - Search for accounts for the given keyword. Can search across multiple instances at once.</li>
                                <li><router-link to="/accountsbyId" class="api-documentation">Single account by Id</router-link> - Retrieve information about a profile using the account Id.</li>
                            </ol>
                        </div>
                        <div class="api-section">
                            <h4>3. Get Hashtag Metadata</h4>
                            <ol class="api-list">
                                <li><router-link to="/searchhashtags" class="api-documentation">Hashtag Metadata</router-link> - Search for accounts for the given keyword. Can search across multiple instances at once.</li>
                            </ol>
                        </div>
                        <div class="api-section">
                            <h4>4. Instances</h4>
                            <ol class="api-list">
                                <li><router-link to="/instances" class="api-documentation">Mastodon Instances</router-link> - Retrieves the top 20 Mastodon instances with a minimum of 5000 active users and lists them in descending order by active users. It utilizes the instances.social API to gather the instances.</li>
                            </ol>
                        </div>
                        <div class="api-section">
                            <h4>5. Documentation</h4>
                            <ol class="api-list">
                                <li><router-link to="/faq" class="api-documentation">FAQ</router-link> - Can search across multiple instances at once.</li>
                                <li><router-link to="/apidocumentation" class="api-documentation">API Documentation</router-link> -  Can search across multiple instances at once.</li>
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
</style>