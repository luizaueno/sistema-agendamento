from pydantic import BaseModel
from presentation.validators.email_validator import EmailValido
from presentation.validators.senha_validator import SenhaValida
from presentation.validators.nome_validator import NomeValido
from presentation.validators.cnpj_validator import CnpjValido

class CadastroDTO(BaseModel):
    nome: NomeValido
    cnpj: CnpjValido
    email: EmailValido
    senha: SenhaValida

  
    
  
 
   
 
 
