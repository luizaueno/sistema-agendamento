from fastapi import APIRouter
from dto import LoginDTO
from domain.responses import LoginResponse
from domain.service import UsuarioService

rotas = APIRouter()
usuario1 = UsuarioService()

@rotas.post("/login")
def fazer_login(dto: LoginDTO):
   response =  usuario1.fazer_login(dto.email, dto.senha)
   return LoginResponse(response.token, response.tempo_expiracao, response.perfil)