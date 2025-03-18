import pytest
from src.longest_increasing_subsequence import longest_continuous_increasing_subsequence

def test_standard_increasing_sequence():
    """Test a standard increasing sequence"""
    assert longest_continuous_increasing_subsequence([1,3,5,4,7]) == 3

def test_all_equal_elements():
    """Test an array with all equal elements"""
    assert longest_continuous_increasing_subsequence([2,2,2,2,2]) == 1

def test_empty_array():
    """Test an empty array"""
    assert longest_continuous_increasing_subsequence([]) == 0

def test_single_element():
    """Test an array with a single element"""
    assert longest_continuous_increasing_subsequence([42]) == 1

def test_fully_increasing_sequence():
    """Test a fully increasing sequence"""
    assert longest_continuous_increasing_subsequence([1,2,3,4,5]) == 5

def test_multiple_increasing_subsequences():
    """Test array with multiple increasing subsequences"""
    assert longest_continuous_increasing_subsequence([1,3,5,1,2,3,4]) == 4

def test_non_increasing_sequence():
    """Test a strictly non-increasing sequence"""
    assert longest_continuous_increasing_subsequence([5,4,3,2,1]) == 1

def test_mixed_sequence():
    """Test a mixed sequence with some increasing parts"""
    assert longest_continuous_increasing_subsequence([1,2,3,0,2,3,4,5]) == 4