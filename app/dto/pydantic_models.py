import uuid

from beanie import PydanticObjectId
from fastapi_users import schemas
from pydantic import BaseModel


class CourseSchema(BaseModel):
    "Pydantic schema for course."

    name: str
    autor: str
    description: str
    category: str
    tags: list[str]


class CourseID(BaseModel):
    "Validation of id == Pydantic object id."

    id: PydanticObjectId


class CourseUpdate(BaseModel):
    "Schema for updating  course data."

    name: str = None
    autor: str = None
    decription: str = None
    category: str = None
    tags: list[str] = None


class UserRead(schemas.BaseUser[uuid.UUID]):
    "Default fastapi_users schema."


class UserCreate(schemas.BaseUserCreate):
    "Default fastapi_users schema."


class UserUpdate(schemas.BaseUserUpdate):
    "Default fastapi_users schema."
