from fastapi import FastAPI

from api.db import init_db
from api.routes.category import router as cRouter


app = FastAPI()
app.include_router(cRouter, tags=["Category"], prefix="/category")


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}
