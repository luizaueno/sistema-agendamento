import { useState } from "react" 
import './CreateProfissional.css' 

export function CreateProfissional() { 
  const [cadastroProfissionalAberto, setCadastroProfissionalAberto] = useState(false);

  return ( 
    <> 
      <div className="profissional-container"> 
        <h2 className="title">Profissionais</h2> 
        <button className="btn-cadastro" onClick={() => setCadastroProfissionalAberto(true)}>
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
          <div className="conteudo-formulario" onClick={(e) => e.stopPropagation()}> 
            <>
              <h3 className="subtitle">Cadastre um profissional</h3> 
              <input className="form-input" type="text" placeholder="Nome" /> 
              <input className="form-input" type="text" placeholder="CNPJ" /> 
              <input className="form-input" type="text" placeholder="Especialidade" /> 
              <input className="form-input" type="text" placeholder="Telefone" /> 
              <input className="form-input" type="email" placeholder="Email" /> 
              
              <div className="form-input-tag">Segunda 10h-16h</div> 
              
              <div className="bloco-input-cor">
                <input className="form-input-color picker" type="color" defaultValue="#88003F" />
                <span className="aviso-cor">* Esta cor será usada para identificar o profissional na agenda.</span>
              </div> 
              
              <button className="form-cadastro-btn">
                <span>Cadastrar e enviar convite</span>
              </button> 
            </>
          </div> 
        </div>
      )}
    </>
  )
}
