"Initilization of course atributes package."

from app.internal.repository.course_repo import CourseRepository, NotFoundError

__all__ = ["NotFoundError", "CourseRepository"]
