from enum import Enum


class Perfil(Enum):
    ADMIN = "Admin"
    PROFISSIONAL = "Profissional"
    ADMIN_PROFISSIONAL = "Admin_Profissional"

class Usuario:
    id: int | None = None # aceita inteiro, aceita vazio e começa vazio
    nome: str
    email: str
    senha: str
    perfil: Perfil
    id_empresa: int| None = None

    def __init__(self, nome, email, senha, perfil, id=None, id_empresa=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil
        self.id_empresa = id_empresa # para saber de qual empresa é
