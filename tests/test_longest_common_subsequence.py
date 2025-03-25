import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("test", "") == ""
    assert longest_common_subsequence("", "test") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_partial_match():
    """Test partial matches"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""

def test_single_character():
    """Test single character scenarios"""
    assert longest_common_subsequence("a", "a") == "a"
    assert longest_common_subsequence("a", "b") == ""

def test_long_strings():
    """Test longer string scenarios"""
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert longest_common_subsequence(str1, str2) == str1

    str3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str4 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    assert longest_common_subsequence(str3, str4) == ""