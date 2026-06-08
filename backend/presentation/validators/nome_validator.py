from domain.exceptions import CampoObrigatorioVazio, NomeInvalido
from typing import Annotated
from pydantic import AfterValidator

def validar_nome(nome):
    nome = nome.strip()
    if nome == "":
        raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
    if len(nome) < 5:
        raise NomeInvalido("O nome da sua empresa precisa ser maior")
    return nome

NomeValido = Annotated[str, AfterValidator(validar_nome)]