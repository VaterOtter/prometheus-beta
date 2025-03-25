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
    abacus = [[1 if num > row else 0 for num in arr] for row in range(max_num + 1)]
    
    # Let beads "fall"
    sorted_arr = []
    for col in range(len(arr)):
        # Count beads in this column
        bead_count = sum(abacus[row][col] for row in range(max_num + 1))
        # Add the number of beads as multiple elements
        sorted_arr.extend([col] * bead_count)
    
    return sorted_arr