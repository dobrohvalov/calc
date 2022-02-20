import os

from app import schemas
from app import services

from fastapi import APIRouter

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

# @api_router.get("/start/", status_code=201)
# async def start():
#     await services.portal_list()
#     return capture_message('Start intagration')
#
#
# @api_router.post("/setting/", status_code=201)
# async def get_setting(params: schemas.Portal) -> Dict[str, Any]:
#     """Получаем настройки из бд, для конкретного портала.
#     Возвращаем логин, пароль"""
#     portal = params.portal
#     request = await crud.get_setting(portal)
#     return {"tl_logging": request[0], "tl_password": request[1]}
