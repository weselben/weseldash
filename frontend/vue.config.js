const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  
  // PWA Configuration
  pwa: {
    name: 'Personal Dashboard',
    short_name: 'Dashboard',
    description: 'Personal self-hosted hub for managing digital life',
    theme_color: '#4DBA87',
    background_color: '#000000',
    display: 'standalone',
    scope: '/',
    start_url: '/',
    icons: [
      {
        src: 'img/icons/icon-192x192.png',
        sizes: '192x192',
        type: 'image/png'
      },
      {
        src: 'img/icons/icon-512x512.png',
        sizes: '512x512',
        type: 'image/png'
      }
    ],
    manifestOptions: {
      categories: ['productivity', 'utilities'],
      lang: 'en-US'
    },
    workboxOptions: {
      runtimeCaching: [
        {
          urlPattern: /^https:\/\/api\./,
          handler: 'NetworkFirst',
          options: {
            cacheName: 'api-cache',
            networkTimeoutSeconds: 3,
            cacheableResponse: {
              statuses: [0, 200]
            }
          }
        }
      ]
    }
  },

  // Development server configuration
  devServer: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false
      },
      '/health': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false
      }
    }
  },

  // Build configuration
  configureWebpack: {
    optimization: {
      splitChunks: {
        chunks: 'all'
      }
    }
  }
})