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
    
    # Create a list of beads to simulate gravity
    beads = [0] * len(arr)
    max_val = max(arr)
    
    # Simulate bead sort
    for val in arr:
        for j in range(val):
            beads[j] += 1
    
    # Reconstruct sorted array
    sorted_arr = []
    for i in range(len(beads)):
        sorted_arr.extend([i] * beads[i])
    
    return sorted_arr