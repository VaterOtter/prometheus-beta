import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios."""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_edge_cases():
    """Test edge cases like empty strings."""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_identical_strings():
    """Test when strings are identical."""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test strings with no common subsequence."""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_partial_common_subsequence():
    """Test strings with partial common subsequence."""
    result = longest_common_subsequence("ABCBDAB", "BDCABA")
    # There might be multiple valid longest common subsequences
    assert result in ["BCBA", "BDAB"]

def test_case_sensitivity():
    """Test case sensitivity."""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("HELLO", "hello") == ""
    assert longest_common_subsequence("hello", "HELLO") == ""

def test_long_strings():
    """Test longer strings."""
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert longest_common_subsequence(str1, str2) == str1

def test_input_types():
    """Test input type handling."""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", 456)