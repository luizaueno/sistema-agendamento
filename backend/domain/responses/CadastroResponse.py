class CadastroResponse:
    def __init__(self, nome, cnpj, email_empresa):
        self.nome: str = nome
        self.cnpj: str = cnpj
        self.email_empresa: str = email_empresa