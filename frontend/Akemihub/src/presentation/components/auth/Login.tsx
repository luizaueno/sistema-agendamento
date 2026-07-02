import React, { useState } from 'react'
import './login.css'



interface LoginProps {
    className: string
}

function Login({ className }: LoginProps) {

    const [dadosLogin, setDadosLogin] = useState({ email: "", senha: ""})

    function HandleChange(event: React.ChangeEvent<HTMLInputElement>) {

        setDadosLogin({
            ...dadosLogin,
            [event.target.name] : event.target.value
        })
    }

    function HandleSubmit(event: React.SyntheticEvent<HTMLFormElement, SubmitEvent>) {

        event.preventDefault()
    }
    
    return (
        <form className={`painel painel-login ${className}`} aria-labelledby="titulo-login" onSubmit={HandleSubmit}> 
            <fieldset className="login-section">
                <div className="tela-login-group">
                    <h1 id="titulo-login" className="login-title">Login</h1>
                </div>
                <div className="tela-login-group">
                    <input type="email" name="email" value={dadosLogin.email} onChange={HandleChange} id="login-email" className="tela-login-input" required placeholder="email@example.com"/>
                    <label className="tela-login-label" htmlFor="login-email">Email</label>
                </div>
                <div className="tela-login-group">
                    <input type="password" name="senha" value={dadosLogin.senha} onChange={HandleChange} id="login-senha" className="tela-login-input" required placeholder=" " />
                    <label className="tela-login-label" htmlFor="login-senha">Senha</label>
                </div>
                
                <button className="tela-login-button" type="submit">Entrar</button>
            </fieldset>
        </form>
    )
}

export default Login
