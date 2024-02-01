<template>
    <div v-if="isOpen" class="prompt-modal">
        <div class="prompt-modal-content">
            <div class="prompt-modal-header">
                <h5>{{ header }}</h5>
                <button class="prompt-modal-close" @click="$emit('cancel')">&times;</button>
            </div>

            <div class="prompt-modal-body">
                <div class="row" v-if="!isModalError">
                    <p>{{info}}</p>
                </div>
                <div class="row" v-if="isModalError">
                    <div v-html="info"></div>
                </div>
                <div class="row" style="text-align: center; margin-left:10px; margin-right: 10px; margin-top:5px;">
                    <div class="col" >
                        <button  class="btn btn-success btn-md" @click="$emit('cancel')">Okay</button>
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
        info: {
            type: Boolean,
            required: true,
        },
        infoModalIsOpen: {
            type: Boolean,
            required: true,
        },
        header:{
            type: String,
            default: 'Info',
        },
        isModalError:{
            type: String,
            default: Boolean
        }
    },
    data() {
        return {
        };
    },
    methods: {
    },
};
</script>

<style>
.prompt-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 95%;
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
    width: 600px;
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
    text-align: center; /* Add this line to center-align text */
    justify-content: center;
    align-items: center;
}
.prompt-modal-body p {
    margin-top: 0;
}
.prompt-modal-footer {
    padding: 2px;
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
</style>