class Empresa:
    id: int | None = None
    nome: str
    cnpj: str
    email: str
    senha: str
    
    def __init__(self, nome, cnpj, email,senha, id=None):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.senha = senha