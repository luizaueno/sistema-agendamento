class Empresa:
    id: int | None = None
    nome: str
    cnpj: str
    email_empresa: str
    
    def __init__(self, nome, cnpj, email_empresa, id=None):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.email_empresa = email_empresa 