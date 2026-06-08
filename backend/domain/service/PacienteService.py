from domain.entities.Paciente import Paciente
from domain.exceptions import CampoObrigatorioVazio, CpfInvalido, CpfJaCadastrado, TelefoneInvalido

class PacienteService:

    def __init__(self, paciente_repository):
        self.repo = paciente_repository # salva o repository para se aplicar as regras

    def cadastrar(self, nome, data_nascimento, sexo, nome_responsavel, cpf, telefone, id_empresa):

        if nome== "" or data_nascimento == "" or sexo== "" or nome_responsavel=="" or cpf=="" or telefone=="" or id_empresa is None:
            raise CampoObrigatorioVazio("Campo Obrigatório não preenchido")

        if len(cpf) < 11:
            raise CpfInvalido("O CPF inserido não tem o formato correto")
        
        self.buscar_por_cpf(cpf)
        
        if len(telefone) < 11:
            raise TelefoneInvalido("O telefone inserido não tem o formato correto")

        novo_paciente = Paciente(nome, data_nascimento, sexo, nome_responsavel, cpf, telefone, id_empresa)
        paciente_salvo = self.repo.salvar(novo_paciente)
        return (paciente_salvo)

    def buscar_por_cpf(self, cpf_valido):
        cpf = self.repo.buscar_por_cpf(cpf_valido) # self.repo, onde se salvou o repository, busca um cpf, se for igual lança um erro
        if cpf is not None:
            raise CpfJaCadastrado("Esse CPF já está cadastrado") 

    def buscar_por_responsavel(self, nome_responsavel):
        responsavel = self.repo.buscar_por_responsavel(nome_responsavel)
        return responsavel
        

