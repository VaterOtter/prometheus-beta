import pytest
from src.fizzy_numbers import find_fizzy_numbers

def test_find_fizzy_numbers_normal_case():
    """Test finding fizzy numbers in a typical scenario."""
    result = find_fizzy_numbers(10)
    assert result == [3, 6, 7, 9], "Should find numbers divisible by 3 or 7"

def test_find_fizzy_numbers_single_digit():
    """Test finding fizzy numbers for a single-digit input."""
    result = find_fizzy_numbers(1)
    assert result == [], "Should return empty list for small inputs"

def test_find_fizzy_numbers_larger_range():
    """Test finding fizzy numbers in a larger range."""
    result = find_fizzy_numbers(21)
    expected = [3, 6, 7, 9, 12, 14, 15, 18, 21]
    assert result == expected, "Should find all numbers divisible by 3 or 7"

def test_find_fizzy_numbers_invalid_input():
    """Test handling of invalid inputs."""
    # Test non-integer input
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        find_fizzy_numbers("10")
    
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        find_fizzy_numbers(-5)
    
    # Test zero input
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        find_fizzy_numbers(0)