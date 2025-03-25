def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for a target integer in a T x R matrix of unique integers.
    
    Args:
        matrix (list[list[int]]): A 2D matrix of integers where each row is sorted in ascending order
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if the target is found in the matrix, False otherwise
    
    Time Complexity: O(log(T*R)) - efficient search leveraging matrix properties
    Space Complexity: O(1) - constant extra space
    
    Raises:
        ValueError: If the input matrix is empty or None
    """
    # Check for invalid input
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Get matrix dimensions
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Perform binary search on the flattened matrix
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D coordinates
        row = mid // cols
        col = mid % cols
        
        # Get the value at current position
        current = matrix[row][col]
        
        # Compare and adjust search space
        if current == target:
            return True
        elif current < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False