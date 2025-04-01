module.exports = {
  devServer: {
    port: 8080,  // Frontend roda em 8080
    proxy: {
      '/api': {
        target: 'http://localhost:5000',  // Backend roda em 5000
        changeOrigin: true
      }
    }
  }
};