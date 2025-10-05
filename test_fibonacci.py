import pytest
from fibonacci import calculate_fibonacci

def test_fibonacci_basic():
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1
    assert calculate_fibonacci(2) == 1
    assert calculate_fibonacci(5) == 5
    assert calculate_fibonacci(10) == 55

def test_fibonacci_larger():
    assert calculate_fibonacci(20) == 6765
    assert calculate_fibonacci(30) == 832040

def test_fibonacci_type_error():
    with pytest.raises(TypeError):
        calculate_fibonacci(2.5)
    with pytest.raises(TypeError):
        calculate_fibonacci("5")

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        calculate_fibonacci(-1)
    with pytest.raises(ValueError):
        calculate_fibonacci(-10)
