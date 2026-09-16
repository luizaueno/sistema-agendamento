from fastapi import APIRouter, Depends
from presentation.dto.LoginDTO import LoginDTO
from repository.Usuario_Repository import UsuarioRepository
from domain.responses import LoginResponse
from domain.service.UsuarioService import UsuarioService

from infra.conexao_db import criar_conexao

rotas = APIRouter()

@rotas.post("/login")
def fazer_login(dto: LoginDTO, db = Depends(criar_conexao)):
   repo = UsuarioRepository(db_connection=db)
   usuario1 = UsuarioService(repo)
   response = usuario1.fazer_login(dto.email, dto.senha)
   
   return response
