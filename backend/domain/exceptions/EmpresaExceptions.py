from domain.exceptions.ExceptionCampoVazio import ExceptionCampoObrigatorioVazio

class NomeInvalido(Exception):
    pass

class CnpjInvalido(Exception):
    pass

class CnpjJaCadastrado(Exception):
    pass

class LimiteAdmins(Exception):
    pass

class EmpresaNaoEncontrada(Exception):
    pass