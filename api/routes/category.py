from beanie import PydanticObjectId
from fastapi import APIRouter
from typing import List

from api.models import Category
from api.custom_exceptions import NotFoundError

router = APIRouter()


@router.get("/", response_description="Get All Categories")
async def get_all_categories() -> List[Category]:
    categories = await Category.find_all().to_list()
    return categories


@router.post("/", response_description="Add Category to DB")
async def add_category(category: Category) -> dict:
    await category.create()
    return {"message": "Category added successfully"}


@router.get("/{id}", response_description="Get Category")
async def get_category(id: PydanticObjectId) -> Category:
    category = await Category.get(id)

    if not category:
        raise NotFoundError()

    return category


@router.put("/{id}", response_description="Update category")
async def update_category(id: PydanticObjectId, req: Category) -> Category:
    category = await Category.get(id)
    if not category:
        raise NotFoundError()

    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    await category.update(update_query)
    return category


@router.delete("/{id}", response_description="Delete Category")
async def delete_category(id: PydanticObjectId) -> dict:
    record = await Category.get(id)

    if not record:
        raise NotFoundError()

    await record.delete()
    return {
        "message": "Record deleted successfully"
    }
