import bcrypt
from domain.entities.Profissional import Profissional #  pasta entities, arquivo profissional, importe a classe profissional
from domain.exceptions.UsuarioExceptions import UsuarioNaoEncontrado, CampoObrigatorioVazio, EmailInvalido, SenhaInvalida, EmailJaCadastrado

class ProfissionalService:
    def __init__(self, profissional_repository):
        self.repo = profissional_repository # salva o repository para se aplicar as regras

    def buscar_por_email(self, email):
        email_existente = self.repo.buscar_por_email(email) # self.repo, onde se salvou o repository, busca um email, se for igual lança um erro
        if email_existente is not None:
            raise EmailJaCadastrado("Esse Email já está cadastrado") 
    
    def cadastrar(self, nome, email, senha, perfil, profissao, cor, id=None):
        if nome=="" or perfil=="" or profissao=="" or cor=="":
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
        login = Profissional(nome, email, senha_banco, perfil, profissao, cor)
        self.repo.salvar(login) # salva as informações de login com a senha 

        