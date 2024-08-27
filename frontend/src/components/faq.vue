<template>
    <main>
        <div class="container-fluid px-4">
            <h2 class="page-title">FAQ</h2>
            <ul class= "list-item-main">
                <li class= "list-item" v-scroll-to="'#q-1'" @click="highlightSection('q-1')"><span><i class="fa-solid fa-long-arrow-right" ></i></span> Mastodon instances</li>
                <li class= "list-item" v-scroll-to="'#q-2'" @click="highlightSection('q-2')"><span><i class="fa-solid fa-long-arrow-right"></i></span> How to get the access token</li>
                <li class= "list-item" v-scroll-to="'#q-3'" @click="highlightSection('q-3')"><span><i class="fa-solid fa-long-arrow-right"></i></span> How are the Mastodon status ids made?</li>
                <li class= "list-item" v-scroll-to="'#q-4'" @click="highlightSection('q-4')"><span><i class="fa-solid fa-long-arrow-right"></i></span> How is OSoMe Mastodon Search supported?</li>
                <li class= "list-item" v-scroll-to="'#q-5'" @click="highlightSection('q-5')"><span><i class="fa-solid fa-long-arrow-right"></i></span> Report an issue</li>
            </ul>
            <div id="q-1" class="content-section">
                <h3 class="mt-4">Mastodon Instances</h3>
                <div :class="{ 'highlighted': highlightedSection === 'q-1' }">
                    <p>
                        Mastodon instances are independent, self-hosted communities within the Mastodon social network. Each instance operates as a separate server, allowing users to join and interact with others on that specific instance. Instances share a common set of protocols, enabling users from different instances to communicate and follow each other. These instances can have their own rules, themes, and user communities, providing diverse and customizable spaces for social interaction within the broader Mastodon network.
                    </p>
                </div>
            </div>
            <div id="q-2">
                <h3 class="mt-4">How to get the access token</h3>
                <div :class="{ 'highlighted': highlightedSection === 'q-2' }">
                    <p>
                        To obtain an access token for a Mastodon instance, you typically need to follow a few steps. Mastodon uses OAuth 2.0 for authentication, which involves registering your application with the Mastodon instance and then obtaining an access token for user authentication.
                        The exact location for acquiring an API token may be different depending on the software version installed on an instance. As an example, on the desktop version of <a href="https://mastodon.social/" target="_blank" class="black-link">mastodon.social:</a>
                    </p>
                    <ol>
                        <li>Log in to your account.</li>
                        <li>Click "Preferences" from either the bottom of the right column or from the hamburger menu next to your profile picture.</li>
                        <li>Choose &lt;/&gt; Development &lt;/&gt; from the menu.</li>
                    </ol>
                    <p>Or, just go to mastodon application <a href="https://mastodon.social/settings/applications" target="_blank" class="black-link">settings</a>.</p>
                    <p>Name your application something like "OSoMe Search Tool". Use "https://osome.iu.edu/tools/mastodon/" for the Application Website. Add "https://osome.iu.edu/tools/mastodon/" to the Redirect URI list. You should only need "Read" permissions, so make sure that "read" is selected under Scopes. You will need to do this for each Mastodon instance you'd like to search.</p>
                </div>
            </div>
            <div id="q-3">
                <h3 class="mt-4">How are the Mastodon status ids made?</h3>
                <div :class="{ 'highlighted': highlightedSection === 'q-3' }">
                    <p>
                        In Mastodon, each post is assigned a unique identifier using a modified version of Twitter's Snowflake algorithm. This algorithm incorporates three key components to generate a distinct id for each post. Firstly, a timestamp is included to ensure chronological order. Secondly, a worker id that represents the name of the server(instance) to which the posting user belongs, prevents collisions between ids from different instances. Finally, a sequence number is employed to guarantee uniqueness within the same instance, incrementing with each new post. This combination of timestamp, worker id, and sequence number allows Mastodon to create globally unique post ids, facilitating efficient organization and retrieval of posts across its decentralized network.
                    </p>
                </div>
            </div>
            <div id="q-4">
                <h3 class="mt-4">How is OSoMe Mastodon Search supported?</h3>
                <div :class="{ 'highlighted': highlightedSection === 'q-4' }">
                    <p>
                        The development of this tool was funded through the generous support of the 
                        <a href="https://knightfoundation.org/" target="_blank" class="black-link">Knight Foundation</a>,
                        the <a href="https://www.opentech.fund/" target="_blank" class="black-link">Open Technology Fund</a>, and
                        <a href="https://craignewmarkphilanthropies.org/" target="_blank" class="black-link">Craig Newmark Philanthropies</a>.
                    </p>
                </div>
            </div>
            <div id="q-5">
                <h3 class="mt-4">Report an issue</h3>
                <div :class="{ 'highlighted': highlightedSection === 'q-5' }">
                    <p>
                        Please feel free to submit any issues, bug reports, or feature requests that you might have by adding new issues to the <a href="https://github.com/osome-iu/osomemastodon/issues" target="_blank" class="black-link">Github repository</a>.
                    </p>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import VueScrollTo from 'vue-scrollto';
export default {
    name: "FAQ",
    data() {
        return {
            highlightedSection: null
        }
    },
    methods: {
        highlightSection(sectionId) {
            this.highlightedSection = null
            this.highlightedSection = sectionId;
        }
    },
    mounted() {
        const id = this.$route.hash.slice(1);
        if (id) {
            if (id) {
                this.highlightSection(id)
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

.highlighted {
    background-color: #A8F1F9; /* Highlight color */
    padding: 2px; /* Padding for highlighted text */
}

</style>