import pytest
from src.vowel_consonant_counter import count_vowels_consonants

def test_basic_counting():
    """Test basic vowel and consonant counting."""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_mixed_case():
    """Test that function works with mixed case input."""
    result = count_vowels_consonants("HeLLo")
    assert result == {'vowels': 2, 'consonants': 3}

def test_string_with_spaces():
    """Test counting in a string with spaces."""
    result = count_vowels_consonants("hello world")
    assert result == {'vowels': 3, 'consonants': 7}

def test_string_with_punctuation():
    """Test counting in a string with punctuation."""
    result = count_vowels_consonants("hello, world!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test counting in an empty string."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    """Test a string with only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test a string with only consonants."""
    result = count_vowels_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_non_string_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)

def test_special_characters():
    """Test handling of special characters."""
    result = count_vowels_consonants("hello@123")
    assert result == {'vowels': 2, 'consonants': 3}