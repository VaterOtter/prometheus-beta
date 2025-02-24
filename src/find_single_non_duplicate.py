def find_single_non_duplicate(arr):
    """
    Find the single element that appears only once in a sorted array where all other elements appear twice.
    
    Args:
        arr (list): A sorted array of integers where every element appears twice except one element.
    
    Returns:
        int: The single element that appears only once.
    
    Raises:
        ValueError: If the input array is empty or None.
        TypeError: If the input is not a list.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Input validation
    if arr is None:
        raise TypeError("Input cannot be None")
    
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    # If only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Binary search approach
    left, right = 0, len(arr) - 1
    
    # Handle edge cases at the beginning and end of the array
    if arr[0] != arr[1]:
        return arr[0]
    
    if arr[-1] != arr[-2]:
        return arr[-1]
    
    # Binary search for the single element
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if mid is the unique element
        if mid % 2 == 1:
            mid -= 1
        
        # If elements around mid are the same, the unique element is on the right side
        if arr[mid] == arr[mid + 1]:
            left = mid + 2
        # Otherwise, the unique element is on the left side or is mid
        else:
            right = mid
    
    return arr[left]