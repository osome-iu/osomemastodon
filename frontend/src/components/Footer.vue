<template>
    <div class="container text-center">
        <footer class="py-4 bg-light mt-auto">
            <div class="container-fluid px-4">
                <div class="d-flex align-items-center justify-content-between small">
                    <div class="text-muted"><a href="https://www.iu.edu/copyright/index.html" target="_blank">Copyright </a> &copy; {{ getcurrentYear }} the
                        Trustees of <a href="http://indiana.edu/" target="_blank">Indiana University</a></div>
                    <div>
                        <a href="https://cnets.indiana.edu/" target="_blank">CNetS</a>&nbsp;&nbsp;&nbsp;&nbsp;
                        <a href="https://luddy.indiana.edu/" target="_blank">Luddy</a>
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