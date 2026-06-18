import './cadastro.css'

interface CadastroProps {
    className: string
}

function Cadastro({ className }: CadastroProps) {
    return(
        <form className={`painel-cadastro ${className}`} aria-labelledby="painel-cadastro"> 
        <h2 id="painel-cadastro" className="cadastro-title">Crie sua Conta</h2> 
        
        <fieldset className="form-cadastro-section"> 
            <legend className="sr-only">Dados da empresa</legend> 
            <div className="form-cadastro-group">
                <input className="form-cadastro-input" required placeholder=" " type="text" name="nome" id="nome"/> 
                <label className="form-cadastro-label" htmlFor="nome">Nome da empresa</label> 
            </div>
            <div className="form-cadastro-group">
                <input className="form-cadastro-input" required placeholder="XX.XXX.XXX/XXXX-XX" type="text" name="cnpj" id="cnpj"/>
                <label className="form-cadastro-label" htmlFor="cnpj">CNPJ</label>
            </div>
        </fieldset>

        <fieldset className="form-cadastro-section">
            <legend className="sr-only">Dados de acesso</legend>
            <div className="form-cadastro-group">
                <input className="form-cadastro-input" required placeholder="email@example.com" type="email" name="email" id="email"/>
                <label className="form-cadastro-label" htmlFor="email">Email</label>
            </div>
            <div className="form-cadastro-group">
                <input className="form-cadastro-input" required placeholder=" " type="password" name="senha" id="senha"/> 
                <label className="form-cadastro-label" htmlFor="senha">Senha</label>
            </div>
        </fieldset>

        <button className="form-cadastro-button" type="submit">Cadastrar</button>
    </form>
    )
}


export default Cadastro