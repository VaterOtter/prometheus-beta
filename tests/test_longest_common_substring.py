import pytest
from src.longest_common_substring import longest_common_substring

def test_basic_common_substring():
    assert longest_common_substring("programming", "programmer") == "program"
    assert longest_common_substring("hello", "world") == ""

def test_edge_cases():
    # Empty strings
    assert longest_common_substring("", "") == ""
    assert longest_common_substring("test", "") == ""
    assert longest_common_substring("", "test") == ""

def test_identical_strings():
    assert longest_common_substring("hello", "hello") == "hello"

def test_partial_matches():
    assert longest_common_substring("abcdef", "bcdefg") == "bcdef"
    assert longest_common_substring("ababc", "abc") == "abc"

def test_case_sensitivity():
    assert longest_common_substring("Hello", "hello") == ""

def test_multiple_possible_substrings():
    result = longest_common_substring("abab", "baba")
    assert result in ["ab", "ba"]

def test_long_strings():
    str1 = "x" * 1000 + "abcdef" + "y" * 1000
    str2 = "z" * 1500 + "abcdef" + "w" * 1500
    assert longest_common_substring(str1, str2) == "abcdef"

def test_type_hints():
    # Verify type hints and potential type conversion
    with pytest.raises(TypeError):
        longest_common_substring(123, "test")
    with pytest.raises(TypeError):
        longest_common_substring("test", 456)