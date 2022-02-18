import re
from loguru import logger

logger.add("log/debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB", compression="zip")


def calculate(expression):
    request = []
    result = 0
    ex = re.split(r'\[|\]|\(|\)', expression.replace(" ", ""), maxsplit=12)
    logger.debug(ex)

    for n in ex:
        if n != '':
            request.append(n)
    logger.debug(request)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    for i in range(len(request)):
        if i == (len(request) - 1):
            if is_number(request[i]):
                if float(request[i]) != 0:
                    result = result * float(request[i])
            else:
                return {"request": ' '.join(request), "response": "Division by zero", "status": "fail"}
        elif i == 0 and request[i] == '-':
            result = float(request[i + 1]) * (-1)
        elif i == 0 and request[i] == '+':
            result = float(request[i + 1])
        elif is_number(request[i]):
            continue
        elif request[i] == '+':
            result = result + float(request[i + 1])
            logger.debug(i)
            logger.debug(result)
        elif request[i] == '-':
            result = result - float(request[i + 1])
            logger.debug(i)
            logger.debug(result)
        elif request[i] == '*':
            result = result * float(request[i + 1])
        elif request[i] == '/':
            logger.debug(i)
            if float(request[i + 1]) == 0:
                return {"request": ' '.join(request), "response": "Division by zero", "status": "fail"}
            else:
                result = result / float(request[i + 1])
        else:
            result = 'Try agayn'
    if is_number(result):
        return {"request": ' '.join(request), "response": round(float(result), 3), "status": "OK"}
    else:
        return {"request": ' '.join(request), "response": result, "status": "fail"}
