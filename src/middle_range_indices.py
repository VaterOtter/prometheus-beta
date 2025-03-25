def find_middle_range_indices(sorted_list, range_size):
    """
    Find indices of elements within a given range of the middle value in a sorted list.

    Args:
        sorted_list (list): A sorted list of integers.
        range_size (int): The number of indices to return on each side of the middle.

    Returns:
        list: Indices of elements within the specified range of the middle value.

    Raises:
        ValueError: If the input list is empty or range_size is negative.
        TypeError: If inputs are not of the expected type.
    """
    # Input validation
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(range_size, int):
        raise TypeError("Range size must be an integer")
    
    if range_size < 0:
        raise ValueError("Range size cannot be negative")
    
    # Handle empty list
    if not sorted_list:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the middle index for both odd and even length lists
    if len(sorted_list) % 2 == 1:
        # Odd length: use integer division to get exact middle
        mid_index = len(sorted_list) // 2
    else:
        # Even length: use the left-of-center middle index
        mid_index = (len(sorted_list) // 2) - 1
    
    # Calculate the start and end indices for the range
    start_index = max(0, mid_index - range_size)
    end_index = min(len(sorted_list) - 1, mid_index + range_size)
    
    # Return the indices within the range
    return list(range(start_index, end_index + 1))