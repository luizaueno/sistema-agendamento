from domain.exceptions import CampoObrigatorioVazio, NomeCurto, CnpjInvalido, EmailInvalido, SenhaInvalida
class CnpjJaCadastrado(Exception):
    pass

class LimiteAdmins(Exception):
    pass

class EmpresaNaoEncontrada(Exception):
    pass