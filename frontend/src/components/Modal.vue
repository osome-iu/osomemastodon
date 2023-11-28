<template>
    <div v-if="isOpen" class="prompt-modal">
        <div class="prompt-modal-content">
            <div class="prompt-modal-header">
                <h5>{{ header }}</h5>
                <button class="prompt-modal-close" @click="$emit('cancel')">&times;</button>
            </div>

            <div class="prompt-modal-body">
                <div>
                    <div class="row">

                    </div>

                    <div class="row">
                        <div class="col-9">
                            <label for="form-control" style="font-size:15px">Official - Mastodon API <b>(GET)</b></label>
                            <input v-model="this.officialURL" ref="officialURL" class="form-control"/>
                        </div>
                        <div class="col-2">
                            <label for="form-control"></label>
                            <button type="button" class="btn btn-success btn-sm" :onclick="copyOfficialMastodonAPItoClipboard">Copy</button>
                        </div>
                    </div>
                    <div v-if="linkcopiedofficialAPI" class="validation-message" >
                        Copied to clipboard!
                    </div>
                    <div class="row">
                        <div class="col-9">
                            <label for="form-control">OSoME - Mastodon API <b>(POST)</b></label>
                            <input v-model="this.osomeURL" ref="osomeURL" class="form-control"/>
                        </div>
                        <div class="col-2">
                            <label for="form-control"></label>
                            <button type="button" class="btn btn-success btn-sm" :onclick="copyOSoMeMastodonAPItoClipboard">Copy</button>
                        </div>
                    </div>
                    <div v-if="linkcopiedOsoMEAPI" class="validation-message">
                        Copied to clipboard!
                    </div>
                </div>
                <div class="row" style="text-align: center; margin-left:10px; margin-right: 10px; margin-top:20px;">
                    <div class="col" >
                        <button  class="btn btn-secondary btn-md" @click="$emit('cancel')">Cancel</button>
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
        officialURL: {
            type: String,
            default: 'Official API URL',
        },
        osomeURL: {
            type: String,
            default: "OSoME API URL"
        },
        osomeURLrequestType:{
            type: String,
            default: "POST"
        },
        header:{
            type: String,
            default: 'Search API',
        }
    },
    data() {
        return {
            linkcopiedofficialAPI: false,
            linkcopiedOsoMEAPI: false,
            inputValue: '',
        };
    },
    methods: {
        copyOfficialMastodonAPItoClipboard() {
            // Select the input field content
            this.$refs.officialURL.select();
            this.$refs.officialURL.setSelectionRange(0, 99999);

            // Execute the copy command
            document.execCommand('copy');

            // Clear the selection
            window.getSelection().removeAllRanges();

            // Show validation message
            this.linkcopiedofficialAPI = true;

            // Hide validation message after a delay (e.g., 2 seconds)
            setTimeout(() => {
                this.linkcopiedofficialAPI = false;
            }, 500);
        },
        copyOSoMeMastodonAPItoClipboard(){
            // Select the input field content
            this.$refs.osomeURL.select();
            this.$refs.osomeURL.setSelectionRange(0, 99999);

            // Execute the copy command
            document.execCommand('copy');

            // Clear the selection
            window.getSelection().removeAllRanges();

            // Show validation message
            this.linkcopiedOsoMEAPI = true;

            // Hide validation message after a delay (e.g., 2 seconds)
            setTimeout(() => {
                this.linkcopiedOsoMEAPI = false;
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