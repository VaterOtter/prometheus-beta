import re

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
    
    # Use regex to insert spaces before uppercase letters and digits
    # First, handle consecutive uppercase letters
    s1 = re.sub(r'([A-Z])([A-Z][a-z])', r'\1 \2', input_string)
    
    # Then insert space before uppercase letters or numbers
    s2 = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', s1)
    
    # Convert to uppercase
    return s2.upper()