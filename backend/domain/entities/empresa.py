from pydantic import BaseModel

class Empresa(BaseModel):
    def __init__(self, nome, cnpj, max_profissionais, total_admins, id = None):
        self.id: int = id
        self.nome: str = nome
        self.cnpj: str = cnpj
        self.max_profissionais: int = max_profissionais
        self.total_admins: int = total_admins 
        