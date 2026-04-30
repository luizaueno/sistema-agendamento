from fastapi import APIRouter
from dto import loginDTO, loginResponseDTO
from domain.service import UsuarioService

rotas = APIRouter()
usuario1 = UsuarioService()

@rotas.post("/login")
def fazer_login(dto: loginDTO):
   response =  usuario1.fazer_login(dto.email, dto.senha)
   return loginResponseDTO(response.token, response.tempo_expiracao, response.perfil)