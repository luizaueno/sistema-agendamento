import { useState } from "react";
import {  NavLink, Outlet } from "react-router-dom";
import './dashboard.css';
import { Menu, Calendar, Users, UserRoundGroup, LogOut} from 'lucide-react' 
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
            
                <Header alternarTema={alternarTema} escuro={isDarkMode} />
                
                <button className="sidebar-btn" onClick={() => setIsMenuOpen(!isMenuOpen)} aria-expanded={isMenuOpen} >
                    <Menu size={20} />
                </button>
                
                <nav className="sidebar-links">
                    <NavLink to="/dashboard/agenda" className="nav-btn"> 
                        <Calendar size={20} />
                        {isMenuOpen && <span className="link-label">Agenda</span>}
                    </NavLink>
                    

                    <NavLink to="/dashboard/pacientes" className="nav-btn"> 
                        <Users size={20} />
                        {isMenuOpen && <span className="link-label">Pacientes</span>}
                    </NavLink>

                    {(perfil?.toUpperCase() === 'ADMIN' || localStorage.getItem('perfil')?.toUpperCase() === 'ADMIN') && (
                        <NavLink to="/dashboard/profissionais" className="nav-btn"> 
                            <UserRoundGroup size={20}/>
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
