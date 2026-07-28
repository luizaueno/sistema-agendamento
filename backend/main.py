from fastapi import FastAPI
import uvicorn
from domain.entities.Usuario import Usuario
from presentation.routers.cadastrorouter import rotas as cadastrorouter
from presentation.routers.loginrouter import rotas as loginrouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() # aplicacao agora pode receber requisições
app.add_middleware(CORSMiddleware,  allow_origins =["http://localhost:5173"],  allow_methods = ["POST"],  allow_headers = ["Content-Type", "Accept"])
app.include_router(cadastrorouter) # incluindo as rotas cadastro
app.include_router(loginrouter) # e login 