import React, { useState } from 'react'
import './login.css'
import axios from 'axios'
import { validarEmail, validarSenha } from '../../../core/validations/login'
import { Eye, EyeOff } from 'lucide-react'

interface LoginProps {
    className: string
    onLoginSuccess: () => void
}

function Login({ className, onLoginSuccess }: LoginProps) {

    const [dadosLogin, setDadosLogin] = useState({ email: "", senha: ""})

    const [erroEmail, setErroEmail] = useState<string | null>(null)
    const [erroSenha, setErroSenha] = useState("")
    const [erroGeral, setErroGeral] = useState<string | null>(null) // Novo estado para capturar erros do backend (Ex: 401)
    const [mostrarSenha, setMostrarSenha] = useState(false)

    function HandleChange(event: React.ChangeEvent<HTMLInputElement>) {

        const { name, value } = event.target

        setDadosLogin({
            ...dadosLogin,
            [name] : value
        })

        // Limpa o erro geral do backend assim que o usuário mexe nos inputs
        setErroGeral(null)

        if (name === "email") {
            setErroEmail("")
        }
        else if (name === "senha") {
            setErroSenha("")
        }
    }

    function HandleBlur(event: React.FocusEvent<HTMLInputElement>) {
        const { name, value } = event.target

        if (name === "email") {
            const erroValidacao = validarEmail(value)
            setErroEmail(erroValidacao || "")
        }
        else if (name === "senha") {
            const erroValidacao = validarSenha(value)
            setErroSenha(erroValidacao || "")
        }
    }

    async function HandleSubmit(event: React.SyntheticEvent<HTMLFormElement, SubmitEvent>) {

        event.preventDefault()
        setErroGeral(null) // Limpa o erro antes de tentar

        const eEmail = validarEmail(dadosLogin.email)
        const eSenha = validarSenha(dadosLogin.senha)

        setErroEmail(eEmail)
        setErroSenha(eSenha)

        if (eEmail || eSenha) {
            return
        }

        try {
            const resposta = await axios.post('http://localhost:8000/login', dadosLogin)
            localStorage.setItem("token", resposta.data.token)
            localStorage.setItem("perfil", resposta.data.perfil) 
            onLoginSuccess()
        }
        catch (error: any) {
            // ISSO VAI MOSTRAR NO CONSOLE EXATAMENTE O QUE O BACKEND MANDOU
            console.log("--- DIAGNÓSTICO DE ERRO ---")
            console.log("Status do erro:", error.response?.status)
            console.log("Dados que vieram do backend:", error.response?.data)
            console.dir(error)

            // Se o backend respondeu 401, vamos forçar o texto na tela
            if (error.response && error.response.status === 401) {
                const backendMsg = error.response.data?.detail || error.response.data
                
                if (typeof backendMsg === 'string') {
                    setErroGeral(backendMsg)
                } else {
                    setErroGeral("E-mail ou senha incorretos.")
                }
            } else {
                setErroGeral("Não foi possível conectar ao servidor.")
            }
        }
    }

    return (
        <form className={`painel painel-login ${className}`} aria-labelledby="titulo-login" onSubmit={HandleSubmit} noValidate> 
            <fieldset className="login-section">
                <div className="tela-login-group">
                    <h1 id="titulo-login" className="login-title">Login</h1>
                </div>
                <div className="tela-login-group">
                    <div className="form-input-wrapper">
                        <input className={`tela-login-input ${erroEmail ? 'input-com-erro' : ''}`} required placeholder="email@example.com" type="email" name="email" value={dadosLogin.email} onChange={HandleChange} onBlur={HandleBlur} id="login-email"/>
                        <label className="tela-login-label" htmlFor="login-email">Email</label>
                    </div>
                {erroEmail && (<div className="container-erro"><i className="icone">!</i><span className="form-login-erro">{erroEmail}</span></div>)}
                </div>
                <div className="tela-login-group">
                  <div className="form-input-wrapper">
                    <input className={`form-cadastro-input ${erroSenha ? 'input-com-erro' : ''}`} required placeholder=" " type={mostrarSenha ? "text" : "password"} name="senha" value={dadosLogin.senha} onChange={HandleChange} onBlur={HandleBlur} id="senha"/> 
                    <label className="form-cadastro-label" htmlFor="senha">Senha</label>
                    <button
                        type="button"
                        className="botao-revelar-senha"
                        onClick={() => setMostrarSenha(!mostrarSenha)}>
                        {mostrarSenha ? <EyeOff size={20} /> : <Eye size={20} />}
                    </button>
                </div>
                {erroSenha && (<div className="container-erro"><i className="icone">!</i><span className="form-login-erro">{erroSenha}</span></div>)}
                </div>

                {/* Bloco adicionado para exibir o erro do Backend */}
                {erroGeral && (
                    <div className="container-erro geral">
                        <i className="icone">!</i>
                        <span className="form-login-erro">{erroGeral}</span>
                    </div>
                )}
                                
                <button className="tela-login-button" type="submit">Entrar</button>
            </fieldset>
        </form>
    )
}

export default Login
