<template>
    <div class="container text-center">
        <footer class="py-4 bg-light mt-auto">
            <div class="container-fluid px-4">
                <div class="d-flex align-items-center justify-content-between small">
                    <div class="text-muted"><a href="https://www.iu.edu/copyright/index.html" target="_blank" class="navigation-link">Copyright </a> &copy; {{ getcurrentYear }} the
                        Trustees of <a href="http://indiana.edu/" target="_blank" class="navigation-link">Indiana University</a></div>
                    <div>
                        <a href="https://osome.iu.edu/" target="_blank" class="navigation-link">OSoMe</a>&nbsp;&nbsp;&nbsp;&middot;&nbsp;
                        <a href="https://cnets.indiana.edu/" target="_blank" class="navigation-link">CNetS</a>&nbsp;&nbsp;&nbsp;&middot;&nbsp;
                        <a href="https://luddy.indiana.edu/" target="_blank" class="navigation-link">Luddy</a>
                    </div>
                </div>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
    name: 'Footer',
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

<style>

.navigation-link {
    text-decoration: underline;
    color: #2c3e50; /* Adjust the color as needed */
    transition: text-decoration 0.3s;
}
.navigation-link:hover {
    text-decoration: none;
}
</style>