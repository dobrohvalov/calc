from fastapi import FastAPI
from app.api import api_router

app = FastAPI(
    title='calc',
    description='calc for example',
    version='0.0.1',
)

app.include_router(api_router)
