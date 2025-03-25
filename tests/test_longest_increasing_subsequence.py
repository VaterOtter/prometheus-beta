import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence_length

def test_basic_increasing_sequence():
    """Test a basic increasing sequence"""
    assert longest_increasing_subsequence_length([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6

def test_empty_list():
    """Test an empty list returns 0"""
    assert longest_increasing_subsequence_length([]) == 0

def test_single_element_list():
    """Test a list with a single element"""
    assert longest_increasing_subsequence_length([5]) == 1

def test_completely_decreasing_list():
    """Test a completely decreasing list"""
    assert longest_increasing_subsequence_length([5, 4, 3, 2, 1]) == 1

def test_all_same_elements():
    """Test a list with all same elements"""
    assert longest_increasing_subsequence_length([2, 2, 2, 2]) == 1

def test_mixed_sequence():
    """Test a mixed sequence"""
    assert longest_increasing_subsequence_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_negative_numbers():
    """Test a sequence with negative numbers"""
    assert longest_increasing_subsequence_length([-7, 10, 9, 2, 3, 8, 8, 1, 2, 3, 4]) == 5

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        longest_increasing_subsequence_length("not a list")
        longest_increasing_subsequence_length(123)
        longest_increasing_subsequence_length(None)