import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test a typical case with positive integers."""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1

def test_all_same_numbers():
    """Test an array with all identical numbers."""
    arr = [5, 5, 5, 5, 5]
    k = 3
    assert max_subarray_sum(arr, k) == 15

def test_small_array():
    """Test with a very small array."""
    arr = [1, 2]
    k = 2
    assert max_subarray_sum(arr, k) == 3

def test_negative_numbers():
    """Test with negative numbers."""
    arr = [-1, -2, -3, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == -6

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    k = 3
    assert max_subarray_sum(arr, k) == 19  # 3 + 10 + -4

def test_invalid_k_too_large():
    """Test when k is larger than array length."""
    arr = [1, 2, 3]
    k = 4
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than array length"):
        max_subarray_sum(arr, k)

def test_invalid_k_zero():
    """Test when k is zero."""
    arr = [1, 2, 3]
    k = 0
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        max_subarray_sum(arr, k)

def test_invalid_k_negative():
    """Test when k is negative."""
    arr = [1, 2, 3]
    k = -1
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        max_subarray_sum(arr, k)

def test_none_input():
    """Test when input array is None."""
    arr = None
    k = 3
    with pytest.raises(ValueError, match="Input array cannot be None"):
        max_subarray_sum(arr, k)

def test_empty_input():
    """Test when input array is empty."""
    arr = []
    k = 3
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        max_subarray_sum(arr, k)