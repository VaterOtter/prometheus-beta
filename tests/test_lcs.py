import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic LCS functionality"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_string_cases():
    """Test LCS with empty strings"""
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("XYZ", "") == ""
    assert longest_common_subsequence("", "") == ""

def test_identical_strings():
    """Test LCS when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test LCS when no common subsequence exists"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_partial_match():
    """Test LCS with partial matches"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "ABC")

def test_case_sensitivity():
    """Test case sensitivity of LCS"""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_repeated_characters():
    """Test LCS with repeated characters"""
    assert longest_common_subsequence("AAAAAA", "AAAAAAA") == "AAAAAA"
    assert longest_common_subsequence("ABCCCDE", "BCCDE") == "BCCE"