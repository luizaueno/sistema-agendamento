from pydantic import BaseModel

class CadastroDTO(BaseModel):
    nome: str
    cnpj: str
    max_profissionais: int
    total_admins: int