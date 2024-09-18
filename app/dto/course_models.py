from beanie import PydanticObjectId
from pydantic import BaseModel


class CourseSchema(BaseModel):
    "Pydantic schema for course."

    title: str
    slug: str
    description: str
    status: str
    tags: list[str]
    level: str
    prerequisites: list[str]
    larning_info: list[str]
    price: str
    discount_price: str
    language: str
    category: str
    subcategories: str
    resourse: str
    autor: str
    instructor_id: str  # maybe integer?
    url: str  # format as url


class PydantID(BaseModel):
    "Validation of id == Pydantic object id."

    id: PydanticObjectId


class CourseUpdate(BaseModel):
    "Schema for updating  course data."

    name: str = None
    autor: str = None
    decription: str = None
    category: str = None
    tags: list[str] = None
