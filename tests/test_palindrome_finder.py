import pytest
from src.palindrome_finder import find_palindromic_substrings

def test_basic_palindromes():
    """Test basic palindromic substring scenarios."""
    assert sorted(find_palindromic_substrings("abc")) == ['a', 'b', 'c']
    assert sorted(find_palindromic_substrings("racecar")) == ['a', 'aceca', 'c', 'cec', 'e', 'r', 'racecar']

def test_empty_and_single_char():
    """Test edge cases with empty string and single character."""
    assert find_palindromic_substrings("") == []
    assert find_palindromic_substrings("a") == ['a']

def test_multiple_palindromes():
    """Test strings with multiple palindromic substrings."""
    result = find_palindromic_substrings("aaa")
    assert sorted(result) == ['a', 'aa', 'aaa']

def test_no_palindromes():
    """Test strings with no repeating characters."""
    assert sorted(find_palindromic_substrings("abcd")) == ['a', 'b', 'c', 'd']

def test_longer_palindromes():
    """Test longer palindromic substrings."""
    result = find_palindromic_substrings("abaxyzzyxf")
    expected = ['a', 'b', 'x', 'y', 'z', 'aba', 'xyzyx']
    assert sorted(result) == sorted(expected)

def test_invalid_input():
    """Test handling of invalid input types."""
    assert find_palindromic_substrings(None) == []
    assert find_palindromic_substrings(123) == []

def test_case_sensitivity():
    """Test case-sensitive palindrome detection."""
    result = find_palindromic_substrings("Aba")
    assert sorted(result) == ['A', 'a', 'b']