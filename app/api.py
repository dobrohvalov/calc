import os

from app import schemas
from app import services

from fastapi import APIRouter

from app.crosszero import crosszero

api_router = APIRouter(prefix='', tags=["backend"])


@api_router.get('/', status_code=201)
async def root():
    API_KEY = os.environ.get('API_KEY')
    return {'api_key': API_KEY}


@api_router.get('/calc', response_model=schemas.request, status_code=201)
def read_expression(expression):
    result = services.calculate(expression)
    request = schemas.request(request=result[0], response=result[1], status=result[2])
    services.append_history(request)
    return request


@api_router.post('/history', status_code=201)
def read_expression(params: schemas.historyFilter):
    request = services.get_history(params.limit, params.status)
    return request


@api_router.post('/crosszero', status_code=201)
def read_expression(params: schemas.play):
    request = crosszero(params.width, params.height, params.quantity).play()
    return request