import path from "node:path";
import { fileURLToPath } from "node:url";
import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default defineConfig({
  root: path.resolve(__dirname, "./frontend"),
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./frontend/src"),
    },
  },
  server: {
    host: "0.0.0.0",
    port: 5173,
    strictPort: true,
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/sala": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/tipo-sala": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/especialidade": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/formato": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/disciplina": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/disciplina-especialidade": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
    },
  },
});
