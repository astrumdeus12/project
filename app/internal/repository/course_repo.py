from app.dto.pydantic_models import CourseID, CourseSchema
from app.internal.models.course import Course


class NotFoundError(Exception):
    "Exception class."

    def __init__(self, course_id: CourseID) -> None:
        "Return error message."
        super().__init__(f"Course with id {course_id} not found in the database.")


class CourseRepository:
    "Repository model for Course."

    async def get_course_or_error(self, course_id: CourseID) -> Course:
        "Return course object."
        course = await Course.find_one(course_id)
        if not course:
            raise NotFoundError(course_id)
        return course

    async def add(self, add_course_dto: CourseSchema) -> str:
        "Add Course object."
        new_course = Course(add_course_dto.model_dump())
        new_course.insert()
        return f"Course added with ID: {new_course.id}"

    async def remove(self, course_id: CourseID) -> str:
        "Remove Course obbject by course_ID."
        course_delete = await self.get_course_or_error(course_id=course_id)
        await course_delete.delete()
        return f"Course with id {course_id} deleted."

    async def update(self, course_id: CourseID, update_course_dto: CourseSchema) -> str:
        "Update Course obbject by course_ID."
        course = await self.get_course_or_error(course_id=course_id)
        await course.update(update_course_dto.model_dump())
        await course.save()
        return f"Course updated with ID: {course_id}"

    async def check(self, course_id: CourseID) -> str:
        "Use function get course or error to get course object."
        return await self.get_course_or_error(course_id=course_id)
