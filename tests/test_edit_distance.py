import pytest
from src.edit_distance import edit_distance

def test_edit_distance_same_strings():
    """Test edit distance when strings are identical"""
    assert edit_distance("hello", "hello") == 0

def test_edit_distance_different_lengths():
    """Test edit distance with strings of different lengths"""
    assert edit_distance("kitten", "sitting") == 3

def test_edit_distance_empty_strings():
    """Test edit distance with empty strings"""
    assert edit_distance("", "") == 0
    assert edit_distance("hello", "") == 5
    assert edit_distance("", "world") == 5

def test_edit_distance_single_char_changes():
    """Test simple single character operations"""
    assert edit_distance("cat", "cut") == 1  # replace
    assert edit_distance("cat", "cart") == 1  # insert
    assert edit_distance("cart", "cat") == 1  # delete

def test_edit_distance_complex_cases():
    """Test more complex edit distance scenarios"""
    assert edit_distance("sunday", "saturday") == 3
    assert edit_distance("intention", "execution") == 5

def test_edit_distance_case_sensitive():
    """Test that the function is case-sensitive"""
    assert edit_distance("Hello", "hello") == 1

def test_edit_distance_invalid_input():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        edit_distance(123, "hello")
    with pytest.raises(TypeError):
        edit_distance("hello", None)
    with pytest.raises(TypeError):
        edit_distance(["h", "i"], "hi")