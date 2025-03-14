import pytest
from src.anagram_checker import is_anagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert is_anagram("Debit Card", "Bad Credit") == True
    assert is_anagram("Night", "Thing") == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert is_anagram("astronomer", "moon starer") == True
    assert is_anagram("  race", "care  ") == True

def test_non_anagrams():
    """Test pairs that are not anagrams"""
    assert is_anagram("test", "text") == False
    assert is_anagram("hello", "world") == False

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram("", "") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram("abc", "abcd") == False
    assert is_anagram("a", "") == False

def test_type_errors():
    """Test type checking"""
    with pytest.raises(TypeError):
        is_anagram(123, "test")
    with pytest.raises(TypeError):
        is_anagram("test", None)
    with pytest.raises(TypeError):
        is_anagram(None, None)