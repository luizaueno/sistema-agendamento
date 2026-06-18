import { useState, useEffect } from 'react';
import '../global/global.css';
import Acessibilidade from './components/ui/Acessibilidade';
import Header from './components/ui/Header';
import Cadastro from './components/auth/Cadastro';
import PainelBoasVindas from './components/auth/PainelBoasVindas';
import Login from './components/auth/Login';
import Footer from './components/ui/Footer';

function App() {
  const [telaAtual, setTelaAtual] = useState<"login" | "cadastro" >("cadastro")
  const [isDarkMode, setDarkMode] = useState(true)

  function inverterTema() {
    setDarkMode(!isDarkMode)
  }

  useEffect(() => {
    if (!isDarkMode) {
      document.documentElement.classList.add('modo-claro');
    } else {
      document.documentElement.classList.remove('modo-claro');
    }
  }, [isDarkMode]);
   
  return (
    <>
    <Acessibilidade />
    <Header alternarTema={inverterTema} escuro={isDarkMode}/>
    <main>
      <Cadastro className={telaAtual === "cadastro" ? "painel-cadastro-ativo" : "painel-cadastro-inativo"}/>
      <PainelBoasVindas telaAtual={telaAtual} alternarTela={setTelaAtual}/>
      <Login className={telaAtual === "login" ? "painel-login-ativo" : "painel-login-inativo"}/>
    </main>
    <Footer/>
    </>

  )
}

export default App;
