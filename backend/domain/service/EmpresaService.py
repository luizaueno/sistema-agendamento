from domain.entities.Empresa import Empresa #  pasta entities, arquivo Empresa, importe a classe Empresa
from domain.exceptions import EmpresaNaoEncontrada, CnpjJaCadastrado, LimiteAdmins
from presentation.dto import CadastroDTO
from utils import SenhaUtil
from domain.service import UsuarioService


class EmpresaService:
    def __init__(self, empresa_repository, usuario_repository, usuario_service):
        self.repo_empresa = empresa_repository # salva o repository para se aplicar as regras
        self.repo_usuario = usuario_repository
        self.serv_usuario = usuario_service

    def cadastrar(self, dados: CadastroDTO): # tudo de CadastroDTO em uma variavel
        """
        Coordena o fluxo de criação de uma nova empresa.
        """
        # Validação de Regra de Negócio: O CNPJ já existe?
        # Chamamos o método que você criou abaixo. Se existir, ele lança erro e para aqui.
        self.buscar_por_cnpj(dados.cnpj)

        # faz o hash da senha enviada no cadastro
        hash_gerado = SenhaUtil.SenhaUtil.hash(dados.senha)

        # Transformação: Transforma o DTO em um objeto da classe Empresa
        nova_empresa = Empresa (
            nome = dados.nome, 
            cnpj = dados.cnpj, 
            email = dados.email,
            senha = hash_gerado
        )

        # Persistência: Manda o repositório salvar no banco
        id_da_empresa = self.repo_empresa.salvar(nova_empresa)
        
        usuario_salvo = self.serv_usuario.cadastrar(dados.nome, dados.email, dados.senha, id_da_empresa, "admin")

        return {
            "empresa": nova_empresa,
            "usuario": usuario_salvo
        }

    def buscar_por_cnpj(self, cnpj_valido):
        """
        Verifica se um CNPJ já está no sistema para evitar duplicidade.
        """
        empresa_existente = self.repo_empresa.buscar_por_cnpj(cnpj_valido)
        
        if empresa_existente is not None:
            raise CnpjJaCadastrado("Esse CNPJ já está cadastrado")
        # Se for None, a função termina em silêncio e o 'cadastrar' continua.

    def buscar_id(self, id):
        """
        Busca uma empresa específica pelo ID para exibição ou edição.
        """
        id_empresa = self.repo_empresa.buscar_id(id)
        
        if id_empresa is None:
            raise EmpresaNaoEncontrada("Empresa não cadastrada")
            
        return id_empresa
    
    def adicionar_admin(self, id_profissional, total_admins):
        
        if total_admins > 3:
            raise LimiteAdmins("Limite de Administradores atingido")