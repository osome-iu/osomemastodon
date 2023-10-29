<template>
    <div v-if="isOpen" class="prompt-modal">
        <div class="prompt-modal-content">
            <div class="prompt-modal-header">
                <h5>Account Search</h5>
                <button class="prompt-modal-close" @click="$emit('cancel')">&times;</button>
            </div>

            <div class="prompt-modal-body">
                <div style="text-align: left">
                    <div class="row">
                        <label for="keyword"><b>GET</b> Request</label>
                    </div>

                    <div class="row">
                        <label for="keyword"><b>Documentation</b> <a href="https://docs.joinmastodon.org/methods/search/" target="_blank">Mastodon Search</a></label>
                    </div>

                    <div class="row" style="margin-left:1px; margin-right: 1px">
                        <input
                            v-model="this.showURL" ref="showURLvalue"
                        />
                    </div>
                </div>

                <div v-if="linkcopied" class="validation-message" style="text-align: center;">
                    Copied to clipboard!
                </div>

                <div class="row" style="text-align: center; margin-left:10px; margin-right: 10px">
                    <div class="col">
                        <button type="button" class="btn btn-success btn-sm" :onclick="copyToClipboard">Copy</button>
                    </div>
                    <div class="col">
                        <button  class="btn btn-secondary btn-sm" @click="$emit('cancel')">Cancel</button>
                    </div>
                </div>
            </div>

            <div class="prompt-modal-footer"></div>
        </div>
    </div>
</template>
<script>

export default {
    props: {
        isOpen: {
            type: Boolean,
            required: true,
        },
    },
    data() {
        return {
            linkcopied: false,
            inputValue: '',
            showURL: "https://mastodon.social/api/v2/search?q=helloworld&type=Accounts"
        };
    },
    methods: {
        copyToClipboard() {
            // Select the input field content
            this.$refs.showURLvalue.select();
            this.$refs.showURLvalue.setSelectionRange(0, 99999);

            // Execute the copy command
            document.execCommand('copy');

            // Clear the selection
            window.getSelection().removeAllRanges();

            // Show validation message
            this.linkcopied = true;

            // Hide validation message after a delay (e.g., 2 seconds)
            setTimeout(() => {
                this.linkcopied = false;
            }, 500);
        }
    },
};
</script>

<style scoped>
.prompt-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
}
.prompt-modal-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.1);
}
.prompt-modal-content {
    position: relative;
    width: 400px;
    max-width: 90%;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
}
.prompt-modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 20px;
    padding-left: 20px;
    background-color: #f2f2f2;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}
.prompt-modal-header h2 {
    margin: 0;
}
.prompt-modal-close {
    border: none;
    outline: none;
    font-size: 24px;
    cursor: pointer;
    color: #666;
}
.prompt-modal-body {
    padding: 20px;
}
.prompt-modal-body p {
    margin-top: 0;
}
.prompt-modal-footer {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
}
@media screen and (max-width: 480px) {
    .prompt-modal-content {
        width: 90%;
    }
}

.prompt-modal-body .card-body {
    background-color: black;
    border-radius: 4px; /* Adjust the radius as needed */
    padding: 15px; /* Adjust the padding as needed */
}

.row{
    padding-top: 10px;
}

.validation-message {
    margin-top: 10px;
    color: green;
}
</style>