from app.dto.category_models import CategorySchema
from app.dto.course_models import PydantID
from app.internal.models.course_atributes import Category
from app.internal.repository.course_repo import NotFoundError


class CategoryRepository:
    "Repository model for Category."

    async def get_category_or_error(self, category_id: PydantID) -> Category:
        "Return course object or error."
        category = await Category.find_one(category_id)
        if not category:
            raise NotFoundError(category_id)
        return category

    async def add(self, add_category_dto: CategorySchema) -> str:
        "Add Category object."
        new_category = Category(add_category_dto.model_dump())
        new_category.insert()
        return f"Category added with ID: {new_category.id}"

    async def remove(self, category_id: PydantID) -> str:
        "Remove Category obbject by course_ID."
        course_delete = await self.get_category_or_error(course_id=category_id)
        await course_delete.delete()
        return f"Category with id {category_id} deleted."

    async def update(
        self, category_id: PydantID, update_category_dto: CategorySchema
    ) -> str:
        "Update category obbject by category_ID."
        category = await self.get_category_or_error(course_id=category_id)
        await category.update(update_category_dto.model_dump())
        await category.save()
        return f"Category updated with ID: {category_id}"

    async def check(self, category_id: PydantID) -> str:
        "Use function get category or error to get Category object."
        return await self.get_category_or_error(course_id=category_id)
