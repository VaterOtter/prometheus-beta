import pytest
from src.matrix_search import search_matrix

def test_search_matrix_basic():
    """Test basic matrix search functionality"""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False

def test_search_matrix_edge_cases():
    """Test edge cases for matrix search"""
    # Single row matrix
    single_row = [[1, 3, 5]]
    assert search_matrix(single_row, 3) == True
    assert search_matrix(single_row, 4) == False

    # Single column matrix
    single_col = [[1], [3], [5]]
    assert search_matrix(single_col, 3) == True
    assert search_matrix(single_col, 4) == False

def test_search_matrix_boundary_values():
    """Test boundary values in the matrix"""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 1) == True  # First element
    assert search_matrix(matrix, 60) == True  # Last element
    assert search_matrix(matrix, 0) == False  # Below first element
    assert search_matrix(matrix, 61) == False  # Above last element

def test_search_matrix_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        search_matrix([], 5)
    
    with pytest.raises(ValueError):
        search_matrix([[]], 5)

def test_search_matrix_large_matrix():
    """Test search in a larger matrix"""
    large_matrix = [
        [i * 10 + j for j in range(10)] 
        for i in range(20)
    ]
    assert search_matrix(large_matrix, 42) == True
    assert search_matrix(large_matrix, 199) == True
    assert search_matrix(large_matrix, 201) == False