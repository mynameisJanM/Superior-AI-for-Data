import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  root: '.',
  publicDir: 'public',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: 'index.html'
    }
  },
  server: {
    open: true,
    configureServer({ app }) {
      app.use((req, res, next) => {
        if (req.url === '/favicon.ico') {
          res.statusCode = 204; // No content
          res.end();
          return;
        }
        next();
      });
    }
  }
})