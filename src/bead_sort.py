def bead_sort(arr):
    """
    Implement the bead sort algorithm for sorting positive integers.
    
    Bead sort (or gravity sort) is a natural sorting algorithm that works 
    by simulating a physical model of beads falling under gravity.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # If list is empty or has only one element, return as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Find maximum value to determine number of "rows"
    max_val = max(arr)
    
    # Create a board representing bead positions
    board = [[1 if x > i else 0 for x in arr] for i in range(max_val)]
    
    # Simulate dropping beads
    sorted_arr = []
    for col in range(len(arr)):
        # Count number of beads in each column
        bead_count = sum(board[row][col] for row in range(max_val))
        sorted_arr.extend([col] * bead_count)
    
    return sorted_arr