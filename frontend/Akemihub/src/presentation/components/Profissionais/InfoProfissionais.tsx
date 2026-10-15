import { useState } from "react";
import "./InfoProfissionais.css"; 
import { SquarePen, Trash2 } from 'lucide-react';

interface Profissional {
  id: number | string;
  nome: string;
  cnpj: string;
  especialidade: string;
  email: string;
  telefone: string;
  cor: string;
  status: string;
  // Permitir chaves alternativas que o MySQL costuma mandar
  [key: string]: any; 
}

interface InfoProfissionaisProps {
  profissionais: Profissional[];
  aoClicarNovo?: () => void;
}

export function InfoProfissionais({ profissionais, aoClicarNovo }: InfoProfissionaisProps) {
  const [itemAtivo, setItemAtivo] = useState<number | string | null>(null);

  // 🕵️‍♂️ LOG PARA PEGAR A CHARADA: Abra o console do navegador (F12) e veja como o objeto chegou!
  console.log("DADOS EXATOS RECEBIDOS NO REACT:", profissionais);

  const toggleAccordion = (id: number | string) => {
    setItemAtivo(itemAtivo === id ? null : id);
  };
 
  return (
    <div className="accordion-container">
      {aoClicarNovo && (
          <button className="btn-cadastro" onClick={aoClicarNovo}>
            Cadastrar Novo Profissional
          </button>
      )}

      {profissionais?.map((profissional) => {
        // 🛠️ MAPEAMENTO EM TEMPO DE EXECUÇÃO: 
        // Se o banco mandou 'CNPJ' ou 'idprofissional', nós convertemos na hora para não exibir em branco.
        const id = profissional.id || profissional.idprofissional;
        const nome = profissional.nome || "Nome não informado";
        const especialidade = profissional.especialidade || "";
        const cnpj = profissional.cnpj || profissional.CNPJ || "";
        const email = profissional.email || "";
        const telefone = profissional.telefone || "";
        const status = profissional.status || "Conta ativa";

        return (
          <div key={id} className="accordion-item">
            
            <div
              className={`accordion-header ${itemAtivo === id ? "ativo" : ""}`}
              onClick={() => toggleAccordion(id)}
              style={{ cursor: "pointer" }}
            >
              <div className="accordion-header-content">
                {/* 🛠️ Exibe o nome que estava vindo invisível no cabeçalho */}
                <span className="profissional-nome">{nome}</span>
                          
                <div className="acoes-container" onClick={(e) => e.stopPropagation()}>
                  <button className="btn-acao btn-editar" title="Editar">
                    <SquarePen size={18} strokeWidth={2} />
                  </button>
                  <button className="btn-acao btn-deletar" title="Deletar">
                    <Trash2 size={18} strokeWidth={2} />
                  </button>
                </div>

                <div className="status-container">
                  <span className="status-texto">{status}</span>
                  <span 
                    className={`indicador-cor ${
                      status === "Conta ativa" ? "verde" : 
                      status === "Conta desativada" ? "vermelho" : "amarelo"
                    }`}
                  ></span>
                </div>
              </div>

              <span className="accordion-seta">
                {itemAtivo === id ? "▲" : "▼"}
              </span>
            </div>
             
            {itemAtivo === id && (
              <div className="accordion-content">
                <p><strong>Especialidade:</strong> {especialidade}</p>
                <p><strong>CNPJ:</strong> {cnpj}</p>
                <p><strong>E-mail:</strong> {email}</p>
                <p><strong>Telefone:</strong> {telefone}</p>
              </div>
            )}
            
          </div>
        );
      })}
    </div>
  );
}

export default InfoProfissionais;
