from domain.exceptions import CampoObrigatorioVazio, CnpjInvalido 
from utils.CnpjUtil import limpar_cnpj
from typing import Annotated
from pydantic import AfterValidator

def validar_cnpj(v, mode="before"):
    if not isinstance(v, str):
        raise CnpjInvalido("Formato do cnpj incorreto")
    cnpj_limpo = limpar_cnpj(v)
    if cnpj_limpo == "":
        raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
    if len(cnpj_limpo) != 14:
        raise CnpjInvalido("O tamanho do CNPJ está incorreto")
    return cnpj_limpo

CnpjValido = Annotated[str, AfterValidator(validar_cnpj)]