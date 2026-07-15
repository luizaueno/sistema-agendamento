import React, { useState } from 'react'
import './cadastro.css'
import axios from 'axios'
import { validarNome, validarCNPJ, validarEmail, validarSenha } from '../../../core/validations/cadastro'

interface CadastroProps {
    className: string
}

function Cadastro({ className }: CadastroProps) {

    const [dadosCadastro, setDadosCadastro] = useState({ nome: "", cnpj: "", email: "", senha: "" })

    const [erroNome, setErroNome] = useState("")
    const [erroCNPJ, setErroCNPJ] = useState("")
    const [erroEmail, setErroEmail] = useState("")
    const [erroSenha, setErroSenha] = useState("")

    function HandleChange(event: React.ChangeEvent<HTMLInputElement>) {

        const { name, value } = event.target

        setDadosCadastro({
            ...dadosCadastro,
            [name]: value 
        })

        if (name === "nome") {
            setErroNome("")
        }
        else if (name === "cnpj") {
            setErroCNPJ("")
        }
        else if (name === "email") {
            setErroEmail("")
        }
        else if (name === "senha") {
            setErroSenha("")
        }
    } 
    
    function HandleBlur(event: React.FocusEvent<HTMLInputElement>) {
        const { name, value } = event.target

        if (name === "nome") {
            const erroValidacao = validarNome(value)
            setErroNome(erroValidacao || "")
        }
        else if (name === "cnpj") {
            const erroValidacao = validarCNPJ(value)
            setErroCNPJ(erroValidacao || "")
        }
        else if (name === "email") {
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

        const eNome = validarNome(dadosCadastro.nome) || ""
        const eCNPJ = validarCNPJ(dadosCadastro.cnpj) || ""
        const eEmail = validarEmail(dadosCadastro.email) || ""
        const eSenha = validarSenha(dadosCadastro.senha) || ""

        setErroNome(eNome) 
        setErroCNPJ(eCNPJ)
        setErroEmail(eEmail)
        setErroSenha(eSenha)

        if (eNome || eCNPJ || eEmail || eSenha) {
            return
        }

        try {
            await axios.post('http://127.0.0', dadosCadastro)
            alert("Cadastro realizado com sucesso!")
        }
        catch (error) {
            console.log("ERRO: ", error)
        }
    }

    return (
        <form className={`painel painel-cadastro ${className}`} aria-labelledby="painel-cadastro" onSubmit={HandleSubmit} noValidate> 
            <h2 id="painel-cadastro" className="cadastro-title">Crie sua Conta</h2> 
            
            <fieldset className="form-cadastro-section"> 
                <legend className="sr-only">Dados da empresa</legend> 
                
                <div className="form-cadastro-group">
                    <div className="form-input-wrapper">
                        <input className={`form-cadastro-input ${erroNome ? 'input-com-erro' : ''}`} required placeholder=" " type="text" name="nome" value={dadosCadastro.nome} onChange={HandleChange} onBlur={HandleBlur} id="nome"/> 
                        <label className="form-cadastro-label" htmlFor="nome">Nome da empresa</label> 
                    </div>
                    {erroNome && (<div className="container-erro"><i className="icone">!</i><span className="form-cadastro-erro">{erroNome}</span></div>)}
                </div>

                <div className="form-cadastro-group">
                    <div className="form-input-wrapper">
                        <input className={`form-cadastro-input ${erroCNPJ ? 'input-com-erro' : ''}`} required placeholder="XX.XXX.XXX/XXXX-XX" type="text" name="cnpj" value={dadosCadastro.cnpj} onChange={HandleChange} onBlur={HandleBlur} id="cnpj"/>
                        <label className="form-cadastro-label" htmlFor="cnpj">CNPJ</label>
                    </div>
                    {erroCNPJ && (<div className="container-erro"><i className="icone">!</i><span className="form-cadastro-erro">{erroCNPJ}</span></div>)}
                </div>
            </fieldset>

            <fieldset className="form-cadastro-section">
                <legend className="sr-only">Dados de acesso</legend>
                
                <div className="form-cadastro-group">
                    <div className="form-input-wrapper">
                        <input className={`form-cadastro-input ${erroEmail ? 'input-com-erro' : ''}`} required placeholder="email@example.com" type="email" name="email" value={dadosCadastro.email} onChange={HandleChange} onBlur={HandleBlur} id="email"/>
                        <label className="form-cadastro-label" htmlFor="email">Email</label>
                    </div>
                    {erroEmail && (<div className="container-erro"><i className="icone">!</i><span className="form-cadastro-erro">{erroEmail}</span></div>)}
                </div>

                <div className="form-cadastro-group">
                    <div className="form-input-wrapper">
                        <input className={`form-cadastro-input ${erroSenha ? 'input-com-erro' : ''}`} required placeholder=" " type="password" name="senha" value={dadosCadastro.senha} onChange={HandleChange} onBlur={HandleBlur} id="senha"/> 
                        <label className="form-cadastro-label" htmlFor="senha">Senha</label>
                    </div>
                    {erroSenha && (<div className="container-erro"><i className="icone">!</i><span className="form-cadastro-erro">{erroSenha}</span></div>)}
                </div>
            </fieldset>

            <button className="form-cadastro-button" type="submit">Cadastrar</button>
        </form>
    )
}

export default Cadastro
