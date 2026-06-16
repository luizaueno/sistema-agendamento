import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './global/global.css' // css geral
import App from './presentation/App.tsx' // arquivo app - o principal, que comanda tudo

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
