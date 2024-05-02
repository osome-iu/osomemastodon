<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="page-title"><b>OSoMe Mastodon Search</b></h1>
            <div class="col-12">
                <div class="paragraph-text">
                    <p>OSoMe Mastodon Search provides an interface to Mastodon data: retrieve statuses, explore accounts, access hashtag metadata, discover instances, and access comprehensive documentation. This allows researchers to explore and analyze data for valuable insights. As Mastodon is a federated social network, the OSoMe Mastodon Search interface lets you search for for keywords and hashtags <b>across multiple Mastodon instances</b>.</p>
                </div>
            </div>
        </div>
        <div class="col-12 d-flex justify-content-center align-items-center" style="margin-top: 5px;">
            <img src="../assets/homepage.jpg" alt="Mastodon Image" style="max-width: 100%; max-height: 700px;" />
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
    font-size: 1.5rem;
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
.paragraph-text{
    font-size: 1.5rem;
}
.api-documentation{
    text-decoration : underline;
}
</style>
<script setup>
</script>
