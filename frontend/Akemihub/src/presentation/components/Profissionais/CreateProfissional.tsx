import React, { useState } from "react" 
import './CreateProfissional.css'
import axios from 'axios'
import { validarNome, validarEspecialidade, validarCNPJ, validarEmail, validarTelefone } from '../../../core/validations/profissional'

interface CreateProfissionalProps {
  className?: string
  onCadastroSucess: () => void
}

export function CreateProfissional({className, onCadastroSucess}: CreateProfissionalProps) {
  const [dadosProfissional, setDadosProfissional] = useState({
    nome: "", cnpj:"", especialidade: "", email: "", telefone:"", cor: "#E3E7ED"
  }) 

  const [erroNome, setErroNome] = useState("")
  const [erroCNPJ, setErroCNPJ] = useState("")
  const [erroEmail, setErroEmail] = useState("")
  const [erroTelefone, setErroTelefone] = useState("")
  const [erroEspecialidade, setErroEspecialidade] = useState("")
  const [cadastroProfissionalAberto, setCadastroProfissionalAberto] = useState(false)
  const [erroEnvio, setErroEnvio] = useState("")
  const [sucessoEnvio, setSucessoEnvio] = useState(false)
  const [carregando, setCarregando] = useState(false) 

  function HandleChange(event: React.ChangeEvent<HTMLInputElement>) {
    const { name, value } = event.target

    setDadosProfissional({
      ...dadosProfissional, [name]: value
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
    else if (name === "especialidade") {
        setErroEspecialidade("")
    }
    else if (name === "telefone") {
        setErroTelefone("")
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
    else if (name === "especialidade") {
      const erroValidacao = validarEspecialidade(value)
      setErroEspecialidade(erroValidacao || "")
    }
    else if (name === "telefone") {
      const erroValidacao = validarTelefone(value)
      setErroTelefone(erroValidacao || "")
    }
  }

  async function HandleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setErroEnvio("")
    
    const eNome = validarNome(dadosProfissional.nome) || ""
    const eCNPJ = validarCNPJ(dadosProfissional.cnpj) || ""
    const eEmail = validarEmail(dadosProfissional.email) || ""
    const eEspecialidade = validarEspecialidade(dadosProfissional.especialidade) || ""
    const eTelefone = validarTelefone(dadosProfissional.telefone) || ""

    setErroNome(eNome) 
    setErroCNPJ(eCNPJ)
    setErroEmail(eEmail)
    setErroEspecialidade(eEspecialidade)
    setErroTelefone(eTelefone)

    if (eNome || eCNPJ || eEmail || eEspecialidade || eTelefone) {
        return
    }
    
    try {
      setCarregando(true)
      setErroEnvio("")
      await axios.post('http://localhost:8000/profissionais', dadosProfissional)
      onCadastroSucess()
      setSucessoEnvio(true) 
      setDadosProfissional({ nome: "", cnpj: "", especialidade: "", email: "", telefone: "", cor: "#E3E7ED" })
      
      // 3. Aguarda 3 segundos com o aviso na tela antes de fechar tudo
      setTimeout(() => {
        setCadastroProfissionalAberto(false)
        setSucessoEnvio(false) // Reseta o estado de sucesso
      }, 3000)
    }
    catch (error: any) {
        if (error.response && error.response.data && error.response.data.message) {
          setErroEnvio(error.response.data.message)
      } else {
          setErroEnvio("Não foi possível conectar ao servidor. Tente novamente mais tarde.")
      }
      setTimeout(() => {
        setErroEnvio("")
      }, 7000)
    }
    finally {
      setCarregando(false)
    }
  }

  return ( 
    <> 
      <div className="profissional-container"> 
        <h2 className="title">Profissionais</h2> 
        <button className="btn-cadastro-novo" onClick={() => setCadastroProfissionalAberto(true)}>
          Cadastrar
        </button> 
      </div> 

      {cadastroProfissionalAberto && ( 
        <div 
          className="container-formulario" 
          onClick={(e) => {
            if (e.target === e.currentTarget) {
              setCadastroProfissionalAberto(false);
            }
          }}
        > 
            {sucessoEnvio && (
              <div className="aviso-flutuante sucesso">
                Cadastro realizado com sucesso!
              </div>
            )}

            {erroEnvio && (
            <div className="aviso-flutuante erro">
              ❌ {erroEnvio}
            </div>
        )}
          <form onSubmit={HandleSubmit} className={`conteudo-formulario ${className ?? ""}`.trim()}>
          <h3 className="subtitle">Cadastre um profissional</h3>
            {/* Campo: Nome */}
            <div className="form-cadastro-group">
              <input 
                className={`form-input ${erroNome ? 'input-com-erro' : ''}`} 
                placeholder="Nome do profissional" 
                type="text" 
                name="nome" 
                value={dadosProfissional.nome} 
                onChange={HandleChange} 
                onBlur={HandleBlur} 
                id="nome"
              />
              {erroNome && (
                <div className="container-erro">
                  <i className="icone">!</i>
                  <span className="form-cadastro-erro">{erroNome}</span>
                </div>
              )}
            </div>

            {/* Campo: CNPJ */}
            <div className="form-cadastro-group">
              <input 
                className={`form-input ${erroCNPJ ? 'input-com-erro' : ''}`} 
                type="text" 
                placeholder="CNPJ" 
                name="cnpj" 
                value={dadosProfissional.cnpj} 
                onChange={HandleChange} 
                onBlur={HandleBlur} 
                id="cnpj" 
              /> 
              {erroCNPJ && (
                <div className="container-erro">
                  <i className="icone">!</i>
                  <span className="form-cadastro-erro">{erroCNPJ}</span>
                </div>
              )}
            </div>

            {/* Campo: Especialidade */}
            <div className="form-cadastro-group">
              <input 
                className={`form-input ${erroEspecialidade ? 'input-com-erro' : ''}`} 
                type="text" 
                placeholder="Especialidade" 
                name="especialidade" 
                value={dadosProfissional.especialidade} 
                onChange={HandleChange} 
                onBlur={HandleBlur} 
                id="especialidade" 
              /> 
              {erroEspecialidade && (
                <div className="container-erro">
                  <i className="icone">!</i>
                  <span className="form-cadastro-erro">{erroEspecialidade}</span>
                </div>
              )}
            </div>

            {/* Campo: Telefone */}
            <div className="form-cadastro-group">
              <input 
                className={`form-input ${erroTelefone ? 'input-com-erro' : ''}`} 
                type="text" 
                placeholder="Telefone" 
                name="telefone" 
                value={dadosProfissional.telefone} 
                onChange={HandleChange} 
                onBlur={HandleBlur} 
                id="telefone" 
              /> 
              {erroTelefone && (
                <div className="container-erro">
                  <i className="icone">!</i>
                  <span className="form-cadastro-erro">{erroTelefone}</span>
                </div>
              )}
            </div>

            {/* Campo: Email */}
            <div className="form-cadastro-group">
              <input 
                className={`form-input ${erroEmail ? 'input-com-erro' : ''}`} 
                type="email" 
                placeholder="E-mail" 
                name="email" 
                value={dadosProfissional.email} 
                onChange={HandleChange} 
                onBlur={HandleBlur} 
                id="email" 
              /> 
              {erroEmail && (
                <div className="container-erro">
                  <i className="icone">!</i>
                  <span className="form-cadastro-erro">{erroEmail}</span>
                </div>
              )}
            </div>

            <div className="bloco-input-cor">
              <input 
                className="form-input-color picker" 
                type="color"  
                name="cor"
                value={dadosProfissional.cor}
                onChange={HandleChange}
              />
              <span className="aviso-cor">* Esta cor será usada para identificar o profissional na agenda.</span>
            </div> 

            <button type="submit" className="btn-cadastro" disabled={carregando}>
              {carregando ? "Cadastrando..." : "Confirmar Cadastro"}
            </button>
          </form>
        </div> 
      )} 
    </> 
  )
}
