from task4 import calculate_discount

def test_integer():
    assert calculate_discount(100, 5) == 95

def test_float():
    assert calculate_discount(20.50, 20) == 16.4
    assert calculate_discount(100, 10.5) == 89.5
    assert calculate_discount(25.5, 45.5) == 13.8975


def test_zero():
    assert calculate_discount(50, 0) == 50
    assert calculate_discount(25.99, 0) == 25.99

def test_invalid():
    assert calculate_discount("100", 5) is None
    assert calculate_discount(100, "5") is None
    assert calculate_discount("100", "5") is None
