import task2

def test_integer():
    assert task2.intType == 5
    assert isinstance(task2.intType, int)

def test_float():
    assert task2.floatType == 3.5
    assert isinstance(task2.floatType, float)

def test_string():
    assert task2.stringType == "penguin"
    assert isinstance(task2.stringType, str)

def test_boolean():
    assert task2.boolType == True
    assert isinstance(task2.boolType, bool)

def test_boolean_negate():
    assert task2.boolType == False
    assert isinstance(task2.boolType, bool)