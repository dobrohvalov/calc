from pydantic import BaseModel

"""
Описываем модели для pydantic
Необходима для работы API
"""


class request(BaseModel):
    request: str
    response: str
    status: str


class historyFilter(BaseModel):
    limit: int
    status: int


class play(BaseModel):
    width: int
    height: int
    quantity: int
