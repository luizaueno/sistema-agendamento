from domain.exceptions.SharedExeptions import CampoObrigatorioVazio, CorInvalida
from typing import Annotated
from pydantic import AfterValidator

def validar_cor(v):
    if v == "":
        raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
    cor_limpa = v.strip()
    if cor_limpa[0]!= "#":
        raise CorInvalida("O formato da cor está incorreto")
    if len(cor_limpa) != 7 and len(cor_limpa) != 9:
        raise CorInvalida("A cor precisa ter de 7 a 9 caracteres")

CorValida = Annotated[str, AfterValidator(validar_cor)]