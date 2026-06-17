import './painelboasvindas.css'

interface PainelProps {
    telaAtual: "login" | "cadastro";
    alternarTela: (tela: "login" | "cadastro") => void
}

function PainelBoasVindas({telaAtual, alternarTela}: PainelProps) {
    return (
        <div className="painel-boas-vindas" aria-labelledby="boas-vindas-titulo" role="region">
            {telaAtual === "cadastro" && (
            <div className="conteudo-boas-vindas">
                <h2 id="boas-vindas-titulo" className="painel-boas-vindas-titulo">Bem-vinda(o) de Volta!</h2>
                <p className="painel-boas-vindas-texto">Se já possui uma conta, clique abaixo para entrar</p>
                <button id="alternar-para-login" className="botao-link" type="button" onClick={() => alternarTela("login")}>
                    Acessar Conta <span className="sr-only">Ir para a tela de login</span>
                </button>
            </div>
            )}
            {telaAtual === "login" && (
            <div className="conteudo-boas-vindas">
                <h2 className="painel-boas-vindas-titulo">Novo por aqui?</h2>
                <p className="painel-boas-vindas-texto">Crie sua conta e comece a gerenciar sua empresa</p>
                <button id="alternar-para-cadastro" className="botao-link" type="button" onClick={() => alternarTela("cadastro")}>
                    Criar Conta <span className="sr-only">Ir para a tela de cadastro</span>
                </button>
            </div>
            )}
        </div>
    )
}
export default PainelBoasVindas