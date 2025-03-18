def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    Args:
        pattern (str): The pattern string to compute LPS for.
    
    Returns:
        list: The LPS array for the given pattern.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input
    if not isinstance(pattern, str):
        raise TypeError("Pattern must be a string")
    
    # Handle empty string
    if not pattern:
        return []
    
    # Initialize LPS array with zeros
    lps = [0] * len(pattern)
    
    # Length of the previous longest prefix suffix
    length = 0
    i = 1
    
    # Build the LPS array
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length != 0:
                # Try to find a shorter prefix
                length = lps[length - 1]
            else:
                # No prefix found
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt string search.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: Indices of all occurrences of the pattern in the text.
    
    Raises:
        TypeError: If inputs are not strings.
    """
    # Validate inputs
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    # Handle empty inputs
    if not pattern or not text:
        return []
    
    # Compute the LPS array
    lps = compute_lps_array(pattern)
    
    # List to store all matches
    matches = []
    
    # Pointers for text and pattern
    i = 0  # text index
    j = 0  # pattern index
    
    while i < len(text):
        # If characters match, move both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # Pattern fully matched
        if j == len(pattern):
            matches.append(i - j)
            # Continue searching by moving j to the longest proper prefix
            j = lps[j - 1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not at the start, use LPS to continue
            if j != 0:
                j = lps[j - 1]
            else:
                # No match, move to next character in text
                i += 1
    
    return matches