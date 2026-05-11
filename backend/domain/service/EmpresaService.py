from domain.entities.Empresa import Empresa #  pasta entities, arquivo Empresa, importe a classe Empresa
from domain.exceptions import EmpresaNaoEncontrada, CnpjJaCadastrado, LimiteAdmins

class EmpresaService:
    def __init__(self, empresa_repository):
        self.repo = empresa_repository # salva o repository para se aplicar as regras

    def cadastrar(self, nome, cnpj_valido, email_empresa):
        nova_empresa = Empresa(nome, cnpj_valido, email_empresa)
        empresa_salva = self.repo.salvar(nova_empresa)
        return empresa_salva
        
    def buscar_por_cnpj(self, cnpj_valido):
        empresa_existente = self.repo.buscar_por_cnpj(cnpj_valido) # self.repo, onde se salvou o repository, busca um  cnpj, se for igual lança um erro
        if empresa_existente is not None:
            raise CnpjJaCadastrado("Esse CNPJ já esta cadastrado") 
    
    def buscar_id(self, id):
        id_empresa = self.repo.buscar_id(id) # self.repo, onde se salvou o repository, busca um id, aquele em especifico
        if id_empresa is None: # se não tiver aquele id cadastrado
            raise EmpresaNaoEncontrada("Empresa não cadastrada")
        return id_empresa
    
    def adicionar_admin(self, id_profissional, total_admins):
        
        if total_admins > 3:
            raise LimiteAdmins("Limite de Administradores atingido")