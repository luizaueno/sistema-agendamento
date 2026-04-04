# sistema de agendamento focado em clínicas para a área da saúde
Backend em python desenvolvido para gerir o agendamento de consultas e facilitando esse administrar da empresa, garantindo maior organização dos profissionais. Utilizando como banco de dados o mysql 
# Ferramentas usadas:
- Python 3
- Mysql server
- mysql-connector-python (Biblioteca para ligar o Python ao Banco de Dados)
# Organização de pastas
/backend/infra: Configurações de conexão com o banco de dados.

/backend/repository: Scripts SQL e funções de manipulação de dados.

/backend/domain: Regras de negócio e modelos do sistema.

/database: Diagramas ER e ficheiros de backup (.sql ou .bak).
# Para o sistema rodar
Clonar o repositório: git clone [https://github.com/luizaueno/sistema-agendamento]

Instalar dependências: pip install mysql-connector-python

Configurar o Banco: "Executar o script SQL presente na pasta /database para criar as tabelas."