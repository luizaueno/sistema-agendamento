import datetime

class ConviteAtivacao:
    def __init__(self, token, criado_em, expira_em, utilizado, id=None, id_usuario=None):
        self.id: int = id
        self.id_usuario: int = id_usuario        
        self.token: str = token
        self.criado_em: datetime = criado_em
        self.expira_em: datetime = expira_em
        self.utilizado: bool = utilizado