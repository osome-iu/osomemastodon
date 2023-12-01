<template>
    <main>
        <div class="container-fluid px-4">
            <h1 class="page-title">FAQ</h1>
            <ul>
                <li  class= "list-item" v-scroll-to="'#q-1'"><span><i class="fa-solid fa-long-arrow-right" ></i></span> Mastodon Instances</li>
                <li  class= "list-item" v-scroll-to="'#q-2'"><span><i class="fa-solid fa-long-arrow-right"></i></span> How to get the access token?</li>
                <li  class= "list-item" v-scroll-to="'#q-3'"><span><i class="fa-solid fa-long-arrow-right"></i></span> Why is there an option to check the Mastodon instance for each status?</li>
                <li  class= "list-item" v-scroll-to="'#q-4'"><span><i class="fa-solid fa-long-arrow-right" ></i></span> What can use in mastodon search inputs?</li>
                <li  class= "list-item" v-scroll-to="'#q-5'"><span><i class="fa-solid fa-long-arrow-right"></i></span> How the mastodon status Id made?</li>
                <li  class= "list-item" v-scroll-to="'#q-6'"><span><i class="fa-solid fa-long-arrow-right"></i></span> Difference between the Local and Federated timelines</li>
            </ul>
            <div id="q-1">
                <h4 class="mt-4">Mastodon Instances</h4>
                <p>
                    Mastodon instances are independent, self-hosted communities within the Mastodon social network. Each instance operates as a separate server, allowing users to join and interact with others on that specific instance. Instances share a common set of protocols, enabling users from different instances to communicate and follow each other. These instances can have their own rules, themes, and user communities, providing diverse and customizable spaces for social interaction within the broader Mastodon network.
                </p>
            </div>
            <div id="q-2">
                <h4 class="mt-4">How to get the access token?</h4>
                <p>
                    To obtain an access token for a Mastodon instance, you typically need to follow a few steps. Mastodon uses OAuth 2.0 for authentication, which involves registering your application with the Mastodon instance and then obtaining an access token for user authentication. Here's a brief overview:
                </p>

                <p>
                    <b>Register Your Application:</b> <br/>
                </p>
                <ol>
                    <li>Go to the Mastodon instance where you want to access the API.</li>
                    <li>Log in to your Mastodon account.</li>
                    <li>Navigate to your account settings or developer settings to create a new application.</li>
                    <li>Create a new application, providing details like the name, website, and redirect URI. The redirect URI is where the user will be redirected after they grant access.</li>
                </ol>
                <p>
                    <b>Get Client ID and Client Secret:</b> <br/>
                </p>
                <ul>
                    <li>Once you've registered the application, you will be provided with a Client ID and a Client Secret. Keep these credentials secure.</li>
                </ul>
            </div>
            <div id="q-3">
                <h4 class="mt-4">Why is there an option to check the Mastodon instance for each status?</h4>
                <p>
                    There are some misconfigured Mastodon instances there.
                </p>
            </div>
            <div id="q-4">
                <h4 class="mt-4">What can use in mastodon search inputs?</h4>
                <ul>
                    <li>You can only use text in statuses and hashtag keywords—no symbols allowed. Spaces are permitted. </li>
                    <li>Status IDs can consist of words and numbers, while Account IDs can only contain numbers</li>
                </ul>
            </div>
            <div id="q-5">
                <h4 class="mt-4">How the mastodon status Id generated?</h4>
                <p>
                    In Mastodon, each post is assigned a unique identifier using a modified version of Twitter's Snowflake algorithm. This algorithm incorporates three key components to generate a distinct ID for each post. Firstly, a timestamp is included to ensure chronological order. Secondly, a worker ID, representing the name of the server (instance) to which the user belongs, prevents collisions between IDs from different instances. Finally, a sequence number is employed to guarantee uniqueness within the same instance, incrementing with each new post. This combination of timestamp, worker ID, and sequence number allows Mastodon to create globally unique post IDs, facilitating efficient organization and retrieval of posts across its decentralized network.
                </p>
            </div>
            <div id="q-6">
                <h4 class="mt-4">Difference between the Local and Federated timelines</h4>
                <p>
                The Local timeline shows posts from all users in your server, while the Federated timeline shows you all public posts from users that people in your server follow.
                </p>
            </div>
        </div>
    </main>
</template>
<script setup>
</script>

<style scoped>
ul {
    list-style-type: none; /* Removes the default list-style dot */
}

.list-item{
    cursor: pointer;
}

.list-item:hover {
    color: blue;
    text-decoration: underline;
}
</style>