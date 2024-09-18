from pydantic import BaseModel


class CategorySchema(BaseModel):
    "."

    name: str
    slug: str
    description: str
