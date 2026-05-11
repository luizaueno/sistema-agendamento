from enum import Enum


class PerfilEnum(Enum):
    ADMIN = "Admin"
    PROFISSIONAL = "Profissional"
    ADMIN_PROFISSIONAL = "Admin_Profissional"

class Usuario:
    id: int | None = None
    nome: str
    email: str
    senha: str
    perfil: PerfilEnum

    def __init__(self, nome, email, senha, perfil, id=None, id_empresa=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil
