from domain.exceptions import CampoObrigatorioVazio, EmailInvalido
from typing import Annotated
from pydantic import AfterValidator

def validar_email(v): # o v é o valor bruto, recebido no frontend
    v = v.strip().lower()
    
    if v == "":
        raise CampoObrigatorioVazio("Campo Obrigatório não preenchido")
    
    email = v.split("@")
    if len(email) != 2 or "." not in email[1]:
        raise EmailInvalido("O formato do email está incorreto")
    if len(email[0]) < 6:
        raise EmailInvalido("O formato do email está incorreto")
    if not email[0][0].isalpha():
            raise EmailInvalido("Email deve começar com letra")
    
    return v

EmailValido = Annotated[str, AfterValidator(validar_email)]