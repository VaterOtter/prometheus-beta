import pytest
from src.string_analyzer import count_vowels_consonants

def test_basic_string():
    """Test a basic string with mixed letters."""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_uppercase_string():
    """Test that the function works with uppercase letters."""
    result = count_vowels_consonants("WORLD")
    assert result == {'vowels': 1, 'consonants': 4}

def test_mixed_case_string():
    """Test a string with mixed case letters."""
    result = count_vowels_consonants("PyThOn")
    assert result == {'vowels': 1, 'consonants': 5}

def test_empty_string():
    """Test an empty string."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_non_alphabetic_string():
    """Test a string with non-alphabetic characters."""
    result = count_vowels_consonants("123!@#")
    assert result == {'vowels': 0, 'consonants': 0}

def test_mixed_alphanumeric_string():
    """Test a string with both letters and non-letters."""
    result = count_vowels_consonants("Hello123 World!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_input_type_error():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(None)

def test_all_vowels():
    """Test a string with only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_all_consonants():
    """Test a string with only consonants."""
    result = count_vowels_consonants("rhythm")
    assert result == {'vowels': 0, 'consonants': 6}