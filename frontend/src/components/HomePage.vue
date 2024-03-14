<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="page-title"><b>OSoMe Mastodon Search</b></h1>
            <div class="col-12">
                <div>
                    <p>OSoMe Mastodon provides an interface to various functionalities, allowing users to retrieve statuses, explore accounts, access hashtag metadata, discover instances, and access comprehensive documentation. This empowers researchers to experiment with Mastodon data, enabling in-depth exploration and analysis for valuable insights.</p>
                </div>
            </div>
            <div class="col-12">
                <div>
                    <p>As Mastodon is a federated social network, the 'OSoMe Mastodon Search' interface allows users to search for keywords/hashtags <b>across multiple Mastodon instances</b>.</p>
                </div>
            </div>
                <div class="row">
                    <div class="col-xl-12">
                        <div class="search-section">
                            <h4>Statuses</h4>
                            <div class="sub-text">
                                <p> For statuses, you can retrieve statuses using a keyword, find recent statuses by a hashtag, view recent statuses from a specific instance, and obtain information about a status using status id.</p>
                            </div>
                        </div>
                        <div class="search-section">
                            <h4>Accounts</h4>
                            <div class="sub-text">
                                <p> For accounts, you can search for accounts using a keyword, and retrieve detailed information about a specific profile using account id.</p>
                            </div>
                        </div>
                        <div class="search-section">
                            <h4> Hashtag Metadata</h4>
                            <div class="sub-text">
                                <p> For hashtag metadata, you can retrieve a list of hashtags containing a specific search term.</p>
                            </div>
                        </div>
                        <div class="search-section">
                            <h4>Instances</h4>
                            <div class="sub-text">
                                <p> Users can see the top 20 Mastodon instances with a minimum of 5000 active users and lists them in descending order by active users. It utilizes the <a href="https://instances.social/api/doc/" target="_blank"  aria-label="instances.social" style="color: #2c3e50;"> instances.social </a> API to gather the instances.</p>
                            </div>
                        </div>
                        <div class="search-section">
                            <h4> Documentation</h4>
                            <div class="sub-text">
                                <p>  The FAQ section offers quick insights and answers to common questions about the OSoMe Mastodon Search interface, while the API Documentation provides a comprehensive guide for interacting with its APIs, covering endpoints, request formats and response structures.</p>
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
.search-section{
    margin-left: 20px;
    margin-top:8px;
    margin-bottom:20px;
}
.sub-text{
    margin-left: 20px;
}
</style>
<script setup>
</script>