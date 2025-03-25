import pytest
from src.list_flattener import flatten_nested_list

def test_flatten_simple_list():
    """Test flattening a simple nested list."""
    input_list = [1, [2, 3], 4]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    input_list = [1, [2, [3, 4]], 5, [6, [7, 8]]]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_mixed_iterables():
    """Test flattening list with mixed iterables."""
    input_list = [1, (2, 3), [4, (5, 6)]]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_nested_list([]) == []

def test_flatten_none():
    """Test flattening None."""
    assert flatten_nested_list(None) == []

def test_flatten_with_strings():
    """Test flattening a list with strings."""
    input_list = ['a', ['b', 'c'], 'd']
    assert flatten_nested_list(input_list) == ['a', 'b', 'c', 'd']

def test_flatten_single_item_list():
    """Test flattening a list with a single nested item."""
    input_list = [1]
    assert flatten_nested_list(input_list) == [1]

def test_flatten_nested_single_item_list():
    """Test flattening a list with a single nested single-item list."""
    input_list = [[1]]
    assert flatten_nested_list(input_list) == [1]

def test_raises_type_error_for_non_iterable():
    """Test that non-iterable input raises a TypeError."""
    with pytest.raises(TypeError):
        flatten_nested_list(42)