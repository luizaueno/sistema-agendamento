from datetime import datetime, timedelta, timezone
import os
import bcrypt
import jwt
from domain.entities import Usuario
from domain.exceptions.SharedExeptions import CampoObrigatorioVazio, EmailInvalido, SenhaInvalida
from domain.exceptions.UsuarioExceptions import EmailJaCadastrado, UsuarioNaoEncontrado
from domain.responses.LoginResponse import LoginResponse



class UsuarioService:
    def __init__(self, usuario_repository):
        self.repo = usuario_repository # para conectar com o repository (banco de dados) do usuario

    def buscar_por_email(self, email):
        email_existente = self.repo.buscar_por_email(email) # a conexão com o banco, vai usar a função de nome explicativo e retornar erro se já foi cadastrado
        if email_existente is not None:
            raise EmailJaCadastrado("Esse Email já está cadastrado")

    def cadastrar(self, email, senha, id_empresa, perfil):
        if email == "" or senha == "":
            raise CampoObrigatorioVazio("Campo Obrigatório não preenchido")
        if not "@" in email or not ".com" in email:
            raise EmailInvalido("Email Inválido")
        self.buscar_por_email(email)
        
        if len(senha) < 8:
            raise SenhaInvalida("Senha Inválida") 
        if not any(l.islower() for l in senha): # se não tiver qualquer minuscula
            raise SenhaInvalida("Senha Inválida")
        if not any(l.isupper() for l in senha): # se não tiver qualquer maiuscula
            raise SenhaInvalida("Senha Inválida")       
        if not any(l in "#@!" for l in senha): # se não tiver qualquer caractere especial
            raise SenhaInvalida("Senha Inválida")    

        senha_banco = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()) # traqnsforma em bytes adiciona caracteres aleatorios e junta tudo para enviar ao bd
        login = Usuario(
            email=email, 
            senha=senha_banco, 
            perfil=perfil, 
            id_empresa=id_empresa
        )
        usuario_criado = self.repo.salvar(login) # salva as informações de login com a senha 
        return usuario_criado

    def fazer_login(self, email, senha):
        email_existente = self.repo.buscar_por_email(email)
        if email_existente is None:
            raise UsuarioNaoEncontrado("Esse usuário não está cadastrado")
        senha_do_banco = email_existente['senha'] # pega a senha do banco que é um dict []

        # se foi salva como string, converte de novo para byte
        if isinstance(senha_do_banco, str): 
            senha_do_banco = senha_do_banco.encode('utf-8') 
        senha_correta = bcrypt.checkpw(senha.encode('utf-8'), senha_do_banco) # compara a salva com a digitada
        if not senha_correta:
            raise SenhaInvalida("Senha Inválida")  
        
        data_expiracao = datetime.now(timezone.utc) + timedelta(hours=8)
        payload = {
            "email": email_existente['email'],
            "exp": data_expiracao,
            "perfil": email_existente['perfil'], 
            "id_empresa": email_existente['id_empresa']
        }

        secret_key = os.getenv("secret_key")   # Pega a chave secreta do servidor escondida nas configurações do sistema (variáveis de ambiente)
        token = jwt.encode(payload, secret_key, algorithm = "HS256")  # Junta os dados (email e expiração) e tranca com a chave secreta para gerar o Token (a pulseira de acesso)
        loginResposta = LoginResponse(token, data_expiracao, email_existente['perfil'])  # Monta o pacote final com o Token, o tempo de validade e o perfil (nível de acesso) do usuário
        return loginResposta # aparece na tela