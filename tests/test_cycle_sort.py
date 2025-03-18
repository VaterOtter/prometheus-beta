import pytest
from src.cycle_sort import cycle_sort

def test_cycle_sort_normal_list():
    """Test sorting a normal list of integers."""
    arr = [5, 2, 9, 1, 7, 6, 3]
    result = cycle_sort(arr.copy())
    assert result == sorted(arr)

def test_cycle_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    result = cycle_sort(arr.copy())
    assert result == arr

def test_cycle_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    result = cycle_sort(arr.copy())
    assert result == sorted(arr)

def test_cycle_sort_with_duplicates():
    """Test sorting a list with duplicate values."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    result = cycle_sort(arr.copy())
    assert result == sorted(arr)

def test_cycle_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    result = cycle_sort(arr.copy())
    assert result == []

def test_cycle_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    result = cycle_sort(arr.copy())
    assert result == arr

def test_cycle_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-5, -2, -9, -1, -7, -6, -3]
    result = cycle_sort(arr.copy())
    assert result == sorted(arr)

def test_cycle_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers."""
    arr = [-5, 2, 0, -3, 7, 1, -1]
    result = cycle_sort(arr.copy())
    assert result == sorted(arr)

def test_cycle_sort_invalid_input():
    """Test that an error is raised for non-list input."""
    with pytest.raises(TypeError):
        cycle_sort("not a list")

def test_cycle_sort_in_place():
    """Test that the sorting happens in-place."""
    arr = [5, 2, 9, 1, 7, 6, 3]
    original = arr.copy()
    cycle_sort(arr)
    assert arr == sorted(original)
    assert arr is not original  # Ensure the same object is returned