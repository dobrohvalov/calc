import pytest

from app.services import calculate


def test_calculate():
    response = calculate("[+](7.322)[(*)(12.32233)]0")
    assert response == {
    "request": "+ 7.322 * 12.32233 0",
    "response": 90.224,
    "status": "OK"
    }


def test_calculate_by_zero():
    response = calculate("[+](7.322)[(/)(0)]2")
    assert response == {
    "request": "+ 7.322 / 0 2",
    "response": "Division by zero",
    "status": "fail"
    }


def test_calculate_by_text():
    response = calculate("[+](+7.322)[(*jj)(-0)]2")
    assert response == {
    "request": "+ +7.322 *jj -0 2",
    "response": 'Incorrect input format',
    "status": "fail"
    }


def test_calculate_first_element():
    response = calculate("[*](+7.322)[(-7)(-0)]2")
    assert response == {
    "request": "* +7.322 -7 -0 2",
    "response": 'Incorrect input format',
    "status": "fail"
    }


def test_request_first():
    response = calculate("[+](100.1)")
    assert response == {
    "request": "+ 100.1",
    "response": 100.1,
    "status": "OK"
    }


def test_request_second():
    response = calculate("[+](0)")
    assert response == {
    "request": "+ 0",
    "response": 0,
    "status": "OK"
    }


def test_request_third():
    response = calculate("[-](7)(/)(34.2)")
    assert response == {
    "request": "- 7 / 34.2",
    "response": -0.205,
    "status": "OK"
    }


def test_request_fourth():
    response = calculate("[-](+6)(*)(2)")
    assert response == {
    "request": "- 6 * 2",
    "response": -11.98,
    "status": "OK"
    }


def test_request_fifth():
    response = calculate("[-](6)(*)(2)")
    assert response == {
    "request": "- 6 * 2",
    "response": -12.0,
    "status": "OK"
    }


def test_request_sixth():
    response = calculate("[+](5)(+ -)(4)")
    assert response == {
    "request": "+ 5 +- 4",
    "response": 'Incorrect input format',
    "status": "fail"
    }


def test_request_seventh():
    response = calculate("[*](1)(+)(7)")
    assert response == {
    "request": "* 1 + 7",
    "response": 'Incorrect input format',
    "status": "fail"
    }


def test_request_eighth():
    response = calculate("[+](4)(/)(3)(+)")
    assert response == {
    "request": "+ 4 / 3 +",
    "response": 'Incorrect input format',
    "status": "fail"
    }

# +100.1 → 100.1
# 0 → 0
# -7 / 34.2 → -0.205
# - 6 * 2 → -11.98
# 2 / 1 → 2
# 5 + - 4 → ошибка
# *1 + 7 → ошибка
# 4 / 3 + → ошибка