class Profissional:
    def __init__(self, nome, cnpj, especialidade, telefone, cor, id=None, id_empresa=None, id_usuario=None):
        self.id: int = id
        self.id_usuario: int = id_usuario
        self.id_empresa: int = id_empresa
        self.nome: str = nome
        self.cnpj: str = cnpj
        self.especialidade: str = especialidade
        self.telefone: str = telefone
        self.cor: str = cor 