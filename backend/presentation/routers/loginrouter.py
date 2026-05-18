from fastapi import APIRouter
from presentation.dto.LoginDTO import LoginDTO
from repository.Usuario_Repository import UsuarioRepository
from domain.responses import LoginResponse
from domain.service.UsuarioService import UsuarioService

rotas = APIRouter()


@rotas.post("/login")
def fazer_login(dto: LoginDTO):
   repo = UsuarioRepository()
   usuario1 = UsuarioService(repo)
   response =  usuario1.fazer_login(dto.email, dto.senha)
   return response