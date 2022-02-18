import os
from app.services import calculate

from fastapi import APIRouter

api_router = APIRouter(prefix='', tags=["backend"])


@api_router.get('/', status_code=201)
async def root():
    API_KEY = os.environ.get('API_KEY')
    return {'api_key': API_KEY}


# http://127.0.0.1:8000/calc?expression=[+](7.322)[(*)(12.32233)]*,
@api_router.get('/calc', status_code=201)
async def read_expression(expression):
    result = calculate(expression)

    return result

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
