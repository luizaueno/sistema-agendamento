from datetime import datetime
from pydantic import BaseModel

class CadastroProfissionalResponse(BaseModel):
    convite_expira_em: datetime
