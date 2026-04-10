from domain.entities.Usuario import Usuario #  pasta entities, arquivo usuario, importe a classe usuario
from domain.exceptions import UsuarioNaoEncontrado, CampoObrigatorioVazio, EmailInvalido, SenhaInvalida, EmailJaCadastrado

class UsuarioService:
    def __init__(self, usuario_repository):
        self.repo = usuario_repository # salva o repository para se aplicar as regras

        
    def buscar_por_email(self, email):
        email_existente = self.repo.buscar_por_email(email) # self.repo, onde se salvou o repository, busca um email, se for igual lança um erro
        if email_existente is not None:
            raise EmailJaCadastrado("Esse email já está cadastrado") 
    
