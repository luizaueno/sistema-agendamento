class Empresa:
    def __init__(self, nome, cnpj, max_profissionais, id = None):
        self.id: int = id
        self.nome: str = nome
        self.cnpj: str = cnpj
        self.max_profissionais: int = max_profissionais
        