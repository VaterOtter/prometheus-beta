import sys
from typing import List, Optional, Union

def floyd_warshall(graph: List[List[Union[int, float]]]) -> Optional[List[List[Union[int, float]]]]:
    """
    Implements the Floyd-Warshall algorithm to find shortest paths between all pairs of nodes.
    
    Args:
        graph (List[List[Union[int, float]]]): Adjacency matrix representing the graph.
                Expects graph[i][j] to be the weight of edge from node i to node j.
                Use sys.maxsize or float('inf') for non-existent edges.
    
    Returns:
        Optional[List[List[Union[int, float]]]]: Distance matrix with shortest paths between all nodes,
        or None if the graph contains a negative cycle.
    
    Raises:
        ValueError: If input graph is not a square matrix or is empty.
    """
    # Input validation
    if not graph or len(graph) == 0:
        raise ValueError("Graph cannot be empty")
    
    # Check if graph is a square matrix
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("Graph must be a square matrix")
    
    # Create a copy of the input graph to avoid modifying the original
    dist = [row.copy() for row in graph]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Check if path through k is shorter
                if (dist[i][k] != sys.maxsize and 
                    dist[k][j] != sys.maxsize and 
                    dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            return None
    
    return dist