import './login.css'

interface LoginProps {
    className: string
}

function Login({ className }: LoginProps) {
    return (
        <form className={className} aria-labelledby="titulo-login"> 
            <fieldset className="login-section">
                <div className="tela-login-group">
                    <h1 id="titulo-login" className="login-title">Login</h1>
                </div>
                <div className="tela-login-group">
                    <input 
                        type="email" 
                        name="email" 
                        id="login-email" 
                        className="tela-login-input" 
                        required 
                        placeholder="email@example.com"
                    />
                    <label className="tela-login-label" htmlFor="login-email">Email</label>
                </div>
                <div className="tela-login-group">
                    <input 
                        type="password" 
                        name="senha" 
                        id="login-senha" 
                        className="tela-login-input" 
                        required 
                        placeholder=" "
                    />
                    <label className="tela-login-label" htmlFor="login-senha">Senha</label>
                </div>
                
                <button className="tela-login-button" type="submit">Entrar</button>
            </fieldset>
        </form>
    )
}

export default Login
