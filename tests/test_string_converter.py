import pytest
from src.string_converter import convert_to_uppercase_with_spaces

def test_basic_string_conversion():
    """Test basic string conversion to uppercase."""
    assert convert_to_uppercase_with_spaces("hello") == "HELLO"

def test_camel_case_conversion():
    """Test conversion of camel case string."""
    assert convert_to_uppercase_with_spaces("helloWorld") == "HELLO WORLD"

def test_mixed_case_conversion():
    """Test conversion of mixed case string."""
    assert convert_to_uppercase_with_spaces("HelloWorld") == "HELLO WORLD"

def test_string_with_numbers():
    """Test conversion of string with numbers."""
    assert convert_to_uppercase_with_spaces("hello2World") == "HELLO 2 WORLD"

def test_already_uppercase():
    """Test conversion of already uppercase string."""
    assert convert_to_uppercase_with_spaces("HELLO") == "HELLO"

def test_empty_string():
    """Test conversion of empty string."""
    assert convert_to_uppercase_with_spaces("") == ""

def test_single_character():
    """Test conversion of single character."""
    assert convert_to_uppercase_with_spaces("a") == "A"

def test_multiple_uppercase_letters():
    """Test conversion with multiple consecutive uppercase letters."""
    assert convert_to_uppercase_with_spaces("HTMLParser") == "HTML PARSER"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase_with_spaces(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase_with_spaces(None)