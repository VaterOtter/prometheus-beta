import pytest
from src.string_case_converter import to_alternating_header_case

def test_basic_string_conversion():
    """Test basic string conversion to alternating header case."""
    assert to_alternating_header_case("hello world") == "HeLlO WoRlD"
    assert to_alternating_header_case("python programming") == "PyThOn PrOgRaMmInG"

def test_single_word():
    """Test conversion of a single word."""
    assert to_alternating_header_case("python") == "PyThOn"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_header_case("") == ""

def test_string_with_numbers():
    """Test conversion of a string with numbers."""
    assert to_alternating_header_case("hello 123 world") == "HeLlO 123 WoRlD"

def test_string_with_special_characters():
    """Test conversion of a string with special characters."""
    assert to_alternating_header_case("hello! world?") == "HeLlO! WoRlD?"

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_header_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_header_case(None)

def test_mixed_case_input():
    """Test conversion of a string with mixed case input."""
    assert to_alternating_header_case("MiXeD CaSe InPuT") == "MiXeD CaSe InPuT"