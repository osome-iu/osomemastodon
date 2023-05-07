const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  devServer: {
    port: 4040,
    proxy: {
      '/api': {
        target: 'http://localhost:7000',
        pathRewrite: { '^/api': '' },
        changeOrigin: true,
      },
    },
  },
};
