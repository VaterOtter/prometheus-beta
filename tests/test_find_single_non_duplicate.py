import pytest
from src.find_single_non_duplicate import find_single_non_duplicate

def test_basic_single_non_duplicate():
    """Test a basic scenario with a single non-duplicate element"""
    arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    assert find_single_non_duplicate(arr) == 2

def test_single_non_duplicate_at_start():
    """Test when the single non-duplicate element is at the start"""
    arr = [2, 3, 3, 4, 4, 5, 5]
    assert find_single_non_duplicate(arr) == 2

def test_single_non_duplicate_at_end():
    """Test when the single non-duplicate element is at the end"""
    arr = [1, 1, 2, 2, 3, 4, 4]
    assert find_single_non_duplicate(arr) == 3

def test_single_element_array():
    """Test an array with a single element"""
    arr = [5]
    assert find_single_non_duplicate(arr) == 5

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_single_non_duplicate(None)
    
    with pytest.raises(TypeError):
        find_single_non_duplicate("not a list")
    
    with pytest.raises(ValueError):
        find_single_non_duplicate([])

def test_large_array():
    """Test a larger array with a non-duplicate element"""
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7]
    assert find_single_non_duplicate(arr) == 4

def test_consecutive_non_duplicate():
    """Test consecutive single non-duplicate elements"""
    arr = [1, 1, 2, 3, 3, 4, 4, 5, 5]
    assert find_single_non_duplicate(arr) == 2