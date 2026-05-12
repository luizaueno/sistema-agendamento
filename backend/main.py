from fastapi import FastAPI
import uvicorn
from domain.entities.Usuario import Usuario
from presentation.routers import cadastrorouter

app = FastAPI() # aplicacao agora pode receber requisições

app.include_router(cadastrorouter)