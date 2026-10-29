import { validarSenha } from "../../../core/validations/login";
import React, { useState } from 'react';
import axios from 'axios';
import { useSearchParams, Link } from 'react-router-dom';
import { CheckCircle2, Eye, EyeOff, Sun, Moon } from 'lucide-react';
import './DefinirSenha.css'; 
import { useTema } from '../../App'

export function DefinirSenha() {
    const [searchParams] = useSearchParams()
    const token = searchParams.get("token")
    const { isDarkMode, inverterTema } = useTema()
    const [dadosSenha, setDadosSenha] = useState({ senha: "", confirmarSenha: "" })
    const [erroSenha, setErroSenha] = useState("")
    const [mostrarSenha, setMostrarSenha] = useState(false)
    const [mostrarConfirmarSenha, setMostrarConfirmarSenha] = useState(false);
    const [sucesso, setSucesso] = useState(false)

    function HandleChange(event: React.ChangeEvent<HTMLInputElement>) {
        const { name, value } = event.target
        setDadosSenha({ ...dadosSenha, [name]: value })
        setErroSenha("")
    }

    function HandleBlur(event: React.FocusEvent<HTMLInputElement>) {
        const { name, value } = event.target
        if (name === "senha") {
            const erroValidacao = validarSenha(value)
            setErroSenha(erroValidacao || "")
        }
    }

    async function HandleSubmit(event: React.SyntheticEvent<HTMLFormElement>) {
        event.preventDefault()

        const eSenha = validarSenha(dadosSenha.senha)
        if (eSenha) {
            setErroSenha(eSenha)
            return
        }

        if (dadosSenha.senha !== dadosSenha.confirmarSenha) {
            setErroSenha("As senhas não coincidem.")
            return
        }

        try {
            await axios.post('http://localhost:8000/profissionais/ativarconta', {
                nova_senha: dadosSenha.senha,
                token: token 
            })

            setSucesso(true)
        } catch (error) {
            if (axios.isAxiosError(error) && error.response) {
                console.log("DETALHE DO ERRO DO FASTAPI:", error.response.data);
            }
            console.error("ERRO: ", error)
            setErroSenha("Erro ao definir a senha. O link pode ter expirado ou o token é inválido.")
        }
    }

    return (
        <>
        <header id="topo-ancora" role="banner" tabIndex={-1}>
            <h1 className="titulo-sistema">Akemi Hub</h1>
            <button 
                id="alternar-tema" 
                onClick={inverterTema} 
                aria-label="Alternar tema entre claro e escuro">  
                {isDarkMode ? <Sun size={24} /> : <Moon size={24} />} 
            </button>
        </header>

        <main className="definir-senha-main">
            <div className="definir-senha-box">
                {sucesso ? (
                    <div className="sucesso-layout">
                        <div className="sucesso-icone">
                            <CheckCircle2 size={72} color="#2e7d32" strokeWidth={1.2} />
                        </div>

                        <h1 className="sucesso-texto">Senha Definida!</h1>
                        
                        <p className="senha-subtitle">
                            Sua credencial foi configurada com sucesso. 
                        </p>

                        <Link to="/login" className="tela-login-button">
                            Ir para o Login
                        </Link>
                    </div>
                ) : (
                    
                    <form onSubmit={HandleSubmit}>
                        <h1 className="senha-title">Crie sua senha</h1>
                        <p className="senha-subtitle">Defina sua senha de acesso para concluir o seu cadastro.</p>

                        {/* Campo: Nova Senha */}
                        <div className="definir-senha-group">
                            <div className="definir-senha-wrapper">
                                <input 
                                    className={`form-cadastro-input ${erroSenha ? 'input-com-erro' : ''}`} 
                                    required 
                                    placeholder=" " 
                                    type={mostrarSenha ? "text" : "password"}
                                    name="senha" 
                                    value={dadosSenha.senha} 
                                    onChange={HandleChange} 
                                    onBlur={HandleBlur} 
                                    id="senha"
                                /> 
                                <label className="form-cadastro-label" htmlFor="senha">Nova Senha</label>
                                <button
                                    type="button"
                                    className="botao-revelar-senha"
                                    onClick={() => setMostrarSenha(!mostrarSenha)}>
                                    {mostrarSenha ? <EyeOff size={20} /> : <Eye size={20} />}
                                </button>
                            </div>
                        </div>

                        {/* Campo: Confirmar Nova Senha */}
                        <div className="definir-senha-group">
                            <div className="definir-senha-wrapper">
                                <input 
                                    className={`form-cadastro-input ${erroSenha ? 'input-com-erro' : ''}`} 
                                    required 
                                    placeholder=" " 
                                    type={mostrarConfirmarSenha ? "text" : "password"}
                                    name="confirmarSenha" 
                                    value={dadosSenha.confirmarSenha} 
                                    onChange={HandleChange} 
                                    id="confirmarSenha"
                                /> 
                                <label className="form-cadastro-label" htmlFor="confirmarSenha">Confirme a senha</label>
                                <button
                                    type="button"
                                    className="botao-revelar-senha"
                                    onClick={() => setMostrarConfirmarSenha(!mostrarConfirmarSenha)}> 
                                    {mostrarConfirmarSenha ? <EyeOff size={20} /> : <Eye size={20} />}
                                </button>
                            </div>
                        </div>

                        {erroSenha && (
                            <div className="container-erro" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                <i className="icone">!</i>
                                <span className="form-login-erro">{erroSenha}</span>
                            </div>
                        )}

                            <button className="tela-login-button" type="submit">Definir Senha</button>
                        </form>
                    )}
                    
                </div>
            </main>
        </>
    );
}

export default DefinirSenha;