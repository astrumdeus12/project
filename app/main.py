# noqa: INP001
from fastapi import FastAPI

from app.config import APP_SETINGS
from app.routers.course_router import router

app = FastAPI()

# v1 = FastAPI())


@app.get("/info")
async def info():  # noqa: ANN201
    "Return settings."
    return {
        "app_name": APP_SETINGS.app_name,
    }


app.include_router(router=router)
