from pydantic import BaseModel
from presentation.validators.email_validator import EmailValido
from presentation.validators.senha_validator import SenhaValida



class LoginDTO(BaseModel): # basemodel garante que o dado venha do mesmo tipo como foi pedido 
    email: EmailValido
    senha: SenhaValida



