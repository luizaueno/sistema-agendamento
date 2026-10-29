import { useState, useLayoutEffect, createContext, useContext, useEffect, type ReactNode } from 'react'
import { createBrowserRouter, RouterProvider, useNavigate, Navigate, Outlet, useLocation } from 'react-router-dom'
import axios from 'axios'
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
import { InfoProfissionais } from './components/Profissionais/InfoProfissionais'
import { CreateProfissional } from './components/Profissionais/CreateProfissional'
import { DefinirSenha } from './components/Profissionais/DefinirSenha'

interface Profissional {
  id: number | string;
  nome: string;
  cnpj: string;
  especialidade: string;
  email: string;
  telefone: string;
  cor: string;
  status: string;
  horarios?: string; 
}

function PaginaProfissionais() {
  const [profissionais, setProfissionais] = useState<Profissional[]>([])
  const [carregando, setCarregando] = useState(true)
  const [modalExclusaoAberto, setModalExclusaoAberto] = useState(false)
  const [profissionalParaDeletar, setProfissionalParaDeletar] = useState<number | string | null>(null)

  const carregarProfissionais = async () => {
    try {
      const response = await axios.get<Profissional[]>("http://localhost:8000/profissionais");
      setProfissionais(response.data);
    } catch (error) {
      console.error("Erro ao carregar a lista de profissionais:", error);
    } finally {
      setCarregando(false);
    }
  }

  const abrirModalDeletar = (id: number | string) => {
    setProfissionalParaDeletar(id)
    setModalExclusaoAberto(true)
  }

  const confirmarExclusao = async () => {
    if (!profissionalParaDeletar) return;
    try {
      setCarregando(true)
      await axios.delete(`http://localhost:8000/profissionais/${profissionalParaDeletar}`)
      await carregarProfissionais()
    } catch (error) {
      console.error("Erro ao deletar o profissional:", error)
    } finally {
      setModalExclusaoAberto(false)
      setProfissionalParaDeletar(null)
      setCarregando(false)
    }
  }

  const editarProfissionais = async (profissionalAtualizado: any) => {
    try {
      setCarregando(true);
      const id = profissionalAtualizado.id || profissionalAtualizado.idprofissional;
      
      const dadosParaPython = {
        nome: profissionalAtualizado.nome,
        cnpj: profissionalAtualizado.cnpj,
        especialidade: profissionalAtualizado.especialidade,
        telefone: profissionalAtualizado.telefone,
        status: profissionalAtualizado.status || "Conta ativa",
        cor: profissionalAtualizado.cor,
        horarios: profissionalAtualizado.horarios 
      };

      await axios.put(`http://localhost:8000/profissionais/${id}`, dadosParaPython);

      setProfissionais((listaAntiga) =>
        listaAntiga.map((p) => {
          const pId = p.id || (p as any).idprofissional;
          if (pId === id) {
            return { ...p, ...dadosParaPython, id: pId };
          }
          return p;
        })
      );

      setCarregando(false);
      carregarProfissionais().catch((err) => 
        console.error("Erro ao atualizar lista oficial em background:", err)
      );

    } catch (error) {
      console.error("Erro ao editar o profissional:", error);
      setCarregando(false);
    }
  };

  useEffect(() => {
    carregarProfissionais()
  }, [])

  if (carregando) {
    return <div style={{ padding: "1rem", color: "var(--text-color)" }}>Carregando profissionais...</div>
  }

  return (
    <div className="painel-profissionais-wrapper">
      <CreateProfissional onCadastroSucess={carregarProfissionais} />
      <InfoProfissionais profissionais={profissionais} aoDeletar={abrirModalDeletar} aoEditar={editarProfissionais}/>
      
      {modalExclusaoAberto && (
        <div className="modal-exclusao">
          <div className="modal-conteudo">
            <p>Tem certeza que deseja excluir este profissional?</p>
            <button className="btn-modal-confirmar" onClick={confirmarExclusao}>Sim, excluir</button>
            <button className="btn-modal-cancelar" onClick={() => setModalExclusaoAberto(false)}>Cancelar</button>
          </div>
        </div>
      )}
      <Outlet context={{ carregarProfissionais }} />
    </div>
  )
}

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

export const useTema = () => {
  const context = useContext(TemaContext)
  if (!context) {
    throw new Error('useTema deve ser usado dentro de Tema')
  }
  return context
}

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
  return <ConteudoAutenticacao />
}

function PaginaAutenticacao() {
  const location = useLocation()
  const navigate = useNavigate()
  const isLogin = location.pathname === '/login'

  return (
    <main id="conteudo-ancora" className={`container ${isLogin ? 'modo-login' : ''}`}>
      <Cadastro className={!isLogin ? 'painel-cadastro-ativo' : 'painel-cadastro-inativo'} />
      <PainelBoasVindas telaAtual={isLogin ? 'login' : 'cadastro'} alternarTela={() => navigate(isLogin ? '/cadastro-empresa' : '/login')} />
      <Login className={isLogin ? 'painel-login-ativo' : 'painel-login-inativo'} onLoginSuccess={() => navigate('/dashboard')} />
    </main>
  )
}

function ConteudoDashboard() {
  const { isDarkMode, inverterTema } = useTema()
  const navigate = useNavigate()
  
  const perfilBruto = localStorage.getItem("perfil")
  
  // Declaramos a variável já tipada com a interface estrita do seu Dashboard
  let perfilUsuario: 'ADMIN' | 'PROFISSIONAL' | 'PROFISSIONAL-ADMIN'

  // 🚀 CORREÇÃO DA REGRA: Se o usuário logado for o Administrador Geral da Empresa ('ADMIN'),
  // injetamos a string 'ADMIN' para trazer o menu de profissionais de volta!
  if (perfilBruto === '4' || perfilBruto === 'ADMIN' || perfilBruto === 'PROFISSIONAL-ADMIN') {
    perfilUsuario = 'ADMIN' 
  } else {
    // Caso seja o profissional comum convidado (nível 3)
    perfilUsuario = 'PROFISSIONAL' 
  }

  const efetuaráLogout = () => {
    localStorage.removeItem("token")
    localStorage.removeItem("perfil") 
    navigate('/login')
  }

  return (
    <Dashboard onLogout={efetuaráLogout} alternarTema={inverterTema} isDarkMode={isDarkMode} perfil={perfilUsuario} />
  )
}


function PaginaDashboard() {
  return <ConteudoDashboard />
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <LayoutRaiz />,
    children: [
      {
        element: <LayoutAutenticacao />,
        children: [
          { index: true, element: <Navigate to="/cadastro-empresa" replace /> },
          { path: "login", element: <PaginaAutenticacao /> },
          { path: "cadastro-empresa", element: <PaginaAutenticacao /> }
        ]
      },
      {
        path: "definir-senha",
        element: <DefinirSenha />
      },
      {
        element: <RotaProtegida />,
        children: [
          {
            path: "dashboard",
            element: <PaginaDashboard />,
            children: [
              { index: true, element: <Navigate to="agenda" replace /> },
              { path: "agenda", element: <div>Painel da Agenda</div> },
              { path: "pacientes", element: <div>Painel de Pacientes</div> },
              { path: "profissionais", element: <PaginaProfissionais /> }
            ]
          }
        ]
      }
    ]
  }
]);

export default function App() {
  return <RouterProvider router={router} />
}
