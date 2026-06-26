import { Sun, Moon } from 'lucide-react';
import './header.css';

interface HeaderProps {
    alternarTema:() => void
    escuro: boolean
}

function Header({ alternarTema, escuro }: HeaderProps) {
    return (
        <header id="topo-ancora" role="banner" tabIndex={-1}>
        <h1 className="titulo-sistema">Akemi Hub</h1>
        <button id="alternar-tema" onClick={alternarTema} aria-label="Alternar tema entre claro e escuro">  {escuro ? <Sun size={24} /> : <Moon size={24} />} </button>
      </header>
    )
}

export default Header