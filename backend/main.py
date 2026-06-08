from fastapi import FastAPI
import uvicorn
from domain.entities.Usuario import Usuario
from presentation.routers.cadastrorouter import rotas as cadastrorouter
from presentation.routers.loginrouter import rotas as loginrouter

app = FastAPI() # aplicacao agora pode receber requisições

app.include_router(cadastrorouter) # incluindo as rotas cadastro
app.include_router(loginrouter) # e login