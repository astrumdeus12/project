#!/usr/bin/env python3
from typing import Literal

from beanie import Document, Link

from app.internal.models.course_atributes import Category, Resourse


class Course(Document):
    "The Main ODM cass of app."

    title: str
    slug: str
    description: str
    status: Literal["draft", "published", "archived"]
    tags: list[str]
    level: Literal["beginner", "intermediate", "advanced", "all_levels"]
    prerequisites: list[str]
    larning_info: list[str]
    price: str  # after getting data make it decimal()
    discount_price: str
    language: str
    category: Link[Category]
    subcategories: list[Link[Category]]
    resourse: Link[Resourse]
    autor: str
    instructor_id: str  # maybe integer?
    url: str  # format as url

    class Settings:
        "Set name for Documents of Course."

        name = "courses"
