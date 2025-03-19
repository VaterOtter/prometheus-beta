import pytest
from src.unique_pairs import get_unique_pairs

def test_basic_unique_pairs():
    """Test basic functionality with a simple list of integers."""
    result = get_unique_pairs([1, 2, 3])
    expected = [(1, 2), (1, 3), (2, 3)]
    assert sorted(result) == sorted(expected)

def test_empty_list():
    """Test behavior with an empty list."""
    assert get_unique_pairs([]) == []

def test_single_element_list():
    """Test behavior with a list containing only one element."""
    assert get_unique_pairs([5]) == []

def test_list_with_duplicates():
    """Test behavior with a list containing duplicate elements."""
    result = get_unique_pairs([1, 1, 2])
    expected = [(1, 1), (1, 2), (1, 2)]
    assert len(result) == 3
    assert all(len(pair) == 2 for pair in result)

def test_larger_list():
    """Test with a larger list of integers."""
    result = get_unique_pairs([1, 2, 3, 4])
    expected = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    assert sorted(result) == sorted(expected)

def test_pair_uniqueness():
    """Ensure pairs are unique regardless of order."""
    result = get_unique_pairs([1, 2])
    assert [(1, 2)] == result