import pytest
from src.strand_sort import strand_sort

def test_empty_list():
    """Test sorting an empty list"""
    assert strand_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert strand_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert strand_sort(input_list) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test sorting a list in descending order"""
    input_list = [5, 4, 3, 2, 1]
    assert strand_sort(input_list) == [1, 2, 3, 4, 5]

def test_random_unsorted_list():
    """Test sorting a random unsorted list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert strand_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert strand_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-4, 1, -9, 0, 5, -1]
    assert strand_sort(input_list) == [-9, -4, -1, 0, 1, 5]

def test_type_error():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        strand_sort("not a list")
        strand_sort(123)
        strand_sort(None)

def test_input_not_modified():
    """Test that the original input list is not modified"""
    input_list = [5, 2, 9, 1, 7]
    original_copy = input_list.copy()
    strand_sort(input_list)
    assert input_list == original_copy