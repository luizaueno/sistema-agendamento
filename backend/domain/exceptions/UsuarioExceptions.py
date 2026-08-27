from domain.exceptions import CampoObrigatorioVazio, EmailInvalido, SenhaInvalida

class UsuarioNaoEncontrado(Exception):
    pass

class EmailJaCadastrado(Exception):
    pass