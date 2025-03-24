import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) == True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test some known non-perfect numbers."""
    non_perfect_numbers = [1, 2, 3, 4, 5, 10, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) == False, f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases and error handling."""
    # Zero and negative numbers should raise ValueError
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(-10)

def test_invalid_input_types():
    """Test invalid input types."""
    # Non-integer inputs should raise ValueError
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(6.5)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number("6")
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number([6])