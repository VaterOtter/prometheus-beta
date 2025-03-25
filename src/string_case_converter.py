def to_alternating_header_case(input_string: str) -> str:
    """
    Convert a string to alternating header case.
    
    This function takes a string and converts it to a case where 
    characters alternate between uppercase and lowercase, starting with uppercase.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating header case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_alternating_header_case("hello world")
        'HeLlO WoRlD'
        >>> to_alternating_header_case("python programming")
        'PyThOn PrOgRaMmInG'
    """
    # Validate input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to alternating case
    result = []
    for i, char in enumerate(input_string):
        # Even indices (0, 2, 4...) get uppercase, odd indices get lowercase
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)