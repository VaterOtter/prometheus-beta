def convert_to_dot_case(input_string):
    """
    Convert a given string to dot case.
    
    Dot case is a string formatting where:
    - All characters are lowercase
    - Words are separated by dots
    - Handles various input formats (camelCase, snake_case, PascalCase, etc.)
    
    Args:
        input_string (str): The input string to convert to dot case
    
    Returns:
        str: The string converted to dot case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> convert_to_dot_case("HelloWorld")
        'hello.world'
        >>> convert_to_dot_case("hello_world")
        'hello.world'
        >>> convert_to_dot_case("helloWorld")
        'hello.world'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Normalize the string by replacing common separators with a temporary marker
    normalized = input_string.replace('_', ' ').replace('-', ' ')
    
    # Add spaces before capital letters for camelCase and PascalCase
    result = []
    for i, char in enumerate(normalized):
        if i > 0 and char.isupper():
            result.append(' ')
        result.append(char.lower())
    
    # Convert spaces to dots and remove extra whitespace
    return '.'.join(''.join(result).split())