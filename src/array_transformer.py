def transform_array(input_array):
    """
    Transform an array of non-negative integers based on specific rules:
    - 0 remains 0
    - Non-zero elements are transformed to their square plus 1

    Args:
        input_array (list): A list of non-negative integers

    Returns:
        list: A new list with transformed elements

    Raises:
        TypeError: If input is not a list
        ValueError: If any element is negative
    """
    # Validate input is a list
    if not isinstance(input_array, list):
        raise TypeError("Input must be a list")
    
    # Check for negative numbers
    if any(num < 0 for num in input_array):
        raise ValueError("All input numbers must be non-negative")
    
    # Transform the array
    return [0 if num == 0 else num**2 + 1 for num in input_array]