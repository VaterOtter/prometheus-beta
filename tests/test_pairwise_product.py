import pytest
from src.pairwise_product import calculate_pairwise_products

def test_basic_pairwise_products():
    """Test basic pairwise product calculation."""
    assert calculate_pairwise_products([1, 2, 3]) == [2, 3, 6]

def test_negative_numbers():
    """Test pairwise products with negative numbers."""
    assert calculate_pairwise_products([-1, 2, 3]) == [-2, -3, 6]

def test_single_element_list():
    """Test that an empty product list is returned for a single-element list."""
    assert calculate_pairwise_products([5]) == []

def test_large_numbers():
    """Test pairwise products with larger numbers."""
    assert calculate_pairwise_products([10, 20, 30]) == [200, 300, 600]

def test_zero_in_list():
    """Test pairwise products with zero in the list."""
    assert calculate_pairwise_products([0, 1, 2]) == [0, 0, 2]

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        calculate_pairwise_products([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_pairwise_products("not a list")

def test_non_integer_input_raises_error():
    """Test that list with non-integer elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_pairwise_products([1, 2, "3"])