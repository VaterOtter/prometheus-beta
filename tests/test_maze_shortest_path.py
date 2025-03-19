import pytest
from src.maze_shortest_path import find_shortest_path

def test_simple_open_path():
    """Test a simple open path from top-left to bottom-right"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4

def test_path_with_obstacles():
    """Test a path that requires navigation around obstacles"""
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4

def test_no_path_exists():
    """Test when no path exists"""
    grid = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_start_blocked():
    """Test when start position is blocked"""
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_end_blocked():
    """Test when end position is blocked"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(grid) == -1

def test_large_grid():
    """Test a larger grid with a path"""
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    assert find_shortest_path(grid) == 6

def test_invalid_grid_empty():
    """Test handling of an empty grid"""
    with pytest.raises(ValueError, match="Grid cannot be empty"):
        find_shortest_path([])

def test_invalid_grid_not_square():
    """Test handling of a non-square grid"""
    with pytest.raises(ValueError, match="Grid must be a square NxN matrix"):
        find_shortest_path([
            [0, 0, 0],
            [0, 0]
        ])

def test_single_cell_grid():
    """Test a single cell grid where start is open"""
    grid = [[0]]
    assert find_shortest_path(grid) == 0

def test_single_cell_grid_blocked():
    """Test a single cell grid where start is blocked"""
    grid = [[1]]
    assert find_shortest_path(grid) == -1