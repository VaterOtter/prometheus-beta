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
    
    # Convert to alternating case
    return ''.join(
        char.upper() if i % 2 == 1 else char.lower() 
        for i, char in enumerate(text)
    )