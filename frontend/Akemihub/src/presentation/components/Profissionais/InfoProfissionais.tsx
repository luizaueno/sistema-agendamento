import { useState } from "react";
import "./InfoProfissionais.css"; 
import { SquarePen, Trash2, Check } from 'lucide-react';

interface Profissional {
  id: number | string;
  nome: string;
  cnpj: string;
  especialidade: string;
  email: string;
  telefone: string;
  cor: string;
  status: string;
  horarios?: string;
  [key: string]: any; 
}

interface InfoProfissionaisProps {
  profissionais: Profissional[];
  aoClicarNovo?: () => void,
  aoDeletar?: (id: number | string) => void,
  aoEditar?: (dadosAtualizados: Profissional) => void 
}

export function InfoProfissionais({ profissionais, aoClicarNovo, aoDeletar, aoEditar }: InfoProfissionaisProps) {
  const [itemAtivo, setItemAtivo] = useState<number | string | null>(null);
  const [idEmEdicao, setIdEmEdicao] = useState<number | string | null>(null);
  const [dadosEditados, setDadosEditados] = useState<Profissional | null>(null);

  const toggleAccordion = (id: number | string) => {
    if (itemAtivo === id) {
      setIdEmEdicao(null);
      setDadosEditados(null);
    }
    setItemAtivo(itemAtivo === id ? null : id);
  };

  const handleInputChange = (campo: string, valor: string) => {
    if (dadosEditados) {
      setDadosEditados({
        ...dadosEditados,
        [campo]: valor
      });
    }
  };

  const handleSalvarInline = () => {
    if (aoEditar && dadosEditados) {
      aoEditar(dadosEditados); 
    }
    setIdEmEdicao(null);
    setDadosEditados(null);
  };

  return (
    <div className="accordion-container">
      {aoClicarNovo && (
          <button className="btn-cadastro" onClick={aoClicarNovo}>
            Cadastrar Novo Profissional
          </button>
      )}

      {profissionais?.map((profissional) => {
        const id = profissional.id || profissional.idprofissional;
        const nome = profissional.nome || "Nome não informado";
        const status = profissional.status || "Conta ativa";
        const estaEditandoEstaLinha = idEmEdicao === id;

        const especialidade = estaEditandoEstaLinha && dadosEditados ? dadosEditados.especialidade : (profissional.especialidade || "");
        const cnpj = estaEditandoEstaLinha && dadosEditados ? dadosEditados.cnpj : (profissional.cnpj || profissional.CNPJ || "");
        const email = estaEditandoEstaLinha && dadosEditados ? dadosEditados.email : (profissional.email || "");
        const telefone = estaEditandoEstaLinha && dadosEditados ? dadosEditados.telefone : (profissional.telefone || "");
        
        // 🛠️ RECOLOCADO: A variável que estava faltando para ler a cor corretamente
        const corAoCadastrar = estaEditandoEstaLinha && dadosEditados ? dadosEditados.cor : (profissional.cor || "#b2b7b4");
        const horarioProfissional = estaEditandoEstaLinha && dadosEditados ? dadosEditados.horarios : (profissional.horarios || "seg 9h- 10h");

        return (
          <div key={id} className="accordion-item">
            
            <div
              className={`accordion-header ${itemAtivo === id ? "ativo" : ""}`}
              onClick={() => toggleAccordion(id)}
              style={{ cursor: "pointer" }}
            >
              <div className="accordion-header-content">
                <span className="profissional-nome">{nome}</span>
                          
                <div className="acoes-container" onClick={(e) => e.stopPropagation()}>
                  {!estaEditandoEstaLinha ? (
                    <button 
                      className="btn-acao btn-editar" 
                      title="Editar" 
                      onClick={() => {
                        setItemAtivo(id);
                        setIdEmEdicao(id);
                        setDadosEditados({ 
                          ...profissional,
                          cor: profissional.cor || '#b2b7b4',
                          horarios: profissional.horarios || 'seg 9h-10h',
                        });
                      }}
                    >
                      <SquarePen size={18} strokeWidth={2} />
                    </button>
                  ) : (
                    <button 
                      className="btn-acao btn-salvar" 
                      title="Salvar" 
                      onClick={handleSalvarInline}
                    >
                      <Check size={18} strokeWidth={2} />
                    </button>
                  )}

                  <button className="btn-acao btn-deletar" title="Deletar" onClick={() => aoDeletar && aoDeletar(id)}>
                    <Trash2 size={18} strokeWidth={2}  />
                  </button>
                </div>

                <div className="status-container">
                  <span className="status-texto">{status}</span>
                  <span className={`indicador-cor ${status === "Conta ativa" ? "verde" : status === "Conta desativada" ? "vermelho" : "amarelo"}`}></span>
                </div>
              </div>

              <span className="accordion-seta">{itemAtivo === id ? "▲" : "▼"}</span>
            </div>
             
            {itemAtivo === id && (
              <div className="accordion-content" onClick={(e) => e.stopPropagation()}>
                <div className="accordion-layout-split">
                  
                  <div className="coluna-direita-config">
                    {!estaEditandoEstaLinha ? (
                      <>
                        <div className="bloco-visual-info">
                          <label>Cor da Agenda:</label>
                          <div className="visualizacao-cor-box" style={{backgroundColor: corAoCadastrar}}></div>
                        </div>
                        <div className="bloco-visual-info">
                          <label>Horários:</label>
                          <span className="tag-horario-display">{horarioProfissional}</span>
                        </div>
                      </>
                    ) : (
                      <div className="form-inputs-direita">
                        <div className="campo-inline-edicao">
                          <label>Alterar Cor:</label>
                          <input 
                            type="color" 
                            value={corAoCadastrar && corAoCadastrar.startsWith('#') ? corAoCadastrar : "#b2b7b4"} 
                            onChange={(e) => handleInputChange("cor", e.target.value)}
                            className="seletor-cor-input" 
                          />
                        </div>
                        <div className="campo-inline-edicao">
                          <label>Modificar Horários:</label>
                          <input 
                            type="text" 
                            value={horarioProfissional} 
                            onChange={(e) => handleInputChange("horarios", e.target.value)}
                            className="input-horario-texto" 
                          />
                        </div>
                      </div>
                    )}
                  </div>

                  <div className="coluna-esquerda-dados">
                    {!estaEditandoEstaLinha ? (
                      <>
                        <p><strong>Especialidade:</strong> {especialidade}</p>
                        <p><strong>CNPJ:</strong> {cnpj}</p>
                        <p><strong>E-mail:</strong> {email}</p>
                        <p><strong>Telefone:</strong> {telefone}</p>
                      </>
                    ) : (
                      <div className="form-inputs-esquerda">
                        <div className="campo-inline-edicao">
                          <label>Especialidade:</label>
                          <input 
                            type="text" 
                            value={especialidade}
                            onChange={(e) => handleInputChange("especialidade", e.target.value)}
                          />
                        </div>
                        <div className="campo-inline-edicao">
                          <label>CNPJ:</label>
                          <input 
                            type="text" 
                            value={cnpj}
                            onChange={(e) => handleInputChange("cnpj", e.target.value)}
                          />
                        </div>
                        <div className="campo-inline-edicao">
                          <label>E-mail:</label>
                          <input 
                            type="email" 
                            value={email}
                            onChange={(e) => handleInputChange("email", e.target.value)}
                          />
                        </div>
                        <div className="campo-inline-edicao">
                          <label>Telefone:</label>
                          <input 
                            type="text" 
                            value={telefone}
                            onChange={(e) => handleInputChange("telefone", e.target.value)}
                          />
                        </div>
                      </div>
                    )}
                  </div>

                </div>
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}

export default InfoProfissionais;
