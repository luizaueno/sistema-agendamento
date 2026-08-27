from domain.exceptions import CampoObrigatorioVazio, NomeCurto
from typing import Annotated
from pydantic import AfterValidator

def validar_nome(nome):
    nome = nome.strip()
    if nome == "":
        raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
    if len(nome) < 5:
        raise NomeCurto("O nome precisa ter no mínimo 5 caracteres")
    return nome

NomeValido = Annotated[str, AfterValidator(validar_nome)]