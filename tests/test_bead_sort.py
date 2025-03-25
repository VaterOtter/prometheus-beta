import pytest
from src.bead_sort import bead_sort

def test_bead_sort_basic():
    """Test basic sorting functionality"""
    assert bead_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_bead_sort_already_sorted():
    """Test list that is already sorted"""
    assert bead_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bead_sort_reverse_sorted():
    """Test list sorted in reverse order"""
    assert bead_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bead_sort_empty_list():
    """Test empty list"""
    assert bead_sort([]) == []

def test_bead_sort_single_element():
    """Test list with single element"""
    assert bead_sort([42]) == [42]

def test_bead_sort_duplicate_elements():
    """Test list with duplicate elements"""
    assert bead_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bead_sort_zero_included():
    """Test list including zero"""
    assert bead_sort([0, 5, 3, 0, 1]) == [0, 0, 1, 3, 5]

def test_invalid_input_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        bead_sort([-1, 2, 3])

def test_invalid_input_non_integers():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        bead_sort("not a list")
    
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        bead_sort([1, 2, "3", 4])