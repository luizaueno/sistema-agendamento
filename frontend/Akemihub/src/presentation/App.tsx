
import Cadastro from './components/auth/Cadastro';

import Login from './components/auth/Login'
import { Sun, Moon } from 'lucide-react';
import { useState, useEffect } from 'react';
import PainelBoasVindas from './components/auth/PainelBoasVindas';

function App() {

    const [isDarkMode, setIsDarkMode] = useState(true)
    useEffect(() => {
    if (!isDarkMode) {
      document.documentElement.classList.add('modo-claro'); // acha a tag html por js, onde ou retira ou adiciona o nome 'modo-claro' nessa tag, que o css usa para alterar as cores
    } else {
      document.documentElement.classList.remove('modo-claro');
    }
  }, [isDarkMode]);

    const [isLogin, setIsLogin] = useState<"login" | "cadastro">("cadastro")
   
  return (
    <div className={isLogin === "login" ? "fundo-login" : "fundo-cadastro"}>
      <div className="ancoras-navegacao" role="navigation" aria-label="acessibilidade">
        <a href="#topo-ancora" className="skip-link" accessKey="1">Ir para o topo [Alt + 1]</a>
        <a href="#menu-ancora" className="skip-link" accessKey="2">Ir para o menu de navegação [Alt + 2]</a>
        <a href="#conteudo-ancora" className="skip-link" accessKey="3">Ir para o conteúdo principal [Alt + 3]</a>
        <a href="#rodape-ancora" className="skip-link" accessKey="4">Ir para o rodapé [Alt + 4]</a>
      </div>
      <header id="topo-ancora" role="banner">
        <h1 className="titulo-sistema">Akemi Hub</h1>
        <button id="alternar-tema"  onClick={() => setIsDarkMode(!isDarkMode)} aria-label="Alternar tema entre claro e escuro">{isDarkMode ? <Sun size={24} /> : <Moon size={24} />}</button>
      </header>
      <nav id="menu-ancora" className="menu-principal" role="navigation" aria-label="Menu principal">
        <ul>
          <li><a href="index.html">Página de login e cadastro</a></li>
        </ul>
      </nav>
      <main className="container">
        <Cadastro className={isLogin === "cadastro" ? "ativo" : "inativo"}/>
        <Login className={isLogin === "login" ? "ativo" : "inativo"}/>
        <PainelBoasVindas telaAtual={isLogin} alternarTela={setIsLogin} />
      </main>
    <footer id="rodape-ancora" role="contentinfo">
      <p>&copy; 2026 Akemi Hub. Todos os direitos reservados.</p>
    </footer>
    </div>
  )
}

export default App
