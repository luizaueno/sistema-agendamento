class Profissional:
    def __init__(self, profissao, cor, id=None, id_empresa=None, id_usuario=None):
        self.id: int = id
        self.id_usuario: int = id_usuario
        self.id_empresa: int = id_empresa
        self.profissao: str = profissao
        self.cor: str = cor