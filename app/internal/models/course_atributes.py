from typing import Literal

from beanie import Document, Link


class Assessment(Document):
    "Assessment ODM class."

    question: str
    submission: str


class Lesson(Document):
    "Lesson ODM class."

    name: str
    content: str  # conten block maybe list idk?  create model
    asessment: list[Link[Assessment]]


class Module(Document):
    "Module class."

    lessons: list[Link[Lesson]]


class Category(Document):
    "Category class."

    name: str
    slug: str
    description: str


class Resourse(Document):
    "Resourse ODM class."

    title: str
    description: str
    type: Literal[""]  # add variants
    url: str  # =url format


class Announcement(Document):
    "Announcement ODM class."

    title: str
    content: str


class Discussion(Document):
    "Discussion ODM class."

    conten: str


class Enrollment(Document):
    "Enrollment class."

    enrolled_date: str  # datetime.date
    paid: int  # decimal
    completion_percentage: int  # %


class Rewiew(Document):
    "Rewiew ODM class."

    rating: int
    content: str


# class Certificate(Document):
#     'Resourse class.'

#     pass
