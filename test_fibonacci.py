import pytest
from fibonacci import calculate_fibonacci

def test_fibonacci_base_cases():
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1

def test_fibonacci_some_values():
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    assert calculate_fibonacci(2) == 1
    assert calculate_fibonacci(3) == 2
    assert calculate_fibonacci(4) == 3
    assert calculate_fibonacci(5) == 5
    assert calculate_fibonacci(6) == 8
    assert calculate_fibonacci(7) == 13
    assert calculate_fibonacci(8) == 21
    assert calculate_fibonacci(9) == 34

def test_fibonacci_larger_value():
    # Known value
    assert calculate_fibonacci(10) == 55
    assert calculate_fibonacci(15) == 610

def test_fibonacci_type_error():
    with pytest.raises(TypeError):
        calculate_fibonacci(3.5)
    with pytest.raises(TypeError):
        calculate_fibonacci("10")

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        calculate_fibonacci(-1)
