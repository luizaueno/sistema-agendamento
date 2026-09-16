from fastapi import APIRouter, Depends
from presentation.dto.CadastroDTO import CadastroDTO
from repository.Empresa_Repository import EmpresaRepository
from domain.service.EmpresaService import EmpresaService
from domain.responses.CadastroResponse import CadastroResponse
from repository.Usuario_Repository import UsuarioRepository
from domain.service.UsuarioService import UsuarioService

from infra.conexao_db import criar_conexao

rotas = APIRouter()

@rotas.post("/cadastro-empresa")
def cadastrar(dto: CadastroDTO, db = Depends(criar_conexao)):
    # Instancia os repositórios necessários
    repo = EmpresaRepository(db_connection=db)
    repo_usuario = UsuarioRepository(db_connection=db)
    
    # Instancia o serviço de apoio do usuário
    usuario_service = UsuarioService(repo_usuario)
    
    # Instancia o serviço principal da regra de negócio
    empresa1 = EmpresaService(repo, repo_usuario, usuario_service)
    
    # Se qualquer service lançar uma exceção mapeada, o main.py intercepta e muda o Status 500 para o correto!
    response = empresa1.cadastrar(dto)
    
    empresa_criada = response["empresa"]
    return CadastroResponse(
        nome=empresa_criada.nome, 
        cnpj=empresa_criada.cnpj, 
        email=empresa_criada.email
    )
