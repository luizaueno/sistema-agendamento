from datetime import datetime

from fastapi import APIRouter
from domain.responses.CadastroProfissionalResponse import CadastroProfissionalResponse
from domain.service.ProfissionalService import ProfissionalService
from domain.service.UsuarioService import UsuarioService
from infra.conexao_db import criar_conexao
from presentation.dto.ProfissionalDTO import ProfissionalDTO
from repository.Convite_Repository import ConviteRepository
from repository.Profissional_Repository import ProfissionalRepository
from repository.Usuario_Repository import UsuarioRepository


rotas = APIRouter()

@rotas.post("/profissionais")

def cadastrar(dto: ProfissionalDTO):
    db_connection = criar_conexao()

    profissional_service = ProfissionalService(db_connection)

    response = profissional_service.cadastrar(dto)
    profissional_criado = response["expira_em"]
    return CadastroProfissionalResponse(convite_expira_em = profissional_criado)

