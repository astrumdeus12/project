from fastapi import APIRouter

from app.dto.category_models import CategorySchema
from app.dto.course_models import PydantID
from app.internal.repository.category_repo import CategoryRepository

category_router = APIRouter(prefix="category")

category_router.get()


async def read_category(category_id: PydantID) -> str:
    "Get category obj by id."
    return await CategoryRepository.check(category_id=category_id)


category_router.post()


async def create_category(category: CategorySchema) -> str:
    "Create new category obj."
    return await CategoryRepository.add(add_category_dto=category)


category_router.delete()


async def remove_category(category_id: PydantID) -> str:
    "Delete Category obj by id."
    return await CategoryRepository.remove(category_id=category_id)


category_router.put()


async def update_category(category_id: PydantID, new_category: CategorySchema) -> str:
    "Update ctaegory obj."
    return await CategoryRepository.update(
        category_id=category_id, update_category_dto=new_category
    )
