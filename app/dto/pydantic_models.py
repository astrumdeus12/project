from pydantic import BaseModel
import uuid
from fastapi_users import schemas
from beanie import PydanticObjectId


class CourseSchema(BaseModel):
    name : str
    autor : str
    description : str
    category : str
    tags : list[str]

class CourseID(BaseModel):
    id : PydanticObjectId

class CourseUpdate(BaseModel):
    name : str = None
    autor : str = None
    decription : str = None
    category : str = None
    tags : list[str] = None


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass