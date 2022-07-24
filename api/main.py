from fastapi import FastAPI
from fastapiwee import AutoFastAPIViewSet

from api.models import CategoryModel


app = FastAPI()
AutoFastAPIViewSet(CategoryModel, app)


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "FastAPIwee powered app!"}
