import uuid
from collections.abc import AsyncGenerator

import motor.motor_asyncio
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users_db_beanie import BeanieUserDatabase

from app.config import APP_SETINGS
from app.internal.models.user import User
from app.internal.service.user_service import get_user_manager

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    "Return jwt token."
    return JWTStrategy(secret=APP_SETINGS.SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)


client = motor.motor_asyncio.AsyncIOMotorClient(
    APP_SETINGS.DATATBASE_URL, uuidRepresentation="standard"
)


db = client["database_name"]


async def get_user_db() -> AsyncGenerator[type[User]]:
    "Return User object."
    yield BeanieUserDatabase(User)
