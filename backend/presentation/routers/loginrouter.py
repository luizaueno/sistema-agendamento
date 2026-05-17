from fastapi import APIRouter
from presentation.dto.LoginDTO import LoginDTO
from repository import Usuario_Repository
from domain.responses import LoginResponse
from domain.service import UsuarioService

rotas = APIRouter()


@rotas.post("/login")
def fazer_login(dto: LoginDTO):
   repo = Usuario_Repository()
   usuario1 = UsuarioService(repo)
   response =  usuario1.fazer_login(dto.email, dto.senha)
   return LoginResponse(response.token, response.tempo_expiracao, response.perfil)