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
    response = calculate("[+](7.322)[(*)(0)]2")
    assert response == {
    "request": "+ 7.322 * 0 2",
    "response": 0.0,
    "status": "OK"
    }


def test_calculate_by_text():
    response = calculate("[+](+7.322)[(*jj)(-0)]2")
    assert response == {
    "request": "+ +7.322 *jj -0 2",
    "response": 0.0,
    "status": "OK"
    }
