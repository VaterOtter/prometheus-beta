import pytest
from src.k_largest import k_largest

def test_k_largest_normal_case():
    """Test k_largest with a normal input scenario."""
    assert k_largest([3, 1, 5, 12, 2, 11], 3) == [12, 11, 5]

def test_k_largest_all_elements():
    """Test k_largest when k equals the array length."""
    assert k_largest([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1]

def test_k_largest_zero_elements():
    """Test k_largest when k is zero."""
    assert k_largest([1, 2, 3, 4, 5], 0) == []

def test_k_largest_empty_array():
    """Test k_largest with an empty array."""
    assert k_largest([], 0) == []

def test_k_largest_negative_k():
    """Test k_largest with a negative k."""
    with pytest.raises(ValueError, match="k cannot be negative"):
        k_largest([1, 2, 3], -1)

def test_k_largest_k_too_large():
    """Test k_largest when k is larger than array length."""
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        k_largest([1, 2, 3], 4)

def test_k_largest_invalid_input_type():
    """Test k_largest with invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list"):
        k_largest("not a list", 2)
    
    with pytest.raises(TypeError, match="k must be an integer"):
        k_largest([1, 2, 3], "2")

def test_k_largest_duplicate_elements():
    """Test k_largest with duplicate elements."""
    assert k_largest([3, 3, 3, 1, 2], 3) == [3, 3, 3]