<template>
    <div>
        <footer class="py-4 bg-light full-width-footer">
            <div id="footer" role="contentinfo" itemscope="itemscope" itemtype="http://schema.org/CollegeOrUniversity">
                <div class="iu-row pad">
                    <p class="signature">
                        <a href="https://www.iu.edu/index.html" class="signature-link signature-img"><img src="//assets.iu.edu/brand/3.3.x/iu-sig-formal.svg" alt="Indiana University"></a>
                    </p>

                    <p class="copyright">
                    <span class="line-break">
                        <a href="https://accessibility.iu.edu/assistance/index.html" id="accessibility-link" title="Having trouble accessing this web page content? Please visit this page for assistance.">Accessibility</a> |
                        <router-link id="privacy-policy-link" :to="{ path: '/privacy' }">Privacy Notice</router-link>
                    </span>
                        <span class="hide-on-mobile"> | </span>
                        <a href="https://www.iu.edu/copyright/index.html">Copyright</a> © {{ currentYear }} <span class="line-break-small">The Trustees of <a href="https://www.iu.edu/index.html" itemprop="url">
                            <span itemprop="name">Indiana University</span></a>
                    </span>
                    </p>
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

<style scoped>
</style>
