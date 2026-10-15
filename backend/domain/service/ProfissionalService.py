import datetime, secrets, bcrypt, jwt, os
from dotenv import load_dotenv
from domain.entities.Profissional import Profissional
from domain.entities.Usuario import Usuario
from domain.entities.ConviteAtivacao import ConviteAtivacao
from domain.exceptions.EmpresaExceptions import CnpjJaCadastrado
from domain.exceptions.SharedExeptions import CampoObrigatorioVazio, ErroConexaobd
from domain.exceptions.UsuarioExceptions import EmailJaCadastrado
from infra.conexao_db import criar_conexao
from repository.Convite_Repository import ConviteRepository
from repository.Profissional_Repository import ProfissionalRepository
from repository.Usuario_Repository import UsuarioRepository

load_dotenv()

class ProfissionalService:
    JWT_SECRET = os.getenv("secret_key", "fallback_secret_key") # trazer o valor de secret para a classe 
    JWT_ALGORITHM = "HS256"
    def __init__(self, db_connection):
        self.db_connection = db_connection 

        self.repo = ProfissionalRepository(db_connection) 
        self.convite_repo = ConviteRepository(db_connection)
        self.usuario_repo = UsuarioRepository(db_connection)

    def verificar_duplicidade(self, cnpj, email, db_connection):
        cnpj_existente = self.repo.buscar_por_cnpj(cnpj, db_connection)
        if cnpj_existente is not None:
            raise CnpjJaCadastrado("Este CNPJ já está cadastrado no sistema")
        
        email_existente = self.usuario_repo.buscar_por_email(email, db_connection)
        if email_existente is not None:
            raise EmailJaCadastrado("Este e-mail já está cadastrado no sistema")

    def cadastrar(self, dto, id_empresa=1):
        campos = [
            str(dto.nome), 
            str(dto.cnpj), 
            str(dto.especialidade), 
            str(dto.telefone), 
            str(dto.email), 
            str(dto.cor)
        ]
        if not all(campo.strip() for campo in campos):
            raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
        

        if self.db_connection is None:
            raise ErroConexaobd("Não foi possível estabelecer conexão com o banco de dados")

        try:
            self.verificar_duplicidade(str(dto.cnpj), str(dto.email), self.db_connection)

      
            usuario_dados = Usuario(
                nome=str(dto.nome),
                senha= "",
                email=str(dto.email),
                perfil="profissional",
                id_empresa=id_empresa
            )
      
            id_usuario = self.usuario_repo.salvar(usuario_dados, self.db_connection)

            profissional_dados = Profissional(
                nome=str(dto.nome),
                cnpj=str(dto.cnpj),
                especialidade=str(dto.especialidade),
                telefone=str(dto.telefone),
                cor=str(dto.cor),
                id_usuario=id_usuario,
                id_empresa=id_empresa
            )
            self.repo.salvar(profissional_dados, self.db_connection)

            
            criado_em = datetime.datetime.now(datetime.timezone.utc)
            expira_em = criado_em + datetime.timedelta(days=3)

            payload = {
                "sub": str(id_usuario), # padrao jwt(uma string criptografada e segura) para id
                "email": str(dto.email), 
                "action": "invite_activation", # diz para que serve esse token, é o token do convite
                "exp": int(expira_em.timestamp()) # para não deixar passar o limite de tempo (3 dias)
            }
            
            token_jwt = jwt.encode(payload, self.JWT_SECRET, algorithm=self.JWT_ALGORITHM)

            convite = ConviteAtivacao(
                token=token_jwt,
                criado_em=criado_em,
                expira_em=expira_em,
                utilizado=False,
                id_usuario=id_usuario
            )
            self.convite_repo.salvar(convite, self.db_connection)
            
            self.db_connection.commit()

            return {
                "email": str(dto.email),
                "token_ativacao": token_jwt,
                "expira_em": expira_em
            }
        

        except Exception:
            self.db_connection.rollback()
            raise 

    def listar(self, id_empresa=1):
        if self.db_connection is None:
            raise ErroConexaobd("Não foi possível estabelecer conexão com o banco de dados")
            
        try:
            # 1. Busca os profissionais (executa o método do repositório modificado)
            if hasattr(self.repo, 'listar_por_empresa'):
                profissionais = self.repo.listar_por_empresa(id_empresa, self.db_connection)
            elif hasattr(self.repo, 'buscar_todos'):
                profissionais = self.repo.buscar_todos(self.db_connection)
            else:
                profissionais = self.repo.listar(id_empresa, self.db_connection)

            if profissionais is None:
                profissionais = []

            lista_retorno = []
            for p in profissionais:
                # 🛠️ CORREÇÃO: Como 'p' é um dicionário (dictionary=True),
                # acessamos os valores usando p.get('chave', 'valor_padrao')
                lista_retorno.append({
                    "id": p.get('id', ''),
                    "nome": p.get('nome', ''),
                    "cnpj": p.get('cnpj', ''),
                    "especialidade": p.get('especialidade', ''),
                    "email": p.get('email', ''),
                    "telefone": p.get('telefone', ''),
                    "cor": p.get('cor', '#E3E7ED'),
                    "status": p.get('status', 'Conta ativa') 
                })
                
            return lista_retorno
        except Exception as e:
            print("\n❌ ERRO DETALHADO NO SERVICE PYTHON:", str(e), "\n")
            raise Exception(f"Erro interno no repositório de profissionais: {str(e)}")
