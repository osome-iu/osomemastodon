<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="page-title">FAQ</h1>
            <ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> Mastodon Instances</ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> How to get the access token?</ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> Mastodon Search API</ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> Mastodon Timeline API</ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> What can use in mastodon search inputs?</ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> How the mastodon status Id made?</ul>
                <ul><span><i class="fa-solid fa-long-arrow-right"></i></span> Difference between the Local and Federated timelines</ul>
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
            <h4 class="mt-4">What can use in mastodon search inputs?</h4>
            <ul>
                <li>You can only use text in statuses and hashtag keywords—no symbols allowed. Spaces are permitted. </li>
                <li>Status IDs can consist of words and numbers, while Account IDs can only contain numbers</li>
            </ul>
            <h4 class="mt-4">How the mastodon status Id generated?</h4>
            <p>
                In Mastodon, each post is assigned a unique identifier using a modified version of Twitter's Snowflake algorithm. This algorithm incorporates three key components to generate a distinct ID for each post. Firstly, a timestamp is included to ensure chronological order. Secondly, a worker ID, representing the name of the server (instance) to which the user belongs, prevents collisions between IDs from different instances. Finally, a sequence number is employed to guarantee uniqueness within the same instance, incrementing with each new post. This combination of timestamp, worker ID, and sequence number allows Mastodon to create globally unique post IDs, facilitating efficient organization and retrieval of posts across its decentralized network.
            </p>
            <h4 class="mt-4">Difference between the Local and Federated timelines</h4>
            <p>
            The Local timeline shows posts from all users in your server, while the Federated timeline shows you all public posts from users that people in your server follow.
            </p>
        </div>
    </main>
</template>
<script setup>
</script>