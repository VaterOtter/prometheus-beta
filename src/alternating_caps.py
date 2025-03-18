def to_alternating_caps(text: str) -> str:
    """
    Convert a string to alternating caps case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: A string with alternating uppercase and lowercase characters.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_caps("hello")
        'HeLlO'
        >>> to_alternating_caps("python")
        'PyThOn'
        >>> to_alternating_caps("")
        ''
    """
    # Check for invalid input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return ""
    
    # Convert to alternating caps
    return ''.join(
        char.upper() if idx % 2 == 0 else char.lower() 
        for idx, char in enumerate(text)
    )