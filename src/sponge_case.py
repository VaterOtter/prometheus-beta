def to_sponge_case(text: str) -> str:
    """
    Convert a string to alternating SpOnGe CaSe.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The input string converted to alternating case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_sponge_case("hello")
        'hElLo'
        >>> to_sponge_case("WORLD")
        'WoRlD'
        >>> to_sponge_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not text:
        return ""
    
    # Convert to alternating case, tracking alphabet-only index
    result = []
    alpha_index = 0
    for char in text:
        if char.isalpha():
            # Apply alternating case for alphabetic characters
            result.append(char.upper() if alpha_index % 2 == 1 else char.lower())
            alpha_index += 1
        else:
            # Preserve non-alphabetic characters as-is
            result.append(char)
    
    return ''.join(result)