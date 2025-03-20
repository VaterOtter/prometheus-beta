def replace_words(text: str, replacements: dict) -> str:
    """
    Perform in-place text replacements using a dictionary of word replacements.

    Args:
        text (str): The input text to perform replacements on.
        replacements (dict): A dictionary where keys are words to be replaced 
                             and values are their replacements.

    Returns:
        str: The text with all specified replacements made.

    Raises:
        TypeError: If input text is not a string or replacements is not a dictionary.
        ValueError: If any replacement key or value is not a non-empty string.
    """
    # Validate input types
    if not isinstance(text, str):
        raise TypeError("Input text must be a string")
    
    if not isinstance(replacements, dict):
        raise TypeError("Replacements must be a dictionary")
    
    # Validate replacement dictionary
    for key, value in replacements.items():
        if not isinstance(key, str) or not key:
            raise ValueError("Replacement keys must be non-empty strings")
        if not isinstance(value, str):
            raise ValueError("Replacement values must be strings")
    
    # Perform replacements
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    
    return text