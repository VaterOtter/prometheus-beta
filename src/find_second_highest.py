def find_second_highest(sorted_list):
    """
    Find the second highest value in a sorted list of integers.

    Args:
        sorted_list (list): A sorted list of integers in ascending or descending order.

    Returns:
        int or None: The second highest value in the list, or None if the list 
        does not have at least two unique values.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty.
    """
    # Check for input validation
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if len(sorted_list) == 0:
        raise ValueError("List cannot be empty")
    
    # Remove duplicates while preserving order
    unique_values = list(dict.fromkeys(sorted_list))
    
    # Check if there are at least two unique values
    if len(unique_values) < 2:
        return None
    
    # Return the second highest value
    return unique_values[-2]