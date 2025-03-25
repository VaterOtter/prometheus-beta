def to_alternating_header_case(input_string: str) -> str:
    """
    Convert a string to alternating header case.
    
    This function takes a string and converts it to a case where 
    characters alternate between uppercase and lowercase within each word, 
    starting with uppercase. Non-alphabetic characters remain unchanged.
    
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
    
    # Process by word to handle spaces and special characters correctly
    words = input_string.split(' ')
    converted_words = []
    
    for word in words:
        # Convert each word while preserving non-alphabetic characters
        converted_word = []
        for i, char in enumerate(word):
            # Even indices (0, 2, 4...) get uppercase, odd indices get lowercase
            if char.isalpha():
                converted_word.append(char.upper() if i % 2 == 0 else char.lower())
            else:
                converted_word.append(char)
        
        converted_words.append(''.join(converted_word))
    
    return ' '.join(converted_words)