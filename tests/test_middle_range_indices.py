import pytest
from src.middle_range_indices import find_middle_range_indices

def test_odd_length_list():
    """Test with an odd-length list."""
    test_list = [1, 2, 3, 4, 5, 6, 7]
    assert find_middle_range_indices(test_list, 1) == [2, 3, 4]

def test_even_length_list():
    """Test with an even-length list."""
    test_list = [1, 2, 3, 4, 5, 6]
    # For even-length lists, the midpoint is left-of-center
    assert find_middle_range_indices(test_list, 1) == [1, 2, 3]

def test_range_size_zero():
    """Test with range size of zero."""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list, 0) == [2]

def test_range_size_larger_than_list():
    """Test when range size is larger than the list length."""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list, 10) == list(range(5))

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_middle_range_indices([], 1)

def test_negative_range_size_raises_error():
    """Test that a negative range size raises a ValueError."""
    with pytest.raises(ValueError, match="Range size cannot be negative"):
        find_middle_range_indices([1, 2, 3], -1)

def test_invalid_input_type_raises_error():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_middle_range_indices("not a list", 1)
    
    with pytest.raises(TypeError, match="Range size must be an integer"):
        find_middle_range_indices([1, 2, 3], "not an int")