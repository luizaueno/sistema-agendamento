from enum import Enum
from datetime import datetime

class PerfilEnum(Enum):
    ADMIN = "Admin"
    PROFISSIONAL = "Profissional"

class LoginResponse:
    def __init__(self, token, tempo_expiracao, perfil):
        self.token: str = token
        self.tempo_expiracao: datetime = tempo_expiracao
        self.perfil: PerfilEnum = perfil