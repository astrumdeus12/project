#!/usr/bin/env python3
from typing import Literal

from beanie import Document, Link
from fastapi_users.db import BeanieBaseUser

from app.internal.models.course import Course


class User(BeanieBaseUser, Document):
    "Main User ODM."

    first_name: str
    second_name: str
    subscribe_courses: list[Link[Course]]
    course_progress: str
    role: Literal["user", "admin"]
