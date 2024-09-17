#!/usr/bin/env python3

import uuid
from collections.abc import AsyncGenerator

from fastapi_users import BaseUserManager, UUIDIDMixin

from app.config import APP_SETINGS
from app.internal.database.mongo import get_user_db
from app.internal.models.user import User


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    "Manager for User."

    reset_password_token_secret = APP_SETINGS.SECRET
    verification_token_secret = APP_SETINGS.SECRET


# Add reset password from documentation


async def get_user_manager() -> AsyncGenerator[type[User]]:
    "Get manager for user."
    user_db = get_user_db()
    yield UserManager(user_db)
