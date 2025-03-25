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
    
    # Find the maximum number to determine the number of rows
    max_num = max(arr) if arr else 0
    
    # Create abacus-like representation
    abacus = [[1 if x > row else 0 for x in arr] for row in range(max_num)]
    
    # Let beads "fall"
    for row in range(max_num):
        # Count beads in each column
        column_counts = [sum(abacus[r][col] for r in range(max_num)) for col in range(len(arr))]
        
        # Reset the abacus row
        abacus[row] = [1 if column_counts[col] > row else 0 for col in range(len(arr))]
    
    # Reconstruct the sorted array
    sorted_arr = [
        sum(abacus[row][col] for row in range(max_num)) 
        for col in range(len(arr))
    ]
    
    return sorted_arr