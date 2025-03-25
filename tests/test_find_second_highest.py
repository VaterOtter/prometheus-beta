import pytest
from src.find_second_highest import find_second_highest

def test_sorted_ascending_list():
    """Test finding second highest in an ascending sorted list."""
    assert find_second_highest([1, 2, 3, 4, 5]) == 4

def test_sorted_descending_list():
    """Test finding second highest in a descending sorted list."""
    assert find_second_highest([5, 4, 3, 2, 1]) == 4

def test_list_with_duplicates():
    """Test list with duplicate values."""
    assert find_second_highest([1, 2, 2, 3, 3, 4, 4, 5]) == 4

def test_list_with_two_unique_values():
    """Test list with only two unique values."""
    assert find_second_highest([1, 1, 2, 2]) == 1

def test_list_with_single_unique_value():
    """Test list with single unique value returns None."""
    assert find_second_highest([1, 1, 1]) is None

def test_empty_list_raises_error():
    """Test that empty list raises ValueError."""
    with pytest.raises(ValueError, match="List cannot be empty"):
        find_second_highest([])

def test_non_list_input_raises_error():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_second_highest("not a list")

def test_single_element_list():
    """Test single element list returns None."""
    assert find_second_highest([42]) is None