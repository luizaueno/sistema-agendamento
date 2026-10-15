import { validarSenha } from "../../../core/validations/login";
import React, { useState } from 'react';
import axios from 'axios';
import { useSearchParams, Link } from 'react-router-dom';
import { CheckCircle2 } from 'lucide-react';
import './DefinirSenha.css'; // Importando o CSS limpo

export function DefinirSenha() {
    const [searchParams] = useSearchParams()
    const token = searchParams.get("token")

    const [dadosSenha, setDadosSenha] = useState({ senha: "", confirmarSenha: "" });
    const [erroSenha, setErroSenha] = useState("");
    const [sucesso, setSucesso] = useState(true);

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
            await axios.post('http://localhost:8000/definirsenha', {
                senha: dadosSenha.senha,
                token: token 
            })

            setSucesso(true)
        } catch (error) {
            console.error("ERRO: ", error)
            setErroSenha("Erro ao definir a senha. O link pode ter expirado.")
        }
    }

    return (
        <main id="conteudo-ancora" className="container modo-login">
            <div className="conteudo-formulario">
                
                {/* 2. TELA FIXA DE SUCESSO (ESTILO MANUAL APENAS NO ALINHAMENTO) */}
                {sucesso ? (
                    <div className="sucesso-layout">
                        <div className="sucesso-icone">
                            <CheckCircle2 size={72} color="#2e7d32" strokeWidth={1.2} />
                        </div>

                        <h1 className="sucesso-texto">Senha Definida!</h1>
                        
                        <p className="senha-subtitle">
                            Sua credencial foi configurada com sucesso. 
                        </p>

                        <Link to="/" className="tela-login-button" >
                            Ir para o Login
                        </Link>
                    </div>
                ) : (
                    
                    /* 3. FORMULÁRIO DE CADASTRO DE SENHA TOTALMENTE INTEGRADO AO SEU PROJETO */
                    <form onSubmit={HandleSubmit}>
                        <h1 className="senha-title">Crie sua senha</h1>
                        <p className="senha-subtitle">Defina sua senha de acesso para concluir o seu cadastro.</p>

                        {/* Campo: Nova Senha */}
                        <div className="tela-login-group" style={{ marginBottom: '20px' }}>
                            <div className="form-input-wrapper">
                                <input 
                                    className={`form-cadastro-input ${erroSenha ? 'input-com-erro' : ''}`} 
                                    required 
                                    placeholder=" " 
                                    type="password" 
                                    name="senha" 
                                    value={dadosSenha.senha} 
                                    onChange={HandleChange} 
                                    onBlur={HandleBlur} 
                                    id="senha"
                                /> 
                                <label className="form-cadastro-label" htmlFor="senha">Nova Senha</label>
                            </div>
                        </div>

                        {/* Campo: Confirmar Nova Senha */}
                        <div className="tela-login-group" style={{ marginBottom: '20px' }}>
                            <div className="form-input-wrapper">
                                <input 
                                    className={`form-cadastro-input ${erroSenha ? 'input-com-erro' : ''}`} 
                                    required 
                                    placeholder=" " 
                                    type="password" 
                                    name="confirmarSenha" 
                                    value={dadosSenha.confirmarSenha} 
                                    onChange={HandleChange} 
                                    id="confirmarSenha"
                                /> 
                                <label className="form-cadastro-label" htmlFor="confirmarSenha">Confirme a senha</label>
                            </div>
                        </div>

                        {/* Mensagem de Erro baseada nas suas classes nativas de erro */}
                        {erroSenha && (
                            <div className="container-erro" style={{ marginBottom: '20px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                                <i className="icone">!</i>
                                <span className="form-login-erro">{erroSenha}</span>
                            </div>
                        )}

                        <button className="tela-login-button" type="submit">Definir Senha</button>
                    </form>
                )}
                
            </div>
        </main>
    );
}

export default DefinirSenha;
