from fastapi import APIRouter
from presentation.dto.CadastroDTO import CadastroDTO
from repository.Empresa_Repository import EmpresaRepository
from domain.service.EmpresaService import EmpresaService
from domain.responses.CadastroResponse import CadastroResponse
from repository.Usuario_Repository import UsuarioRepository
from domain.service.UsuarioService import UsuarioService

rotas = APIRouter()


@rotas.post("/cadastro-empresa")
def cadastrar(dto: CadastroDTO):
    # 1. Criamos os dois repositórios (Empresa e Usuário)
    repo = EmpresaRepository()
    repo_usuario = UsuarioRepository()
    
    # 2. Criamos o service do usuário
    usuario_service = UsuarioService(repo_usuario)
    
    # 3. Agora passamos tudo o que a EmpresaService precisa
    empresa1 = EmpresaService(repo, repo_usuario, usuario_service)
    
    response = empresa1.cadastrar(dto)
    empresa_criada = response["empresa"]
    return CadastroResponse(
        nome=empresa_criada.nome, 
        cnpj=empresa_criada.cnpj, 
        email=empresa_criada.email
    ) 
