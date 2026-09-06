from datetime import datetime
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel                 # <--- Adicionado para estruturar os dados que vêm do Front-end
from domain.responses.CadastroProfissionalResponse import CadastroProfissionalResponse
from domain.service.ProfissionalService import ProfissionalService
from domain.service.UsuarioService import UsuarioService
from domain.service.EmailService import email_convite
from infra.conexao_db import criar_conexao
from presentation.dto.ProfissionalDTO import ProfissionalDTO
from repository.Convite_Repository import ConviteRepository
from repository.Profissional_Repository import ProfissionalRepository
from repository.Usuario_Repository import UsuarioRepository

rotas = APIRouter()

@rotas.post("/profissionais")
def cadastrar(dto: ProfissionalDTO):
    db_connection = criar_conexao()
    
    try:
        profissional_service = ProfissionalService(db_connection)
        
        # Se qualquer erro de validação/negócio acontecer aqui dentro, 
        # ele será lançado (raise) e o FastAPI jogará para o main.py tratar.

        response = profissional_service.cadastrar(dto)

        email_destinatario = response["email"]
        token = response["token_ativacao"]
        expira_em = response["expira_em"]

        email_convite(email_destinatario, token)
        return CadastroProfissionalResponse(convite_expira_em=expira_em)
        
    finally:
        # Garante que a conexão com o banco NUNCA fique aberta ou presa
        db_connection.close()


class ativarcontaDTO(BaseModel):
    token: str
    nova_senha: str

@rotas.post("/profissionais/ativarconta")
# rota que o front chama enviando o token e a senha
def ativar_conta(dados: ativarcontaDTO):
    db_connection = criar_conexao()

    try:
            profissional_service = ProfissionalService(db_connection)
            
            # Se qualquer erro de validação/negócio acontecer aqui dentro, 
            # ele será lançado (raise) e o FastAPI jogará para o main.py tratar.
    
            response = profissional_service.ativar_conta(token=dados.token, nova_senha=dados.nova_senha)

            return response
    
    except Exception as e:
         raise HTTPException(status_code=400, detail=str(e))
            
    finally:
        # Garante que a conexão com o banco NUNCA fique aberta ou presa
        db_connection.close()