import React, { useState } from 'react'
import './login.css'
import axios from 'axios'
import { validarEmail, validarSenha } from '../../../core/validations/login'


interface LoginProps {
    className: string
    onLoginSuccess: () => void
}

function Login({ className, onLoginSuccess }: LoginProps) {

    const [dadosLogin, setDadosLogin] = useState({ email: "", senha: ""})

    const [erroEmail, setErroEmail] = useState<string | null>(null)
    const [erroSenha, setErroSenha] = useState("")

    function HandleChange(event: React.ChangeEvent<HTMLInputElement>) {

        const { name, value } = event.target

        setDadosLogin({
            ...dadosLogin,
            [name] : value
        })

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

        const eEmail = validarEmail(dadosLogin.email)
        const eSenha = validarSenha(dadosLogin.senha)

        setErroEmail(eEmail)
        setErroSenha(eSenha)

        if ( eEmail || eSenha) {
            return
        }

        try {
            const resposta = await axios.post('http://localhost:8000/login', dadosLogin)
            localStorage.setItem("token", resposta.data.token)
            onLoginSuccess()
        }
        catch (error) {
            console.log("ERRO: ", error)
        }
    }
    
    return (
        <form className={`painel painel-login ${className}`} aria-labelledby="titulo-login" onSubmit={HandleSubmit}noValidate> 
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
                    <input className={`form-cadastro-input ${erroSenha ? 'input-com-erro' : ''}`} required placeholder=" " type="password" name="senha" value={dadosLogin.senha} onChange={HandleChange} onBlur={HandleBlur} id="senha"/> 
                        <label className="form-cadastro-label" htmlFor="senha">Senha</label>
                </div>
                {erroSenha && (<div className="container-erro"><i className="icone">!</i><span className="form-login-erro">{erroSenha}</span></div>)}
                </div>
                
                <button className="tela-login-button" type="submit">Entrar</button>
            </fieldset>
        </form>
    )
}

export default Login
