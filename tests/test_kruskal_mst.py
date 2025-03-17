import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_basic():
    """Test basic functionality of DisjointSet."""
    ds = DisjointSet(5)
    
    # Initially, each element should be in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union should connect sets
    assert ds.union(0, 1) == True
    assert ds.find(0) == ds.find(1)
    
    # Second union of same elements should return False
    assert ds.union(0, 1) == False

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple connected graph."""
    # Graph with 3 vertices
    graph = [
        (1, 0, 1),  # weight, vertex1, vertex2
        (2, 1, 2),
        (3, 0, 2)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST should have 2 edges with minimum total weight
    assert len(mst) == 2
    assert sorted(mst) == [(1, 0, 1), (2, 1, 2)]

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm on a graph with multiple components."""
    graph = [
        (1, 0, 1),
        (2, 1, 2),
        (3, 0, 2),
        (4, 3, 4),
        (5, 4, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST should have n-1 edges 
    assert len(mst) == 4  # Correct number of edges for 6 vertices

def test_kruskal_mst_empty_graph():
    """Test error handling for empty graph."""
    with pytest.raises(ValueError):
        kruskal_mst([])

def test_kruskal_mst_single_vertex_graph():
    """Test handling of a single vertex graph."""
    graph = [(0, 0, 0)]
    
    with pytest.raises(ValueError):
        kruskal_mst(graph)

def test_kruskal_mst_complex_graph():
    """Test Kruskal's algorithm on a more complex graph."""
    graph = [
        (1, 0, 1),
        (2, 1, 2),
        (3, 0, 2),
        (4, 1, 3),
        (5, 2, 3),
        (6, 3, 4)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected minimum total weight will be slightly different
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 10  # 1 + 2 + 4 + 3
    assert len(mst) == 4  # Number of vertices - 1