import pytest
from src.sponge_case import to_sponge_case

def test_to_sponge_case_normal_string():
    """Test conversion of a normal string."""
    assert to_sponge_case("hello") == "hElLo"
    assert to_sponge_case("world") == "wOrLd"

def test_to_sponge_case_uppercase():
    """Test conversion of an uppercase string."""
    assert to_sponge_case("HELLO") == "HeLlO"

def test_to_sponge_case_mixed_case():
    """Test conversion of a mixed case string."""
    assert to_sponge_case("HeLLo") == "hElLo"

def test_to_sponge_case_empty_string():
    """Test conversion of an empty string."""
    assert to_sponge_case("") == ""

def test_to_sponge_case_spaces():
    """Test conversion of a string with spaces."""
    assert to_sponge_case("hello world") == "hElLo WoRlD"

def test_to_sponge_case_non_alphabetic():
    """Test conversion of a string with non-alphabetic characters."""
    assert to_sponge_case("123abc") == "1AbC"

def test_to_sponge_case_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(None)