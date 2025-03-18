import pytest
from src.longest_substring import find_longest_substring

def test_find_longest_substring_basic():
    """Test basic functionality of the function"""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_find_longest_substring_edge_cases():
    """Test edge cases"""
    # Empty string
    assert find_longest_substring("") == ""
    
    # Single character
    assert find_longest_substring("a") == "a"
    
    # All unique characters
    assert find_longest_substring("abcdef") == "abcdef"

def test_find_longest_substring_case_sensitivity():
    """Verify case-sensitive behavior"""
    assert find_longest_substring("AbcA") == "Abc"
    assert find_longest_substring("aA") == "aA"

def test_find_longest_substring_complex_cases():
    """Test more complex scenarios"""
    # Repeated patterns
    assert find_longest_substring("dvdf") == "vdf"
    
    # Mix of repeated and unique characters
    assert find_longest_substring("tmmzuxt") == "mzuxt"

def test_find_longest_substring_performance():
    """Ensure function works with longer strings"""
    long_string = "abcdefghijklmnopqrstuvwxyz" * 10
    result = find_longest_substring(long_string)
    assert len(result) == 26  # All unique characters in alphabet
    assert result == "abcdefghijklmnopqrstuvwxyz"