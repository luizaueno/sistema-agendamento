from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from domain.entities.Usuario import Usuario
from presentation.routers.cadastrorouter import rotas as cadastrorouter
from presentation.routers.loginrouter import rotas as loginrouter
from presentation.routers.profissionalrouter import rotas as profissionalrouter
from fastapi.middleware.cors import CORSMiddleware
from domain.exceptions.SharedExeptions import CampoObrigatorioVazio, ErroConexaobd, NomeCurto
from domain.exceptions.UsuarioExceptions import (
    UsuarioNaoEncontrado, EmailJaCadastrado, EmailInvalido,  
    SenhaInvalida
)
from domain.exceptions.EmpresaExceptions import CnpjInvalido, CnpjJaCadastrado

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,  
    allow_origins=["http://localhost:5173"],  
    allow_methods=["POST"],  
    allow_headers=["Content-Type", "Accept"]
)

# 2. Dicionário de mapeamento: associa a classe do erro ao código HTTP correto
MAPA_ERROS_HTTP = {
    CampoObrigatorioVazio: 400,
    EmailInvalido: 400,
    SenhaInvalida: 400,
    NomeCurto: 400,
    CnpjInvalido: 400,
    UsuarioNaoEncontrado: 404,
    EmailJaCadastrado: 409,
    CnpjJaCadastrado: 409,
    ErroConexaobd: 503
}


@app.exception_handler(Exception)
async def gerenciador_erros_global(request: Request, exc: Exception):
    classe_do_erro = type(exc)

    status_code = MAPA_ERROS_HTTP.get(classe_do_erro, 500)

    mensagem = str(exc) if str(exc) else classe_do_erro.__name__
    
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "erro",
            "tipo": classe_do_erro.__name__,
            "detalhe": mensagem
        }
    )

app.include_router(cadastrorouter) # incluindo as rotas cadastro
app.include_router(loginrouter) # e login 
app.include_router(profissionalrouter)
