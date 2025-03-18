import pytest
from src.alternating_caps import to_alternating_caps

def test_basic_conversion():
    """Test basic string conversion to alternating caps."""
    assert to_alternating_caps("hello") == "HeLlO"
    assert to_alternating_caps("python") == "PyThOn"
    assert to_alternating_caps("OpenAI") == "OpEnAi"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_caps("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert to_alternating_caps("a") == "A"
    assert to_alternating_caps("B") == "B"

def test_special_characters():
    """Test conversion with special characters and mixed inputs."""
    assert to_alternating_caps("hello world!") == "HeLlO WoRlD!"
    assert to_alternating_caps("123 abc") == "123 AbC"

def test_invalid_input():
    """Test that invalid inputs raise a TypeError."""
    with pytest.raises(TypeError):
        to_alternating_caps(123)
    
    with pytest.raises(TypeError):
        to_alternating_caps(None)

def test_unicode_characters():
    """Test conversion with unicode characters."""
    assert to_alternating_caps("café") == "CaFé"
    assert to_alternating_caps("наука") == "НаУкА"