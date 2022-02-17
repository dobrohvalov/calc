from datetime import datetime

from pydantic import BaseModel
from typing import List

"""
Описываем модели для pydantic
Необходима для работы API
"""


class expression(BaseModel):
    operation1: int
    operation1: int
    number1: int
    number2: int
