import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_assignment():
    """Test a simple 3x3 cost matrix."""
    cost_matrix = [
        [7, 5, 3],
        [2, 4, 6],
        [4, 7, 8]
    ]
    assignment, total_cost = hungarian_algorithm(cost_matrix)
    
    # Validate assignment uniqueness
    assert len(set(zip(*assignment)[1])) == len(assignment), "Each task should be assigned only once"
    assert len(set(zip(*assignment)[0])) == len(assignment), "Each worker should be assigned only once"
    
    # Validate total cost (you might need to adjust this depending on the optimal assignment)
    expected_assignment = [(0, 2), (1, 0), (2, 1)]
    expected_total_cost = 3 + 2 + 7  # Cost of optimal assignment
    
    assert sorted(assignment) == sorted(expected_assignment), "Incorrect assignment"
    
def test_identical_rows():
    """Test matrix with identical rows."""
    cost_matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assignment, total_cost = hungarian_algorithm(cost_matrix)
    
    assert len(assignment) == 3, "All workers should be assigned"
    assert total_cost == 3, "Total cost should be 3"

def test_large_matrix():
    """Test a larger 4x4 matrix."""
    cost_matrix = [
        [13, 16, 14, 85],
        [32, 45, 22, 71],
        [54, 33, 12, 44],
        [11, 66, 23, 77]
    ]
    assignment, total_cost = hungarian_algorithm(cost_matrix)
    
    # Validate assignment
    assert len(assignment) == 4, "All workers should be assigned"
    assert len(set(zip(*assignment)[1])) == 4, "Each task should be unique"
    assert len(set(zip(*assignment)[0])) == 4, "Each worker should be unique"

def test_invalid_input():
    """Test error handling for invalid inputs."""
    # Non-square matrix
    with pytest.raises(ValueError, match="square matrix"):
        hungarian_algorithm([[1, 2], [3, 4], [5, 6]])
    
    # Non-numeric input
    with pytest.raises(ValueError, match="valid matrix of numbers"):
        hungarian_algorithm([['a', 'b'], ['c', 'd']])
    
    # Empty matrix
    with pytest.raises(ValueError):
        hungarian_algorithm([])

def test_single_element_matrix():
    """Test a 1x1 matrix."""
    cost_matrix = [[42]]
    assignment, total_cost = hungarian_algorithm(cost_matrix)
    
    assert assignment == [(0, 0)], "Single element matrix assignment incorrect"
    assert total_cost == 0, "Total cost should be 0 for single element matrix"

def test_numpy_input():
    """Test input as NumPy array."""
    cost_matrix = np.array([
        [7, 5, 3],
        [2, 4, 6],
        [4, 7, 8]
    ])
    assignment, total_cost = hungarian_algorithm(cost_matrix)
    
    assert len(assignment) == 3, "All workers should be assigned"