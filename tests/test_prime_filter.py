import pytest
from src.prime_filter import filter_primes

def test_positive_primes():
    """Test filtering of positive prime numbers."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]
    assert set(filter_primes(input_list)) == {2, 3, 5, 7, 11, 13}

def test_negative_primes():
    """Test filtering of negative prime numbers."""
    input_list = [-1, -2, -3, -4, -5, -6, -7, 7, 11, -11]
    assert set(filter_primes(input_list)) == {-11, -7, -5, -3, -2, 7, 11}

def test_mixed_numbers():
    """Test filtering of mixed positive and negative numbers."""
    input_list = [-10, -7, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, -11]
    assert set(filter_primes(input_list)) == {-11, -7, 2, 3, 5, 7, 11, 13}

def test_empty_list():
    """Test filtering of an empty list."""
    assert filter_primes([]) == []

def test_no_primes():
    """Test list with no prime numbers."""
    input_list = [0, 1, 4, 6, 8, 9, 10, 12]
    assert filter_primes(input_list) == []