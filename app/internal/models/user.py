from beanie import Document, Link
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase

from app.internal.models.course import Course




class User(BeanieBaseUser, Document):
    subscribe_courses : list[Link[Course]]
    


