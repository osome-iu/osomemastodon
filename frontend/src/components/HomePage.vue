<template>
    <main class="row custom-margin">
        <div class="custom-container">
            <div class="text-container">
                <h1 class="page-title"><b>OSoMe Mastodon Search</b></h1>
                <div class="paragraph-text">
                    <p>OSoMe Mastodon Search provides an interface to Mastodon data: retrieve statuses, explore accounts, access hashtag metadata, discover instances, and access comprehensive documentation. This allows researchers to explore and analyze data for valuable insights. As Mastodon is a federated social network, the OSoMe Mastodon Search interface lets you search for keywords and hashtags <b data-v-595e0590="">across multiple Mastodon instances</b>.</p>
                </div>
            </div>
            <div class="image-container">
                <img src="../assets/homepage-icon.png" alt="Mastodon Image" class="custom-image">
            </div>
        </div>
    </main>
</template>

<style scoped>
.page-title {
    font-size: 2.5rem;
}

.paragraph-text {
    font-size: 1.8rem;
    text-align: justify; /* Ensure the text is justified */
}

/* Custom margin class */
.custom-margin {
    margin: 0 auto;
    padding: 30px;
}

.custom-container {
    display: flex;
    align-items: flex-start;
    gap: 20px; /* Space between text and image */
    flex-wrap: nowrap; /* Prevent wrapping */
}

.custom-image {
    margin-top: -60px;
    max-width: 60vw;
    max-height: 700px;
    flex-shrink: 0; /* Prevent the image from shrinking */
}

.text-container {
    max-width: 70vw; /* Ensures the maximum width is the full viewport width */
    margin: 0 auto; /* Optional: centers the container horizontally */
    padding: 0 20px; /* Optional: adds some padding for better readability */
    min-width: 30vw;
}


.image-container {
    margin-left: 40px;
}

/* Media query for smaller screens */
@media (max-width: 1024px) {
    .custom-margin {
        margin-left: 2px;
        margin-top: 15px;
        margin-right: 2px;
    }

    .page-title {
        font-size: 2rem;
    }

    .paragraph-text {
        font-size: 1.6rem;
    }

    .custom-container {
        flex-direction: column; /* Stack items vertically */
        align-items: center; /* Center items */
    }

    .custom-image {
        margin-top: 20px; /* Add space between text and image */
        max-width: 50vw;
        max-height: 600px;
        flex-shrink: 0; /* Prevent the image from shrinking */
    }
}

@media (max-width: 768px) {
    .custom-margin {
        margin-left: 2px;
        margin-top: 20px;
        margin-right: 2px;
    }

    .text-container {
        max-width: 100%; /* Full width on small screens */
    }

    .page-title {
        font-size: 5vw; /* Use viewport width for responsiveness */
    }

    .paragraph-text {
        font-size: 4vw; /* Adjust font size for better readability on small screens */
    }

    .custom-image {
        max-width: 50vw;
        max-height: 600px;
        flex-shrink: 0; /* Prevent the image from shrinking */
    }
}

@media (max-width: 480px) {
    .custom-margin {
        margin-left: 2px;
        margin-top: 10px;
        margin-right: 2px;
    }

    .page-title {
        font-size: 5.5vw; /* Use viewport width for responsiveness */
    }

    .paragraph-text {
        font-size: 4.5vw; /* Adjust font size for better readability on very small screens */
    }

    .image-container {
        margin-top: 2px;
        margin-left: 20px;
        margin-right: 20px;
    }

    .custom-image {
        max-width: 50vw;
        max-height: 600px;
        flex-shrink: 0; /* Prevent the image from shrinking */
    }
}
</style>
