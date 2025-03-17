class DisjointSet:
    """
    A Disjoint Set data structure (Union-Find) to support Kruskal's algorithm.
    
    This class helps efficiently determine whether adding an edge would create a cycle
    in the graph during Minimum Spanning Tree construction.
    """
    def __init__(self, vertices):
        """
        Initialize the Disjoint Set with each vertex in its own set.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item):
        """
        Find the root/representative of a set with path compression.
        
        Args:
            item (int): Vertex to find the set for
        
        Returns:
            int: Root/representative of the set
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        """
        Union two sets by rank to keep the tree balanced.
        
        Args:
            x (int): First vertex
            y (int): Second vertex
        
        Returns:
            bool: True if union was successful (no cycle), False otherwise
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(graph):
    """
    Find the Minimum Spanning Tree using Kruskal's Algorithm.
    
    Args:
        graph (list of tuples): Edges of the graph in format 
                                [(weight, vertex1, vertex2), ...]
    
    Returns:
        list of tuples: Edges in the Minimum Spanning Tree
    
    Raises:
        ValueError: If the graph is empty or None
    """
    # Validate input
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Get number of vertices
    vertices = max(max(edge[1], edge[2]) for edge in graph) + 1
    
    # Sort edges by weight
    edges = sorted(graph)
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)
    
    # Minimum Spanning Tree
    mst = []
    
    # Process edges
    for weight, u, v in edges:
        # If including this edge doesn't cause a cycle, add it to MST
        if disjoint_set.union(u, v):
            mst.append((weight, u, v))
    
    return mst