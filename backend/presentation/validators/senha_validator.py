from domain.exceptions import CampoObrigatorioVazio, SenhaInvalida
from typing import Annotated
from pydantic import AfterValidator

def validar_senha(v):
    v = v.strip()
    if v == "":
        raise CampoObrigatorioVazio("Campo Obrigatório não preenchido")
    if len(v) < 8:
        raise SenhaInvalida("A senha precisa de no mínimo 8 caracteres")
    if not any(char.isupper() for char in v) or not any(char.islower() for char in v):  # char in v seria cada digito, no v, a string inteira
        raise SenhaInvalida("A senha precisa ter ao menos uma letra maiúscula e outra minúscula")
    if not any(char.isdigit() for char in v) or not any( not char.isalnum() for char in v):
        raise SenhaInvalida("A senha precisa ter ao menos um número e um caractere especial")
    return v

SenhaValida = Annotated[str, AfterValidator(validar_senha)]