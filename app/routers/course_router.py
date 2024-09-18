from fastapi import APIRouter

from app.dto.course_models import CourseID, CourseSchema
from app.internal.models.course import Course
from app.internal.repository.course_repo import CourseRepository

router = APIRouter(prefix="course")


router.post()


async def add_course(course: CourseSchema) -> str:
    "Router for adding course object."
    return await CourseRepository.add(add_course_dto=course)


router.get()


async def read_one_course(
    course_id: CourseID,
) -> Course:  # i'll add multiple select later
    "."
    return await CourseRepository.check(course_id=course_id)


router.put()


async def update_course(course_id: CourseID, new_course: CourseSchema) -> str:
    "."
    return await CourseRepository.update(
        course_id=course_id, update_course_dto=new_course
    )


router.delete()


async def remove_course(course_id: CourseID) -> str:
    "."
    return await CourseRepository.remove(course_id=course_id)
