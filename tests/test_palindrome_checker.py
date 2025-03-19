import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome scenarios."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_simple_palindromes():
    """Test simple palindrome cases."""
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False

def test_edge_cases():
    """Test edge cases for palindrome checking."""
    # Empty string is considered a palindrome
    assert is_palindrome("") == True
    
    # Single character is a palindrome
    assert is_palindrome("a") == True
    
    # Strings with only non-alphanumeric characters
    assert is_palindrome("!@#$") == True

def test_case_sensitivity():
    """Test that the function is case-insensitive."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("NOT A PALINDROME") == False

def test_punctuation_and_spaces():
    """Test handling of punctuation and spaces."""
    assert is_palindrome("A Santa at NASA") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_numeric_palindromes():
    """Test palindromes with numbers."""
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False