<template>
    <main>
        <div class="container-fluid px-4">
            <h2 class="page-title">FAQ</h2>
            <ul class= "list-item-main">
                <li class= "list-item" v-scroll-to="'#q-1'"><span><i class="fa-solid fa-long-arrow-right" ></i></span> Mastodon instances</li>
                <li class= "list-item" v-scroll-to="'#q-2'"><span><i class="fa-solid fa-long-arrow-right"></i></span> How to get the access token</li>
                <li class= "list-item" v-scroll-to="'#q-3'"><span><i class="fa-solid fa-long-arrow-right"></i></span> What does "Check instance validity" mean</li>
                <li class= "list-item" v-scroll-to="'#q-4'"><span><i class="fa-solid fa-long-arrow-right" ></i></span> What can be used in Mastodon search inputs</li>
                <li class= "list-item" v-scroll-to="'#q-6'"><span><i class="fa-solid fa-long-arrow-right"></i></span> Difference between the Local and Federated timelines</li>
                <li class= "list-item" v-scroll-to="'#q-7'"><span><i class="fa-solid fa-long-arrow-right"></i></span> Report an issue</li>
            </ul>
            <div id="q-1">
                <h3 class="mt-4">Mastodon Instances</h3>
                <p>
                    Mastodon instances are independent, self-hosted communities within the Mastodon social network. Each instance operates as a separate server, allowing users to join and interact with others on that specific instance. Instances share a common set of protocols, enabling users from different instances to communicate and follow each other. These instances can have their own rules, themes, and user communities, providing diverse and customizable spaces for social interaction within the broader Mastodon network.
                </p>
            </div>
            <div id="q-2">
                <h3 class="mt-4">How to get the access token</h3>
                <p>
                    To obtain an access token for a Mastodon instance, you typically need to follow a few steps. Mastodon uses OAuth 2.0 for authentication, which involves registering your application with the Mastodon instance and then obtaining an access token for user authentication.
                    The exact location for acquiring an API token may be different depending on the software version installed on an instance. As an example, on the desktop version of <a href="https://mastodon.social/" target="_blank" class="black-link">mastodon.social</a>.
                </p>
                <ol>
                    <li>Log in to your account:</li>
                    <li>Click "Preferences" from either the bottom of the right column or from the hamburger menu next to your profile picture:</li>
                    <li>Choose &lt;/&gt; Development &lt;/&gt; from the menu.</li>
                </ol>
                <p>Or, just go to mastodon application <a href="https://mastodon.social/settings/applications" target="_blank" class="black-link">settings</a>.</p>
                <p>Name your application something like "OSoMe Search Tool". Use "https://osome.iu.edu/tools/mastodon/" for the Application Website. Add "https://osome.iu.edu/tools/mastodon/" to the Redirect URI list. You should only need "Read" permissions, so make sure that "read" is selected under Scopes.</p>
            </div>
            <div id="q-5">
                <h3 class="mt-4">How are the Mastodon Status IDs made</h3>
                <p>
                    In Mastodon, each post is assigned a unique identifier using a modified version of Twitter's Snowflake algorithm. This algorithm incorporates three key components to generate a distinct Id for each post. Firstly, a timestamp is included to ensure chronological order. Secondly, a worker Id, that represents the name of the server (instance) to which the posting user belongs, prevents collisions between Ids from different instances. Finally, a sequence number is employed to guarantee uniqueness within the same instance, incrementing with each new post. This combination of timestamp, worker Id, and sequence number allows Mastodon to create globally unique post Ids, facilitating efficient organization and retrieval of posts across its decentralized network.
                </p>
            </div>
            <div id="q-6">
                <h4 class="mt-4">Difference between the Local and Federated timelines</h4>
                <p>
                    The Local timeline displays posts from all users on a specified server, while the Federated timeline includes public posts from users across the Mastodon network who are followed by users on the specified server.
                </p>
            </div>
            <div id="q-7">
                <h3 class="mt-4">Report an issue</h3>
                <p>
                    Please feel free to submit any issues, bug reports, or feature requests that you might have by adding new issues to the <a href="https://github.com/osome-iu/osomemastodon/issues" target="_blank" class="black-link">Github repository</a>.
                </p>
            </div>
        </div>
    </main>
</template>

<script>
import VueScrollTo from 'vue-scrollto';
export default {
    name: "FAQ",
    mounted() {
        const id = this.$route.hash.slice(1);
        if (id) {
            if (id) {
                VueScrollTo.scrollTo('#' + id, 500, { offset: -65 });
            }
        }
    }
}
</script>

<style scoped>

.list-item-main {
    list-style-type: none; /* Removes the default list-style dot */
}

.list-item{
    cursor: pointer;
}

.list-item:hover {
    color: blue;
    text-decoration: underline;
}

.black-link{
    text-decoration: underline;
}
</style>