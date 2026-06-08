class CadastroResponse:
    def __init__(self, nome, cnpj, email):
        self.nome: str = nome
        self.cnpj: str = cnpj
        self.email: str = email
        # Não tem senha por segurança, para não expor