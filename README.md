Sistema de Agendamento focado em clínicas para a área da saúde

Sistema para gerir o agendamento de consultas e facilitar a administração da empresa, garantindo maior organização dos profissionais. O backend expõe uma API REST (FastAPI) consumida por um frontend em React.

Ferramentas usadas

Backend


Python 3
FastAPI (camada de API REST)
MySQL Server
mysql-connector-python (biblioteca para ligar o Python ao banco de dados)


Frontend


React
TypeScript
Vite
CSS


Organização de pastas

Backend

main.py: Arquivo principal, onde a aplicação FastAPI é criada e as rotas são incluídas.
/infra: Configurações de conexão com o banco de dados.
/repository: Scripts SQL e funções de manipulação de dados.
/domain/entities: Modelos do sistema (ex: Usuario).
/presentation/routers: Rotas e endpoints FastAPI (ex: cadastrorouter, loginrouter).
/database: Diagramas ER e ficheiros de backup (.sql ou .bak).

Frontend

src/
└── presentation/
    └── components/
        ├── auth/         (Cadastro, Login, Boas-vindas)
        ├── ui/           (Componentes compartilhados: Acessibilidade, Header, Nav, Footer)
        ├── paciente/     (Telas/componentes do paciente)
        ├── profissional/ (Telas/componentes do profissional)
        ├── admin/        (Telas de administração)
        └── agenda/       (Tela principal)
└── app.tsx (arquivo principal, que comanda todos os outros)

Para o sistema rodar

Backend

Clonar o repositório: git clone https://github.com/luizaueno/sistema-agendamento
Instalar dependências: pip install mysql-connector-python fastapi uvicorn
Configurar o banco: executar o script SQL presente na pasta /database para criar as tabelas.
Rodar a API: na raiz do projeto, executar uvicorn main:app --reload


Frontend

Acessar a pasta do frontend.
Instalar dependências: npm install
Rodar em modo de desenvolvimento: npm run dev
