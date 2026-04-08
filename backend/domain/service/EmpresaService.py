from entities import Empresa
from exceptions import EmpresaNaoEncontrada, CampoObrigatorioVazio, NomeInvalido, CnpjInvalido, CnpjJaCadastrado

class EmpresaService:
    def __init__(self, empresa_repository):
        self.repo = empresa_repository # salva o repository para se aplicar as regras

    def cadastrar(self, nome, cnpj, max_profissionais, total_admins, id = None):

        if nome== "" or max_profissionais== "" or total_admins== "":
            raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
        elif len(nome) <= 5:
            raise NomeInvalido("O nome da sua empresa precisa ter mais de 5 caracteres")
        elif len(cnpj) < 14:
            raise CnpjInvalido("O CNPJ inserido não tem o formato XX.XXX.XXX/0001-YY")
        self.buscar_cnpj(cnpj)

        nova_empresa = Empresa(nome, cnpj, max_profissionais, total_admins, id = None)
        empresa_salva = self.repo.salvar(nova_empresa)
        return empresa_salva
        
    def buscar_cnpj(self, cnpj):
        cnpj = self.repo.empresa_existente(cnpj) # self.repo, onde se salvou o repository, busca um  cnpj, se for igual lança um erro
        if cnpj != None:
            raise CnpjJaCadastrado("Esse CNPJ já esta cadastrado") 
    
    def buscar_id(self, id):
        id_empresa = self.repo.buscar_id(id) # self.repo, onde se salvou o repository, busca um id, aquele em especifico
        if id_empresa is None: # se não tiver aquele id cadastrado
            raise EmpresaNaoEncontrada("Empresa não cadastrada")
        return id_empresa