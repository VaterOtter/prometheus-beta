def convert_to_uppercase_with_spaces(input_string):
    """
    Convert a given string to uppercase with spaces.

    This function takes a string and returns a version of the string 
    where:
    - All characters are converted to uppercase
    - Additional spaces are added between words or camel case characters

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The converted string in uppercase with added spaces.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If empty string, return empty string
    if not input_string:
        return ""
    
    # Initialize result with the first character
    result = [input_string[0].upper()]
    
    # Iterate through the rest of the characters
    for char in input_string[1:]:
        # Add space before uppercase letters or numbers, 
        # except when previous character was uppercase or a digit
        if (char.isupper() and not result[-1].isupper()) or \
           (char.isdigit() and result[-1].isalpha() and not result[-1].isupper()):
            result.append(' ')
        
        # Add the current character in uppercase
        result.append(char.upper())
    
    return ''.join(result)