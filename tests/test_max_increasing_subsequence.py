import pytest
from src.max_increasing_subsequence import max_increasing_subsequence_sum

def test_empty_array():
    assert max_increasing_subsequence_sum([]) == 0

def test_single_element():
    assert max_increasing_subsequence_sum([5]) == 5

def test_increasing_sequence():
    assert max_increasing_subsequence_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_sequence():
    assert max_increasing_subsequence_sum([10, 9, 2, 5, 3, 7, 101, 18]) == 126

def test_negative_numbers():
    assert max_increasing_subsequence_sum([-2, -1, 3, 1, 4, 2]) == 6

def test_complex_sequence():
    assert max_increasing_subsequence_sum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 23

def test_all_negative():
    assert max_increasing_subsequence_sum([-5, -2, -1, -3, -4]) == -1

def test_large_numbers():
    assert max_increasing_subsequence_sum([1000000, 1, 2, 3, 4, 5]) == 1000015

def test_duplicate_numbers():
    assert max_increasing_subsequence_sum([1, 1, 1, 2, 2, 3, 3, 4]) == 10