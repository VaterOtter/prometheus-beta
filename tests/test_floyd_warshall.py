import sys
import pytest
import math
from src.floyd_warshall import floyd_warshall

def test_basic_graph():
    """Test a simple connected graph"""
    graph = [
        [0, 5, sys.maxsize, 10],
        [sys.maxsize, 0, 3, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0, 1],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]
    expected_dist = [
        [0, 5, 8, 9],
        [sys.maxsize, 0, 3, 4],
        [sys.maxsize, sys.maxsize, 0, 1],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected_dist

def test_disconnected_graph():
    """Test a graph with disconnected nodes"""
    graph = [
        [0, 5, sys.maxsize],
        [sys.maxsize, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0]
    ]
    expected_dist = [
        [0, 5, sys.maxsize],
        [sys.maxsize, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected_dist

def test_negative_edges():
    """Test graph with negative edges (no negative cycles)"""
    graph = [
        [0, -1, 4],
        [sys.maxsize, 0, 3],
        [sys.maxsize, sys.maxsize, 0]
    ]
    expected_dist = [
        [0, -1, 2],
        [sys.maxsize, 0, 3],
        [sys.maxsize, sys.maxsize, 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected_dist

def test_single_node_graph():
    """Test graph with single node"""
    graph = [[0]]
    result = floyd_warshall(graph)
    assert result == [[0]]

def test_empty_graph_raises_error():
    """Test that empty graph raises ValueError"""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        floyd_warshall([])

def test_non_square_matrix_raises_error():
    """Test that non-square matrix raises ValueError"""
    with pytest.raises(ValueError, match="Graph must be a square matrix"):
        floyd_warshall([
            [0, 1, 2],
            [3, 4]
        ])

def test_large_distance_values():
    """Test graph with large distance values"""
    graph = [
        [0, 1000000, sys.maxsize],
        [sys.maxsize, 0, 500000],
        [sys.maxsize, sys.maxsize, 0]
    ]
    result = floyd_warshall(graph)
    assert result[0][2] == 1500000

def test_floating_point_distances():
    """Test graph with floating point distances"""
    graph = [
        [0.0, 1.5, sys.maxsize],
        [sys.maxsize, 0.0, 2.7],
        [sys.maxsize, sys.maxsize, 0.0]
    ]
    result = floyd_warshall(graph)
    assert math.isclose(result[0][2], 4.2, rel_tol=1e-9)