import pytest
from src.string_reversal import recursive_reverse

def test_recursive_reverse_empty_string():
    """Test reversing an empty string."""
    assert recursive_reverse("") == ""

def test_recursive_reverse_single_char():
    """Test reversing a single character string."""
    assert recursive_reverse("a") == "a"

def test_recursive_reverse_normal_string():
    """Test reversing a normal string."""
    assert recursive_reverse("hello") == "olleh"

def test_recursive_reverse_palindrome():
    """Test reversing a palindrome."""
    assert recursive_reverse("racecar") == "racecar"

def test_recursive_reverse_with_spaces():
    """Test reversing a string with spaces."""
    assert recursive_reverse("hello world") == "dlrow olleh"

def test_recursive_reverse_with_symbols():
    """Test reversing a string with symbols."""
    assert recursive_reverse("a1b2c3") == "3c2b1a"

def test_recursive_reverse_invalid_input():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse(None)