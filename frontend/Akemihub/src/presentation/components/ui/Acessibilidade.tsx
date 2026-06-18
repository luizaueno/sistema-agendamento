import './acessibilidade.css';

function Acessibilidade() {
    return (
        <div role="navigation" aria-label="acessibilidade">
            <a href="#topo-ancora" className="skip-link" accessKey="1">Ir para o topo [Alt + 1]</a>
            <a href="#menu-ancora" className="skip-link" accessKey="2">Ir para o menu de navegação [Alt + 2]</a>
            <a href="#conteudo-ancora" className="skip-link" accessKey="3">Ir para o conteúdo principal [Alt + 3]</a>
            <a href="#rodape-ancora" className="skip-link" accessKey="4">Ir para o rodapé [Alt + 4]</a>
      </div>
    )
}

export default Acessibilidade