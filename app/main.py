from functools import lru_cache
from typing import Annotated
from  fastapi import Depends, FastAPI

from app.config import APP_SETINGS


app = FastAPI()

v1 = FastAPI()






@app.get("/info")
async def info(settings = APP_SETINGS ):
    return {
        "app_name": settings.app_name,
        
    }