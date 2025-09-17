import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

// ...existing code...
export default defineConfig({
  plugins: [react()],
  base: '/',
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      // changed: use the HTML entry so Vite/Rollup can resolve index.html
      input: resolve(__dirname, 'index.html')
    }
  },
  server: {
    open: true
  }
})
// ...existing code...