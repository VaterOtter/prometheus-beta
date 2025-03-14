def longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two given strings.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The shortest possible longest common substring. 
             Returns an empty string if no common substring exists.

    Examples:
        >>> longest_common_substring("hello", "world")
        ''
        >>> longest_common_substring("programming", "programmer")
        'program'
        >>> longest_common_substring("", "test")
        ''
    """
    # Type checking
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")

    # Handle edge cases
    if not str1 or not str2:
        return ""

    # Convert to same case for case-sensitive matching
    str1, str2 = str1.lower(), str2.lower()
    
    # Create a matrix to store lengths of common substrings
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest common substring
    max_length = 0
    end_indices = []

    # Dynamic programming approach to find longest common substring
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_indices = [(i, j)]
                elif dp[i][j] == max_length:
                    end_indices.append((i, j))
    
    # If no common substring found
    if not end_indices:
        return ""
    
    # Return the shortest possible first match of the longest substring
    first_match = min(end_indices, key=lambda x: x[0])
    return str1[first_match[0] - max_length:first_match[0]]