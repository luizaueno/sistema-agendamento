import bcrypt
import jwt
import os
from domain.entities.Usuario import Usuario #  pasta entities, arquivo usuario, importe a classe usuario
from domain.exceptions import UsuarioNaoEncontrado, CampoObrigatorioVazio, EmailInvalido, SenhaInvalida, EmailJaCadastrado
from datetime import datetime, timedelta, timezone
from domain.responses.LoginResponse import LoginResponse


class UsuarioService:
    def __init__(self, usuario_repository):
        self.repo = usuario_repository # salva o repository para se aplicar as regras

    def buscar_por_email(self, email):
        email_existente = self.repo.buscar_por_email(email) # self.repo, onde se salvou o repository, busca um email, se for igual lança um erro
        if email_existente is not None:
            raise EmailJaCadastrado("Esse Email já está cadastrado") 
    
    def cadastrar(self, nome, email, senha, id_empresa, perfil):
        if email=="" or senha=="":
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
        
        senha_banco = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        login = Usuario(
            nome=nome, 
            email=email, 
            senha=senha_banco, 
            perfil=perfil, 
            id_empresa=id_empresa
        )
        self.repo.salvar(login) # salva as informações de login com a senha 

    def fazer_login(self, email, senha):
        email_existente = self.repo.buscar_por_email(email)
        if email_existente is None:
            raise UsuarioNaoEncontrado("Esse usuário não está cadastrado")
        senha_do_banco = email_existente['senha'] #dicionario, por isso [] - pega a senha do banco

        # precisa ser byte, por isso a conversão, porque pode ter sito salva como string
        if isinstance(senha_do_banco, str): 
            senha_do_banco = senha_do_banco.encode('utf-8')

        senha_correta = bcrypt.checkpw(senha.encode('utf-8'), senha_do_banco)
        if not senha_correta:
            raise SenhaInvalida("Senha Inválida")  
        
        data_expiracao = datetime.now(timezone.utc) + timedelta(hours=8)
        payload = {
            "email": email_existente['email'],
            "exp": data_expiracao
        }

        secret_key = os.getenv("secret_key")
        token = jwt.encode(payload, secret_key, algorithm = "HS256")
        loginResposta = LoginResponse(token, data_expiracao, email_existente['perfil'])
        return loginResposta