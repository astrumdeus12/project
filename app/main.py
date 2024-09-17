#!/usr/bin/env python3

from fastapi import FastAPI

from app.config import APP_SETINGS

app = FastAPI()

v1 = FastAPI()


@app.get("/info")
async def info(settings: str = APP_SETINGS) -> str:
    "Return settings."
    return {
        "app_name": settings.app_name,
    }
