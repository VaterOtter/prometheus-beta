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
    
    # Remove duplicates while preserving the order of the original list
    unique_values = []
    seen = set()
    for value in sorted_list:
        if value not in seen:
            unique_values.append(value)
            seen.add(value)
    
    # Check if there are at least two unique values
    if len(unique_values) < 2:
        return None
    
    # Determine the order and return the second highest
    if unique_values[0] < unique_values[-1]:
        # Ascending order
        return unique_values[-2]
    else:
        # Descending order
        return unique_values[1]