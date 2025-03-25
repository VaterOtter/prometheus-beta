import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_of_medians import select_kth_smallest

def test_basic_selection():
    """Test basic selection of kth smallest element"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert select_kth_smallest(arr, 1) == 1  # Smallest element
    assert select_kth_smallest(arr, len(arr)) == 9  # Largest element
    
    # Median depends on whether the array is sorted or not
    median_index = (len(arr)+1)//2
    median = select_kth_smallest(arr, median_index)
    # Verify that median is a valid median value
    assert sorted(arr)[median_index-1] == median

def test_sorted_array():
    """Test selection in a sorted array"""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert select_kth_smallest(arr, 5) == 5
    assert select_kth_smallest(arr, 1) == 1
    assert select_kth_smallest(arr, 9) == 9

def test_reverse_sorted_array():
    """Test selection in a reverse sorted array"""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert select_kth_smallest(arr, 5) == 5
    assert select_kth_smallest(arr, 1) == 1
    assert select_kth_smallest(arr, 9) == 9

def test_array_with_duplicates():
    """Test selection in an array with duplicate values"""
    arr = [3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert select_kth_smallest(arr, 1) == 3
    assert select_kth_smallest(arr, len(arr)) == 3

def test_error_handling():
    """Test error cases"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        select_kth_smallest([], 1)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        select_kth_smallest([1, 2, 3], 0)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        select_kth_smallest([1, 2, 3], 4)

def test_random_arrays():
    """Test selection with randomly generated arrays"""
    import random
    
    # Test multiple random arrays
    for _ in range(10):
        arr = [random.randint(1, 1000) for _ in range(100)]
        k = random.randint(1, len(arr))
        
        # Compare with sorted method
        assert select_kth_smallest(arr, k) == sorted(arr)[k-1]

def test_small_arrays():
    """Test selection in very small arrays"""
    arr = [5]
    assert select_kth_smallest(arr, 1) == 5
    
    arr = [2, 1]
    assert select_kth_smallest(arr, 1) == 1
    assert select_kth_smallest(arr, 2) == 2