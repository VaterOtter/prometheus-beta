def rotate_and_reverse(string: str, rotations: int) -> str:
    """
    Reverse the string first, then rotate it a specified number of times.
    
    Args:
        string (str): The input string to reverse and rotate.
        rotations (int): Number of times to rotate the reversed string.
    
    Returns:
        str: The reversed and rotated string.
    
    Raises:
        TypeError: If string is not a string or rotations is not an integer.
        ValueError: If rotations is negative.
    """
    # Type checking
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    if not isinstance(rotations, int):
        raise TypeError("Rotations must be an integer")
    
    # Handle negative rotations
    if rotations < 0:
        raise ValueError("Rotations cannot be negative")
    
    # Handle empty string or zero rotations
    if not string or rotations == 0:
        return string[::-1]
    
    # First reverse the string
    reversed_string = string[::-1]
    
    # Normalize rotations to be within string length
    effective_rotations = rotations % len(reversed_string)
    
    # Rotate the reversed string
    return reversed_string[effective_rotations:] + reversed_string[:effective_rotations]