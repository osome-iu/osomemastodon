<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="mt-4">FAQ</h1>
            <ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> Mastodon Instances</ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> How to get the access token?</ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> Mastodon Search API</ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> Mastodon Timeline API</ul>
            </ul>
            <h4 class="mt-4">Mastodon Instances</h4>
            <p>
                Mastodon instances are independent, self-hosted communities within the Mastodon social network. Each instance operates as a separate server, allowing users to join and interact with others on that specific instance. Instances share a common set of protocols, enabling users from different instances to communicate and follow each other. These instances can have their own rules, themes, and user communities, providing diverse and customizable spaces for social interaction within the broader Mastodon network.
            </p>
            <h4 class="mt-4">How to get the access token?</h4>
            <p>
                To obtain an access token for a Mastodon instance, you typically need to follow a few steps. Mastodon uses OAuth 2.0 for authentication, which involves registering your application with the Mastodon instance and then obtaining an access token for user authentication. Here's a brief overview:
            </p>
            <p>
                <b>Register Your Application:</b> <br/>
            </p>
            <ul>
                <li>Go to the Mastodon instance where you want to access the API.</li>
                <li>Log in to your Mastodon account.</li>
                <li>Navigate to your account settings or developer settings to create a new application.</li>
                <li>Create a new application, providing details like the name, website, and redirect URI. The redirect URI is where the user will be redirected after they grant access.</li>
            </ul>
            <p>
                <b>Get Client ID and Client Secret:</b> <br/>
            </p>
            <ul>
                <li>Once you've registered the application, you will be provided with a Client ID and a Client Secret. Keep these credentials secure.</li>
            </ul>
            <h4 class="mt-4">Mastodon Search API</h4>
            <p>
                Search for content in accounts, statuses and hashtags.
            </p>
            <h4 class="mt-4">Mastodon Timeline API</h4>
            <p>

            </p>
        </div>
    </main>
</template>
<script setup>
</script>