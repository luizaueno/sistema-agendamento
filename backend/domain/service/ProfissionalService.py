import datetime
import secrets
import bcrypt

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


class ProfissionalService:
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

            token = secrets.token_urlsafe(32)
            criado_em = datetime.datetime.now()
            expira_em = criado_em + datetime.timedelta(days=3)
            
            convite = ConviteAtivacao(
                token=token,
                criado_em=criado_em,
                expira_em=expira_em,
                utilizado=False,
                id_usuario=id_usuario
            )
            self.convite_repo.salvar(convite, self.db_connection)
            
            self.db_connection.commit()

            return {
                "token_ativacao": token,
                "expira_em": expira_em
            }

        except Exception:
            self.db_connection.rollback()
            raise 

        finally:
            self.db_connection.close()
