def k_largest(arr, k):
    """
    Returns the k largest elements from the input array.

    Args:
        arr (list): A list of integers to find the k largest elements from.
        k (int): The number of largest elements to return.

    Returns:
        list: A list of the k largest elements in descending order.

    Raises:
        ValueError: If k is negative or greater than the length of the array.
        TypeError: If inputs are not of the correct type.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Check if k is valid
    if k < 0:
        raise ValueError("k cannot be negative")
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # Special case for empty array or k = 0
    if not arr or k == 0:
        return []
    
    # Sort the array in descending order and return the first k elements
    return sorted(arr, reverse=True)[:k]