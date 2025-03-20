def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a contiguous subarray of length k in the given array.

    Args:
        arr (list): A list of integers to search for the maximum subarray sum.
        k (int): The length of the subarray.

    Returns:
        int: The maximum sum of any contiguous subarray of length k.

    Raises:
        ValueError: If the array is None, empty, or k is invalid.
    """
    # Validate input
    if arr is None:
        raise ValueError("Input array cannot be None")
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if k <= 0:
        raise ValueError("Subarray length k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("Subarray length k cannot be larger than array length")
    
    # Use sliding window technique
    # Initialize the sum of first k elements
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window and update max sum
    for i in range(k, len(arr)):
        # Remove the first element of previous window and add the next element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum