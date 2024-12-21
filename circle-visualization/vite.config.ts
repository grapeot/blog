import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    port: 3000,
    host: '0.0.0.0',
    strictPort: true
  },
  build: {
    target: 'esnext',
    outDir: 'dist'
  }
});
