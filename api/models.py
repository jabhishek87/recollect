from datetime import datetime

from beanie import Document


class Category(Document):
    name: str
    description: str
    rdate: datetime = datetime.now()

    class Settings:
        name = "category"

    class Config:
        schema_extra = {
            "example": {
                "name": "Name",
                "description": "Description",
                "rdate": datetime.now()
            }
        }

# class UpdateCategory(BaseModel):
#     name: Optional[str]
#     description: Optional[str]
#     date: Optional[datetime]

#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Name",
#                 "description": "Description",
#                 "rdate": datetime.now()
#             }
#         }
