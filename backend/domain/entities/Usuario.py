from enum import Enum

class PerfilEnum(Enum):
    ADMIN = "Admin"
    PROFISSIONAL = "Profissional"

class Usuario:
    def __init__(self, nome, email, senha, is_admin, perfil, id=None, id_empresa=None):
        self.id: int = id
        self.nome: str = nome
        self.email: str = email
        self.senha: str = senha
        self.is_admin: bool = is_admin
        self.perfil: PerfilEnum = perfil
        