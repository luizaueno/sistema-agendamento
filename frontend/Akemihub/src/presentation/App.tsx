import { useState, useLayoutEffect, createContext, useContext, type ReactNode } from 'react'
import { createBrowserRouter, RouterProvider, useNavigate, Navigate, Outlet, useLocation } from 'react-router-dom'

import '../global/global.css'
import Header from './components/ui/Header'
import Acessibilidade from './components/ui/Acessibilidade'
import './components/ui/botao.css'
import './components/ui/input.css'
import Cadastro from './components/auth/Cadastro'
import PainelBoasVindas from './components/auth/PainelBoasVindas'
import Login from './components/auth/Login'
import Footer from './components/ui/Footer'

import { Dashboard } from './components/Dashboard/Dashboard'
import { RotaProtegida } from '../infra/RotaProtegida'

// 1. Contexto de Tema
interface TemaContextData {
  isDarkMode: boolean
  inverterTema: () => void
}

interface TemaProviderProps {
  children: ReactNode
}

const TemaContext = createContext<TemaContextData | undefined>(undefined)

function Tema({ children }: TemaProviderProps) {
  const [isDarkMode, setDarkMode] = useState<boolean>(() => {
    const temaSalvo = localStorage.getItem('tema')
    return temaSalvo === null ? true : temaSalvo === 'dark'
  })

  function inverterTema() {
    const novoTema = !isDarkMode
    setDarkMode(novoTema)
    localStorage.setItem('tema', novoTema ? 'dark' : 'light')
  }

  useLayoutEffect(() => {
    if (!isDarkMode) {
      document.documentElement.classList.add('modo-claro')
    } else {
      document.documentElement.classList.remove('modo-claro')
    }
  }, [isDarkMode])

  return (
    <TemaContext.Provider value={{ isDarkMode, inverterTema }}>
      {children}
    </TemaContext.Provider>
  )
}

const useTema = () => {
  const context = useContext(TemaContext)
  if (!context) {
    throw new Error('useTema deve ser usado dentro de Tema')
  }
  return context
}

// 2. Layouts da Aplicação
function LayoutRaiz() {
  return (
    <Tema>
      <Outlet />
    </Tema>
  )
}

function ConteudoAutenticacao() {
  const { isDarkMode, inverterTema } = useTema()

  return (
    <>
      <Acessibilidade />
      <Header alternarTema={inverterTema} escuro={isDarkMode} />
      <Outlet />
      <Footer />
    </>
  )
}

function LayoutAutenticacao() {
  return (
    <Tema>
      <ConteudoAutenticacao/>
    </Tema>
  )
}

function PaginaAutenticacao() {
  const location = useLocation()
  const navigate = useNavigate()
  const isLogin = location.pathname === '/login'

  return (
    <main id="conteudo-ancora" className={`container ${isLogin ? 'modo-login' : ''}`}>
      <Cadastro className={!isLogin ? 'painel-cadastro-ativo' : 'painel-cadastro-inativo'} />
      <PainelBoasVindas 
        telaAtual={isLogin ? 'login' : 'cadastro'} 
        alternarTela={() => navigate(isLogin ? '/cadastro-empresa' : '/login')} 
      />
      <Login 
        className={isLogin ? 'painel-login-ativo' : 'painel-login-inativo'}
        onLoginSuccess={() => navigate('/dashboard')}
      />
    </main>
  )
}

// 3. Página Privada
function ConteudoDashboard() {
  const { isDarkMode, inverterTema } = useTema()
  const navigate = useNavigate()
  const perfilUsuario = (localStorage.getItem("perfil") as 'ADMIN' | 'PROFISSIONAL') || 'PROFISSIONAL'

  const efetuarLogout = () => {
    localStorage.removeItem("token")
    navigate('/login')
  }

  return (
    <Dashboard 
      onLogout={efetuarLogout} 
      alternarTema={inverterTema} 
      isDarkMode={isDarkMode}
      perfil={perfilUsuario} 
    />
  )
}

function PaginaDashboard() {
  return <ConteudoDashboard />
}

// 4. Configuração das Rotas
const router = createBrowserRouter([
  {
    path: "/",
    element: <LayoutRaiz />,
    children: [
      {
        element: <LayoutAutenticacao />,
        children: [
          {
            index: true,
            element: <Navigate to="/cadastro-empresa" replace />
          },
          {
            path: "login",
            element: <PaginaAutenticacao />
          },
          {
            path: "cadastro-empresa", 
            element: <PaginaAutenticacao />
          }
        ]
      },
      {
        element: <RotaProtegida />,
        children: [
          {
             path: "dashboard",
            element: <PaginaDashboard />,
            children: [
              {
                index: true,
                // Se o usuário acessar apenas /dashboard, ele é redirecionado de forma segura para /dashboard/agenda
                element: <Navigate to="agenda" replace /> 
              },
              {
                path: "agenda",
                element: <div>Painel da Agenda</div> // Substitua pelo seu componente <Agenda /> real
              },
              {
                path: "pacientes",
                element: <div>Painel de Pacientes</div> // Substitua pelo seu componente <Pacientes /> real
              },
              {
                path: "profissionais",
                element: <div>Painel de Profissionais</div> // Substitua pelo seu componente <Profissionais /> real
              }
            ]
          }
        ]
      },
      {
        path: "*",
        element: <Navigate to="/cadastro-empresa" replace />
      }
    ]
  }
])

function App() {
  return <RouterProvider router={router} />
}

export default App
