from typing import List, Tuple
from collections import deque

def find_shortest_path(grid: List[List[int]]) -> int:
    """
    Find the shortest path length in a 2D grid maze from top-left to bottom-right.
    
    Args:
        grid (List[List[int]]): A 2D grid where 0 represents open paths and 1 represents walls.
                                Grid is NxN, with start at grid[0][0] and end at grid[N-1][N-1].
    
    Returns:
        int: Length of the shortest path from top-left to bottom-right, 
             or -1 if no path exists.
    
    Raises:
        ValueError: If the grid is empty or not a square grid.
    """
    # Validate input
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    n = len(grid)
    
    # Check if grid is square and valid
    if any(len(row) != n for row in grid):
        raise ValueError("Grid must be a square NxN matrix")
    
    # Check start and end are open
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Possible moves: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Track visited cells and initialize queue with start position
    visited = [[False] * n for _ in range(n)]
    queue = deque([(0, 0, 0)])  # (row, col, path_length)
    visited[0][0] = True
    
    while queue:
        curr_row, curr_col, path_length = queue.popleft()
        
        # Check if reached bottom-right
        if curr_row == n - 1 and curr_col == n - 1:
            return path_length
        
        # Try all 4 directions
        for dx, dy in directions:
            next_row, next_col = curr_row + dx, curr_col + dy
            
            # Check if next position is valid
            if (0 <= next_row < n and 
                0 <= next_col < n and 
                grid[next_row][next_col] == 0 and 
                not visited[next_row][next_col]):
                
                queue.append((next_row, next_col, path_length + 1))
                visited[next_row][next_col] = True
    
    # No path found
    return -1