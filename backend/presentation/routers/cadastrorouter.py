from fastapi import APIRouter
from dto import CadastroDTO
from domain.responses import CadastroResponse
from domain.service import EmpresaService
from repository import Empresa_Repository

rotas = APIRouter()
repo = Empresa_Repository()
empresa1 = EmpresaService(repo)

@rotas.post("/cadastrar")
def cadastrar(dto: CadastroDTO):
    response = empresa1.cadastrar(dto.nome, dto.cnpj, dto.email_empresa)
    return CadastroResponse(response.nome, response.cnpj, response.email_empresa) 