from pydantic import BaseModel
from presentation.validators.nome_validator import NomeValido
from presentation.validators.cnpj_validator import CnpjValido
from presentation.validators.especialidade_validator import EspecialidadeValida
from presentation.validators.email_validator import EmailValido
from presentation.validators.telefone_validator import TelefoneValido
from presentation.validators.cor_validator import CorValida

class ProfissionalDTO(BaseModel):
    nome: NomeValido
    cnpj: CnpjValido
    especialidade: EspecialidadeValida
    email: EmailValido
    telefone: TelefoneValido
    cor: CorValida
