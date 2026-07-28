import { useState } from "react";
import { Outlet, NavLink } from "react-router-dom";
import './dashboard.css';
import { Menu, Calendar, Users, LogOut, ShieldAlert} from 'lucide-react' // Adicionados os ícones para o menu
import Header from '../ui/Header';

interface DashboardProps {
    onLogout: () => void       
    alternarTema: () => void   
    isDarkMode: boolean  
    perfil: 'ADMIN' | 'PROFISSIONAL'      
}

export const Dashboard = ({ onLogout, alternarTema, isDarkMode, perfil }: DashboardProps) => {
    const [isMenuOpen, setIsMenuOpen] = useState(true)

    return (
        <div className="dashboard-container">
            <aside className={`dashboard-sidebar ${isMenuOpen ? 'aberto' : 'recolhido'}`} aria-label="Menu lateral">
                {/* O seu Header original de volta ao topo exato da barra lateral */}
                <Header alternarTema={alternarTema} escuro={isDarkMode} />
                
                <button className="sidebar-btn" onClick={() => setIsMenuOpen(!isMenuOpen)} aria-expanded={isMenuOpen} >
                    <Menu size={20} />
                </button>
                
                <nav className="sidebar-links">
                    {/* Link corrigido com o ícone da Agenda */}
                    <NavLink to="/dashboard/agenda" className="nav-btn"> 
                        <Calendar size={20} />
                        {isMenuOpen && <span className="link-label">Agenda</span>}
                    </NavLink>
                    
                    {/* Link corrigido com o ícone de Pacientes */}
                    <NavLink to="/dashboard/pacientes" className="nav-btn"> 
                        <Users size={20} />
                        {isMenuOpen && <span className="link-label">Pacientes</span>}
                    </NavLink>
                    
                    {/* Link corrigido com o ícone de Profissionais (Apenas ADMIN) */}
                    {perfil === 'ADMIN' && (
                        <NavLink to="/dashboard/profissionais" className="nav-btn"> 
                            <ShieldAlert size={20} />
                            {isMenuOpen && <span className="link-label">Profissionais</span>}
                        </NavLink>
                    )}
                </nav>
                <button className="logout-button" onClick={onLogout}>
                     <LogOut size={20} />
                    {isMenuOpen && <span className="logout-text">Sair</span>}
                </button>
            </aside>
            
            <main className="dashboard-content">
                <Outlet/>
            </main>
        </div>
    )
}
