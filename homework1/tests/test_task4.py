import pytest
from task4 import calculate_discount

def test_integer():
    assert calculate_discount(100, 5) == 95

def test_float():
    assert calculate_discount(20.50, 20) == pytest.approx(16.4, 0.01)
    assert calculate_discount(100, 10.5) == pytest.approx(89.5, 0.01)
    assert calculate_discount(25.5, 45.5) == pytest.approx(13.8975, 0.01)


def test_zero():
    assert calculate_discount(50, 0) == 50
    assert calculate_discount(25.99, 0) == 25.99

def test_invalid():
    assert calculate_discount("100", 5) is None
    assert calculate_discount(100, "5") is None
    assert calculate_discount("100", "5") is None
