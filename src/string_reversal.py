def reverse_string_in_place(s: str) -> str:
    """
    Reverse a string in-place without using extra memory.
    
    This function takes a string and returns a reversed version by modifying 
    the input string in-place. It works by swapping characters from the 
    beginning and end of the string until the middle is reached.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list of characters (strings are immutable in Python)
    chars = list(s)
    
    # Two-pointer approach to reverse in-place
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers towards center
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)