import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './global/global.css'
import App from './presentation/App.tsx'


// Usando createRoot e StrictMode diretamente (sem o prefixo React/ReactDOM)
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
)