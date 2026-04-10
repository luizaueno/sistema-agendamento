class Usuario:
    def __init__(self, nome, email, senha, perfil, id=None):
        self.id: int = id
        self.nome: str = nome
        self.email: str = email
        self.senha: str = senha
        self.perfil: str = perfil
        