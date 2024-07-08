"""Модуль запуска сервера."""
import logging

import uvicorn
from fastapi import FastAPI

from fastapi_test_task.memes.router import memes_router
from fastapi_test_task.settings import Settings

logger = logging.getLogger()
settings = Settings()

app = FastAPI()
app.include_router(router=memes_router)


if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )
