from pydantic import BaseModel

class CadastroDTO(BaseModel):
    nome: str
    cnpj: str
    email_empresa: str