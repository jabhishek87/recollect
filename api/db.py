from beanie import init_beanie
import motor.motor_asyncio

# from app.server.models.product_review import ProductReview
from api.models import Category


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://user1:passwd@localhost:27017/"
    )

    await init_beanie(database=client.db_name, document_models=[Category])
