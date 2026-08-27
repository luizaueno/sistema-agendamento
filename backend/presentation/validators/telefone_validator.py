from domain.exceptions import CampoObrigatorioVazio, TelefoneInvalido
from typing import Annotated
from pydantic import AfterValidator

def validar_telefone(v):
   if v == "":
    raise CampoObrigatorioVazio("Campo obrigatório não preenchido")

    telefone_limpo = "".join(char for char in v if char.isdigit())

    if len(telefone_limpo) != 11:
        raise TelefoneInvalido("O celular precisa conter o DDD e ter exatamente 11 dígitos")

    if telefone_limpo[2] != "9":
        raise TelefoneInvalido("O número de celular informado é inválido (deve começar com 9)")
        
    return telefone_limpo

TelefoneValido = Annotated[str, AfterValidator(validar_telefone)]