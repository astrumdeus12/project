"Initilization of course atributes package."

from app.internal.models.course import Course
from app.internal.models.course_atributes import (
    Announcement,
    Assessment,
    Category,
    Discussion,
    Enrollment,
    Lesson,
    Module,
    Resourse,
    Rewiew,
)
from app.internal.models.user import User

__all__ = [
    "Assessment",
    "Lesson",
    "Module",
    "Category",
    "Resourse",
    "Announcement",
    "Discussion",
    "Enrollment",
    "Rewiew",
    "Course",
    "User",
]
