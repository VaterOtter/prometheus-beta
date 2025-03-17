import pytest
from src.lcm import find_lcm

def test_lcm_basic_positive_numbers():
    """Test LCM of basic positive integers"""
    assert find_lcm(4, 6) == 12
    assert find_lcm(3, 5) == 15
    assert find_lcm(2, 7) == 14

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert find_lcm(5, 5) == 5
    assert find_lcm(10, 10) == 10

def test_lcm_one_is_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert find_lcm(4, 8) == 8
    assert find_lcm(7, 14) == 14

def test_lcm_prime_numbers():
    """Test LCM of prime numbers"""
    assert find_lcm(11, 13) == 143
    assert find_lcm(2, 3) == 6

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        find_lcm(4.5, 6)
    with pytest.raises(TypeError):
        find_lcm("4", 6)
    with pytest.raises(TypeError):
        find_lcm(4, "6")

def test_invalid_input_values():
    """Test error handling for non-positive inputs"""
    with pytest.raises(ValueError):
        find_lcm(0, 5)
    with pytest.raises(ValueError):
        find_lcm(5, 0)
    with pytest.raises(ValueError):
        find_lcm(-4, 6)
    with pytest.raises(ValueError):
        find_lcm(4, -6)