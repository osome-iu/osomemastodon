<template>
    <div class="logo-div">
        <span class="logo-title-name">{{ name }}</span>
    </div>
</template>

<script>
export default {
    name: "AppLogo",
    props: {
        nightMode: {
            type: Boolean,
        },
    },
    data() {
        return {
            name: "Mastodon",
            dot: ".",
        };
    },
};
</script>

<style scoped>
.logo-div:hover .logo-title-name {
    letter-spacing: 0px;
    transition: 0.5s all;
}

.logo-title-name {
    font-size: 35px;
    font-weight: 500;
    letter-spacing: 2px;
    transition: 0.5s all;
}
span{
    color: white;
}
</style>