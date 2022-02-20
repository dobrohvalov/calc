import re
from loguru import logger
from app import schemas

logger.add("log/debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB", compression="zip")

history_of_operations = []


def calculate(expression):
    # Основная функция обработки, на вход приходит не обработанный запрос
    request = []
    result = 0
    # Обрабатываем запрос и разделяем на операции и числа
    ex = re.split(r'\[|\]|\(|\)', expression.replace(" ", ""), maxsplit=12)
    logger.debug(ex)
    # Убераем пустые элементы в массиве, и получаем выражение
    for n in ex:
        if n != '':
            request.append(n)
    logger.debug(request)

    # Проверяем, является ли числом
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    # Приведем формат числа к заданному. Округление до 3 элемента после запятой.
    def formatNumber(num):
        if num % 1 == 0:
            return int(num)
        else:
            return round(float(num), 3)

    # Обрабатываем полученное выражение
    for i in range(len(request)):
        # Проверяем последний элемент, если есть хотя бы одна операция
        if i == (len(request) - 1) and i > 3:
            if is_number(request[i]):
                if float(request[i]) != 0:
                    result = result * float(request[i])
            else:
                result = "Incorrect input format"
                break

        # Проверяем первый элемент, он должен быть, либо + либо -
        elif i == 0 and request[i] == '-':
            result = float(request[i + 1]) * (-1)
        elif i == 0 and request[i] == '+':
            result = float(request[i + 1])

        # Проводим расчет операции
        elif is_number(request[i]):
            continue
        elif i > 0 and request[i] == '+':
            result = result + float(request[i + 1])
            logger.debug(i)
            logger.debug(result)
        elif i > 0 and request[i] == '-':
            result = result - float(request[i + 1])
            logger.debug(i)
            logger.debug(result)
        elif i > 0 and request[i] == '*':
            result = result * float(request[i + 1])
        elif i > 0 and request[i] == '/':
            logger.debug(i)
            if float(request[i + 1]) == 0:
                # Проверяем деление на ноль
                result = "Division by zero"
                break
            else:
                result = result / float(request[i + 1])
            logger.debug(result)
        else:
            # Если не прошло вырождение, то запись была сделана не в соответствии с требованиями
            result = "Incorrect input format"
            break

    # Выводим результат или ошибку
    if is_number(result):
        logger.debug(' '.join(request))
        logger.debug(round(float(result), 3))
        return ' '.join(request), str(formatNumber(result)), "OK"
    else:
        logger.debug(' '.join(request))
        logger.debug(result)
        return ' '.join(request), result, "fail"


def append_history(result):
    global history_of_operations

    history_of_operations.append(result)

    while len(history_of_operations) > 30:
        del history_of_operations[0]


def get_history(limit, status):
    result = []
    # Проверяем, что бы лимит не получился отрецательным
    if limit > len(history_of_operations):
        limit = len(history_of_operations)
    # Проверяем, есть ли история
    logger.debug(history_of_operations)
    if len(history_of_operations) == 0:
        result = 'Пока не было расчетов'
    # Отбираем результаты по фильтру
    for i in history_of_operations[(len(history_of_operations) - limit):len(history_of_operations)]:
        request = history_of_operations[history_of_operations.index(i)]
        story = schemas.request(request=request[0], response=request[1], status=request[2])
        logger.debug(story)
        if story.status == "fail" and (status == 1 or status == 3):
            result.append(story)
        elif story.status == "OK" and (status == 1 or status == 2):
            result.append(story)
    return result