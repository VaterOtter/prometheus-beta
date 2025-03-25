import pytest
from src.parity_subsequence import find_longest_parity_subsequence

def test_mixed_array_even_subsequence():
    """Test finding the longest even subsequence in a mixed array."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert find_longest_parity_subsequence(arr) == [2, 4, 6, 8]

def test_mixed_array_odd_subsequence():
    """Test finding the longest odd subsequence in a mixed array."""
    arr = [2, 1, 3, 5, 4, 7, 8]
    assert find_longest_parity_subsequence(arr) == [1, 3, 5, 7]

def test_all_even_array():
    """Test an array with all even numbers."""
    arr = [2, 4, 6, 8, 10]
    assert find_longest_parity_subsequence(arr) == [2, 4, 6, 8, 10]

def test_all_odd_array():
    """Test an array with all odd numbers."""
    arr = [1, 3, 5, 7, 9]
    assert find_longest_parity_subsequence(arr) == [1, 3, 5, 7, 9]

def test_empty_array():
    """Test an empty input array."""
    arr = []
    assert find_longest_parity_subsequence(arr) == []

def test_single_even_number():
    """Test an array with a single even number."""
    arr = [2]
    assert find_longest_parity_subsequence(arr) == [2]

def test_single_odd_number():
    """Test an array with a single odd number."""
    arr = [3]
    assert find_longest_parity_subsequence(arr) == [3]

def test_alternating_numbers():
    """Test an array with alternating even and odd numbers."""
    arr = [1, 2, 3, 4, 5, 6]
    assert find_longest_parity_subsequence(arr) == [2, 4, 6]

def test_multiple_equal_length_subsequences():
    """Test when multiple subsequences of the same length exist."""
    arr = [2, 4, 1, 3, 6, 8]
    result = find_longest_parity_subsequence(arr)
    assert result in [[2, 4], [6, 8]] or result in [[1, 3]]