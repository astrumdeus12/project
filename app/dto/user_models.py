import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    "Default fastapi_users schema."

    pass  # noqa: PIE790


class UserCreate(schemas.BaseUserCreate):
    "Default fastapi_users schema."

    pass  # noqa: PIE790


class UserUpdate(schemas.BaseUserUpdate):
    "Default fastapi_users schema."

    pass  # noqa: PIE790
