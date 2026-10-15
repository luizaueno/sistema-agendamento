from pydantic import BaseModel, field_validator # 🛠️ Adicionado 'field_validator' no import
from presentation.validators.nome_validator import NomeValido
from presentation.validators.cnpj_validator import CnpjValido
from presentation.validators.especialidade_validator import EspecialidadeValida
from presentation.validators.email_validator import EmailValido
from presentation.validators.cor_validator import CorValida

class ProfissionalDTO(BaseModel):
    nome: NomeValido
    cnpj: CnpjValido
    especialidade: EspecialidadeValida
    email: EmailValido
    telefone: str  # Mantemos como str para receber o dado limpo
    cor: CorValida

    # 🛠️ CORREÇÃO: O validador DEVE ficar dentro da classe e indentado corretamente
    @field_validator('telefone', mode='before')
    @classmethod
    def limpar_telefone_nulo(cls, v):
        # Se o front-end mandou null, None ou se veio a palavra literal "None", limpamos
        if v is None or str(v).strip() == "None":
            return ""
        return str(v)
