from entities.Usuario import Usuario

class Profissional(Usuario):
    def __init__(self,nome, email, senha, perfil,  profissao, cor, id=None):
        super().__init__(id, nome, email, senha, perfil)
        self.profissao: str = profissao
        self.cor: str = cor