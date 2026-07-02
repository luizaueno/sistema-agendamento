import React, { useState } from 'react'
import './cadastro.css'
import axios from 'axios'


interface CadastroProps {
    className: string
}

function Cadastro({ className }: CadastroProps) {

    const [dadosCadastro, setDadosCadastro] = useState({ nome: "", cnpj: "", email: "", senha: "" })

    function HandleChange(event: React.ChangeEvent<HTMLInputElement>) {

        setDadosCadastro({
            ...dadosCadastro,
            [event.target.name] : event.target.value
        })
    } 
    
    async function HandleSubmit(event: React.SyntheticEvent<HTMLFormElement, SubmitEvent>) {
        event.preventDefault()
        try {
            console.log(" Enviando dados para o backend: ")

            await axios.post('http://127.0.0.1:8000/cadastrar', dadosCadastro)

            console.log("Resposta do backend: ")
            
        }

        catch {
            console.log("ERRO: ")
        }
     
    }

    return (
        <form className={`painel painel-cadastro ${className}`} aria-labelledby="painel-cadastro" onSubmit={HandleSubmit}> 
            <h2 id="painel-cadastro" className="cadastro-title">Crie sua Conta</h2> 
            
            <fieldset className="form-cadastro-section"> 
                <legend className="sr-only">Dados da empresa</legend> 
                <div className="form-cadastro-group">
                    <input className="form-cadastro-input" required placeholder=" " type="text" name="nome" value={dadosCadastro.nome} onChange={HandleChange} id="nome"/> 
                    <label className="form-cadastro-label" htmlFor="nome">Nome da empresa</label> 
                </div>
                <div className="form-cadastro-group">
                    <input className="form-cadastro-input" required placeholder="XX.XXX.XXX/XXXX-XX" type="text" name="cnpj" value={dadosCadastro.cnpj} onChange={HandleChange} id="cnpj"/>
                    <label className="form-cadastro-label" htmlFor="cnpj">CNPJ</label>
                </div>
            </fieldset>

            <fieldset className="form-cadastro-section">
                <legend className="sr-only">Dados de acesso</legend>
                <div className="form-cadastro-group">
                    <input className="form-cadastro-input" required placeholder="email@example.com" type="email" name="email" value={dadosCadastro.email} onChange={HandleChange} id="email"/>
                    <label className="form-cadastro-label" htmlFor="email">Email</label>
                </div>
                <div className="form-cadastro-group">
                    <input className="form-cadastro-input" required placeholder=" " type="password" name="senha" value={dadosCadastro.senha} onChange={HandleChange} id="senha"/> 
                    <label className="form-cadastro-label" htmlFor="senha">Senha</label>
                </div>
            </fieldset>

            <button className="form-cadastro-button" type="submit">Cadastrar</button>
        </form>
    )
}

export default Cadastro
