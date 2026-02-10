const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.VUE_PUBLIC_PATH || (process.env.NODE_ENV === 'development' ? '/' : '/tools/mastodon'),
  outputDir: './dist',
  assetsDir: 'static'
})
