from domain.exceptions import CampoObrigatorioVazio, EspecialidadeInvalida
from typing import Annotated
from pydantic import AfterValidator

def validar_especialidade(v):
    v = v.title().strip()
    
    if v == "":
        raise CampoObrigatorioVazio("Campo obrigatório não preenchido")
        
    if len(v) < 5:
        raise EspecialidadeInvalida("A especialidade informada é muito curta")
        
    return v

EspecialidadeValida = Annotated[str, AfterValidator(validar_especialidade)]
