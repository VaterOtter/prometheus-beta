import pytest
from src.string_reversal import reverse_string_in_place

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string_in_place("hello") == "olleh"
    assert reverse_string_in_place("python") == "nohtyp"

def test_reverse_string_empty():
    """Test empty string."""
    assert reverse_string_in_place("") == ""

def test_reverse_string_single_char():
    """Test single character string."""
    assert reverse_string_in_place("a") == "a"

def test_reverse_string_with_spaces():
    """Test string with spaces."""
    assert reverse_string_in_place("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test string with special characters."""
    assert reverse_string_in_place("a1b2c3!@#") == "#@!3c2b1a"

def test_reverse_string_invalid_input():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        reverse_string_in_place(123)
    
    with pytest.raises(TypeError):
        reverse_string_in_place(None)
    
    with pytest.raises(TypeError):
        reverse_string_in_place(["not", "a", "string"])