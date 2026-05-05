from pydantic import BaseModel

class Empresa(BaseModel):
    def __init__(self, nome, cnpj, email_empresa, id = None):
        self.id: int = id
        self.nome: str = nome
        self.cnpj: str = cnpj
        self.email_empresa: str = email_empresa       