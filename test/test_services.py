from app import services


def test_calculate():
    response = services.calculate("[+](7.322)[(*)(12.32233)]0")
    assert response == ('+ 7.322 * 12.32233 0', '90.224', 'OK')


def test_calculate_by_zero():
    response = services.calculate("[+](7.322)[(/)(0)]2")
    assert response == ('+ 7.322 / 0 2', 'Division by zero', 'fail')


def test_calculate_by_text():
    response = services.calculate("[+](+7.322)[(*jj)(-0)]2")
    assert response == ('+ +7.322 *jj -0 2', 'Incorrect input format', 'fail')


def test_calculate_first_element():
    response = services.calculate("[*](+7.322)[(-7)(-0)]2")
    assert response == ('* +7.322 -7 -0 2', 'Incorrect input format', 'fail')


def test_request_first():
    response = services.calculate("[+](100.1)")
    assert response == ('+ 100.1', '100.1', 'OK')


def test_request_second():
    response = services.calculate("[+](0)")
    assert response == ('+ 0', '0', 'OK')


def test_request_third():
    response = services.calculate("[-](7)(/)(34.2)")
    assert response == ('- 7 / 34.2', '-0.205', 'OK')


def test_request_fourth():
    response = services.calculate("[-](6)(*)(2)")
    assert response == ('- 6 * 2', '-12.0', 'OK')


def test_request_fifth():
    response = services.calculate("[-](6)(*)(2)")
    assert response == ('- 6 * 2', '-12.0', 'OK')


def test_request_sixth():
    response = services.calculate("[+](2)(/)(1)")
    assert response == ('+ 2 / 1', '2', 'OK')


def test_request_seventh():
    response = services.calculate("[*](1)(+)(7)")
    assert response == ('* 1 + 7', 'Incorrect input format', 'fail')


def test_request_eighth():
    response = services.calculate("[+](4)(/)(3)(+)")
    assert response == ('+ 4 / 3 +', 'Incorrect input format', 'fail')


def test_append_history_del():
    var = services.history_of_operations
    result = services.calculate("[-](6)(*)(2)")
    i = 0
    while i <= 35:
        services.append_history(result)
        i = i + 1

    assert len(var) == 30


def test_get_history():
    response = False
    result = services.calculate("[-](6)(*)(2)")
    i = 0
    while i <= 4:
        services.append_history(result)
        i = i + 1

    result = services.calculate("[-](6)(/)(0)")
    i = 0
    while i <= 4:
        services.append_history(result)
        i = i + 1
    responseone = services.get_history(10, 1)
    responsesecond = services.get_history(10, 2)
    responsethird = services.get_history(10, 3)
    if len(responseone) == 10 and len(responsesecond) == 5 and len(responsethird) == 5:
        response = True
    assert response == True

# +100.1 → 100.1
# 0 → 0
# -7 / 34.2 → -0.205
# - 6 * 2 → -11.98
# 2 / 1 → 2
# 5 + - 4 → ошибка
# *1 + 7 → ошибка
# 4 / 3 + → ошибка
