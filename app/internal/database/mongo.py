import uuid
from fastapi_users_db_beanie import BeanieUserDatabase
from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend
from fastapi_users import FastAPIUsers
import motor.motor_asyncio
from app.config import settings
from app.internal.models.user import User
from app.internal.service.user_service import get_user_manager
from app.config import APP_SETINGS


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
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


async def get_user_db():
    yield BeanieUserDatabase(User)
