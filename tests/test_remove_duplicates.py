import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates(['a', 'b', 'c']) == ['a', 'b', 'c']

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types of elements"""
    assert remove_duplicates([1, '1', 2, '2', 1, '1']) == [1, '1', 2, '2']

def test_remove_duplicates_error_handling():
    """Test error handling for non-list inputs"""
    with pytest.raises(TypeError):
        remove_duplicates("not a list")
    
    with pytest.raises(TypeError):
        remove_duplicates(123)

def test_remove_duplicates_preserve_order():
    """Test that the order of first occurrence is preserved"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert remove_duplicates(input_list) == [3, 1, 4, 5, 9, 2, 6]