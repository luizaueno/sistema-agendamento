import { useState, useLayoutEffect } from 'react';
import '../global/global.css';
import Header from './components/ui/Header';
import './components/ui/botao.css';
import './components/ui/input.css';
import Cadastro from './components/auth/Cadastro';
import PainelBoasVindas from './components/auth/PainelBoasVindas';
import Login from './components/auth/Login';
import Footer from './components/ui/Footer';
import Acessibilidade from './components/ui/Acessibilidade';

function App() {
  const [telaAtual, setTelaAtual] = useState<"login" | "cadastro">("cadastro")
  
  // 1. Criamos o estado de autenticação aqui
  const [isLogged, setIsLogged] = useState(false)

  const [isDarkMode, setDarkMode] = useState(() =>  {
    const temaSalvo = localStorage.getItem('tema')
    if (temaSalvo === null) {
      return true
    }
    return temaSalvo === 'dark'
  })

  function inverterTema() {
    const novoTema = !isDarkMode
    setDarkMode(novoTema)
    localStorage.setItem('tema', novoTema ? 'dark' : 'light')
  }

  useLayoutEffect(() => {
    if (!isDarkMode) {
      document.documentElement.classList.add('modo-claro');
    } else {
      document.documentElement.classList.remove('modo-claro');
    }
  }, [isDarkMode]);

  // 2. Se estiver logado, mostramos a futura tela principal
  if (isLogged) {
    return (
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        backgroundColor: isDarkMode ? '#1e1e1e' : '#ffffff',
        color: isDarkMode ? '#ffffff' : '#000000'
      }}>
        <h1>Futura Tela Principal</h1>
        <p>Você entrou com sucesso! 🎉</p>
        <button className="form-cadastro-button" onClick={() => setIsLogged(false)}>Sair (Logout)</button>
      </div>
    )
  }
   
  // 3. Se não estiver logado, renderiza o fluxo normal de Cadastro/Login
  return (
    <>
      <Acessibilidade/>
      <Header alternarTema={inverterTema} escuro={isDarkMode}/>
      <main id="conteudo-ancora" className={`container ${telaAtual === "login" ? "modo-login" : ""}`} role="main">
        <Cadastro className={telaAtual === "cadastro" ? "painel-cadastro-ativo" : "painel-cadastro-inativo"}/>
        <PainelBoasVindas telaAtual={telaAtual} alternarTela={setTelaAtual}/>
        {/* 4. Passamos a propriedade que muda o estado de login para true */}
        <Login 
          className={telaAtual === "login" ? "painel-login-ativo" : "painel-login-inativo"}
          onLoginSuccess={() => setIsLogged(true)}
        />
      </main>
      <Footer/>
    </>
  )
}

export default App