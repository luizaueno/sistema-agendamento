from datetime import date
from enum import Enum

class SexoEnum(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Paciente:
    def __init__(self, nome, data_nascimento, sexo, nome_responsavel, cpf, telefone, id_empresa, id=None):
        self.id: int = id
        self.nome: str = nome
        self.data_nascimento: date = data_nascimento
        self.sexo: SexoEnum = sexo
        self.nome_responsavel: str = nome_responsavel
        self.cpf: str = cpf
        self.telefone: str = telefone
        self.id_empresa: int = id_empresa