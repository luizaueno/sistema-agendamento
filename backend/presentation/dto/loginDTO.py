from pydantic import BaseModel

class LoginDTO(BaseModel): # basemodel garante que o dado venha do mesmo tipo como foi pedido 
    email: str
    senha: str