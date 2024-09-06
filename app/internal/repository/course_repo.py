from app.dto.pydantic_models import CourseID, CourseSchema
from app.internal.models.course import Course

class NotFoundError(Exception):
    pass


class CourseRepository:
    async def get_course_or_error(self, course_id: CourseID) -> Course:
        course = await Course.find_one(course_id)
        if not course:
            raise NotFoundError(f"Course with id {course_id} not found in the database.")
        else:
            return course


    async def add(self, add_course_dto : CourseSchema):
        new_course = Course(add_course_dto.model_dump())
        new_course.insert()
        return f'Course added with ID: {new_course.id}'


    async def remove(self, course_id : CourseID):
        course_delete = await self.get_course_or_error(course_id=course_id)
        await course_delete.delete()
        return f"Course with id {course_id} deleted."
        

    async def update(self, course_id : CourseID, update_course_dto : CourseSchema):
        course = await self.get_course_or_error(course_id=course_id)
        await course.update(update_course_dto.model_dump())
        await course.save()
        return f'Course updated with ID: {course_id}'
        

    async def check(self, course_id : CourseID):
       return await self.get_course_or_error(course_id=course_id)