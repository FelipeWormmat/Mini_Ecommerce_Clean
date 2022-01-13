from fastapi import FastAPI
from src.presentation.fastapi.routes.router import router

def get_app():
  app = FastAPI()

  app.include_router(router)

  return app