import pytest
from src.capitalize_words import capitalize_comma_words

def test_basic_capitalization():
    """Test basic capitalization of words."""
    assert capitalize_comma_words("hello,world") == "Hello,World"

def test_already_capitalized():
    """Test input with already capitalized words."""
    assert capitalize_comma_words("Hello,World") == "Hello,World"

def test_mixed_case():
    """Test input with mixed case words."""
    assert capitalize_comma_words("hElLo,wOrLd") == "Hello,World"

def test_single_word():
    """Test input with a single word."""
    assert capitalize_comma_words("hello") == "Hello"

def test_multiple_words():
    """Test input with multiple words."""
    assert capitalize_comma_words("python,is,awesome") == "Python,Is,Awesome"

def test_empty_input():
    """Test empty input string."""
    assert capitalize_comma_words("") == ""

def test_invalid_input_with_spaces():
    """Test input with spaces (should raise ValueError)."""
    with pytest.raises(ValueError, match="Input must contain only alphabetical characters and commas"):
        capitalize_comma_words("hello world")

def test_invalid_input_with_numbers():
    """Test input with numbers (should raise ValueError)."""
    with pytest.raises(ValueError, match="Input must contain only alphabetical characters and commas"):
        capitalize_comma_words("hello123,world")

def test_invalid_input_with_punctuation():
    """Test input with punctuation (should raise ValueError)."""
    with pytest.raises(ValueError, match="Input must contain only alphabetical characters and commas"):
        capitalize_comma_words("hello!,world")