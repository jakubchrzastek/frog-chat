from fastapi import FastAPI

from frog_chat.api.router import router

app = FastAPI(title="FrogChat", version="1.0.0")

app.include_router(router)