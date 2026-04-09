from domain.entities.Empresa import Empresa #  pasta entities, arquivo Empresa, importe a classe Empresa
from domain.exceptions import EmpresaNaoEncontrada, CampoObrigatorioVazio, NomeInvalido, CnpjInvalido, CnpjJaCadastrado

class EmpresaService:
    def __init__(self, empresa_repository):
        self.repo = empresa_repository # salva o repository para se aplicar as regras

    def cadastrar(self, nome, cnpj, max_profissionais):

        if nome== "" or max_profissionais <= 0 or cnpj== "":
            raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
        elif len(nome) <= 5:
            raise NomeInvalido("O nome da sua empresa precisa ter mais de 5 caracteres")
        
        cnpj_valido= cnpj.replace(".", "")
        cnpj_valido = cnpj_valido.replace("/", "")
        cnpj_valido = cnpj_valido.replace( "-", "")

        if len(cnpj_valido) < 14:
            raise CnpjInvalido("O CNPJ inserido não tem o tamanho correto")
        self.buscar_por_cnpj(cnpj_valido)

        nova_empresa = Empresa(nome, cnpj_valido, max_profissionais)
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