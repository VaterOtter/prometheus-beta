import pytest
from src.kmp_search import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test basic LPS array computation
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    assert compute_lps_array("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps_array("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    assert compute_lps_array("") == []
    
    # Test error handling
    with pytest.raises(TypeError):
        compute_lps_array(None)
    with pytest.raises(TypeError):
        compute_lps_array(123)

def test_kmp_search_basic():
    # Basic pattern matching scenarios
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    assert kmp_search("ABABABCABABABCABABABC", "ABABAC") == []
    assert kmp_search("hello world", "o w") == [4]

def test_kmp_search_edge_cases():
    # Edge cases
    assert kmp_search("", "") == []  # empty everything
    assert kmp_search("abc", "") == []  # empty pattern
    assert kmp_search("", "abc") == []  # empty text
    
    # Single character matching
    assert kmp_search("aaaaa", "a") == [0, 1, 2, 3, 4]

def test_kmp_search_error_handling():
    # Type error cases
    with pytest.raises(TypeError):
        kmp_search(None, "abc")
    with pytest.raises(TypeError):
        kmp_search("abc", None)
    # No ValueError for empty string anymore
    assert kmp_search("abc", "") == []

def test_kmp_search_complex_patterns():
    # More complex pattern matching scenarios
    text = "AAAAABAAABA"
    pattern1 = "AAAA"
    assert kmp_search(text, pattern1) == [0, 1]
    
    text = "ABABDABACDABABCABAB"
    pattern2 = "ABABCABAB"
    assert kmp_search(text, pattern2) == [10]

def test_kmp_search_no_match():
    # Scenarios with no matches
    assert kmp_search("hello world", "xyz") == []
    assert kmp_search("abcdefg", "abcdefgh") == []

def test_kmp_search_case_sensitive():
    # Verify case sensitivity
    assert kmp_search("Hello World", "world") == []
    assert kmp_search("Hello World", "World") == [6]