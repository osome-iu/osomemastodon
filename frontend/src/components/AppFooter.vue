<template>
    <div class="container text-center">
        <hr class="justify-content-center row">
        <div class="justify-content-center row">
            <div class="col-6">
                <div style="text-align: center">
                    <a href="https://osome.iu.edu/" target="_blank">

                    </a>
                </div>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="column">
                <a href="https://iuni.iu.edu/" target="_blank">IUNI</a>
            </div>
            <div class="column">
                <a href="https://cnets.indiana.edu/" target="_blank">CNetS</a>
            </div>
            <div class="column">
                <a href="https://luddy.indiana.edu/" target="_blank">Luddy</a>
            </div>
        </div>
        <p style="text-align: center; padding-top: 15px">
            <a href="https://www.iu.edu/copyright/index.html" target="_blank">Copyright </a> &copy; {{ getcurrentYear }} the
            Trustees of <a href="http://indiana.edu/" target="_blank">Indiana
            University</a>
        </p>
    </div>
</template>

<script>
export default {
    name: 'AppFooter',
    data() {
        return {
            currentYear: null,
        }
    },
    computed: {
        getcurrentYear() {
            return new Date().getFullYear()
        }
    }
}
</script>

<style scoped>
hr {
    align-content: center;
}
.column {
    width: 10%;
}
@media (max-width: 992px) {
    .column {
        width: 55%;
    }
    img {
        width: 50%;
    }
}
@media (max-width: 1700px) {
    .column {
        width: 20%;
    }
    img {
        width: 50%;
    }
}
@media (max-width: 768px) {
    .column {
        width: 20%;
    }
    img {
        width: 50%;
    }
}
@media (max-width: 480px) {
    .column {
        width: 20%;
    }
    img {
        width: 50%;
    }
}
img {
    width: 50%;
    height: 20%;
}
</style>