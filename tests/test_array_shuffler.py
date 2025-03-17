import pytest
import random
from src.array_shuffler import shuffle_array

def test_shuffle_array_basic():
    """Test basic shuffling of an array."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Ensure shuffled array has same elements as original
    assert sorted(shuffled) == sorted(original)
    # Ensure array is not identical to original (with high probability)
    assert shuffled != original

def test_shuffle_array_empty():
    """Test shuffling an empty array."""
    assert shuffle_array([]) == []

def test_shuffle_array_single_element():
    """Test shuffling an array with a single element."""
    element = [42]
    assert shuffle_array(element) == element

def test_shuffle_array_type_variety():
    """Test shuffling an array with mixed types."""
    original = [1, 'a', True, 3.14, [1, 2]]
    shuffled = shuffle_array(original)
    
    # Ensure shuffled array has same elements as original
    assert sorted(shuffled, key=str) == sorted(original, key=str)

def test_shuffle_array_randomness():
    """Test the statistical randomness of the shuffle."""
    original = list(range(10))
    
    # Track different shuffle outcomes
    results = set()
    for _ in range(50):  # Multiple shuffle attempts
        results.add(tuple(shuffle_array(original)))
    
    # With high probability, most shuffles will be different
    assert len(results) > 1

def test_shuffle_array_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError):
        shuffle_array(123)
    
    with pytest.raises(TypeError):
        shuffle_array(None)

def test_shuffle_array_preserves_original():
    """Ensure the original array is not modified."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    assert original == [1, 2, 3, 4, 5], "Original array should not be modified"