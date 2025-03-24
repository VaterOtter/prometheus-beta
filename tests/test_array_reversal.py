import pytest
from src.array_reversal import reverse_array

def test_reverse_array_integers():
    """Test reversing an array of integers."""
    input_array = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_array(input_array) == expected

def test_reverse_array_strings():
    """Test reversing an array of strings."""
    input_array = ['apple', 'banana', 'cherry']
    expected = ['cherry', 'banana', 'apple']
    assert reverse_array(input_array) == expected

def test_reverse_array_mixed_types():
    """Test reversing an array with mixed types."""
    input_array = [1, 'two', 3.0, True]
    expected = [True, 3.0, 'two', 1]
    assert reverse_array(input_array) == expected

def test_reverse_empty_array():
    """Test reversing an empty array."""
    input_array = []
    expected = []
    assert reverse_array(input_array) == expected

def test_reverse_single_element_array():
    """Test reversing an array with a single element."""
    input_array = [42]
    expected = [42]
    assert reverse_array(input_array) == expected

def test_reverse_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(None)