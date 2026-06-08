from domain.exceptions.ExceptionCampoVazio import CampoObrigatorioVazio

class UsuarioNaoEncontrado(Exception):
    pass
class EmailInvalido(Exception):
    pass
class SenhaInvalida(Exception):
    pass
class EmailJaCadastrado(Exception):
    pass