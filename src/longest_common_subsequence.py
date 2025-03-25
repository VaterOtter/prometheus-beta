def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings.
    
    A subsequence is a sequence that can be derived from another sequence 
    by deleting some or no elements without changing the order of the remaining elements.
    
    Note: This implementation is case-sensitive and exact.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Examples:
        >>> longest_common_subsequence("ABCDGH", "AEDFHR")
        'ADH'
        >>> longest_common_subsequence("AGGTAB", "GXTXAYB")
        'GTAB'
        >>> longest_common_subsequence("", "test")
        ''
        >>> longest_common_subsequence("test", "")
        ''
    """
    # Handle edge cases of empty strings or different case strings
    if not str1 or not str2 or not _case_sensitive_overlap(str1, str2):
        return ""
    
    # Create a matrix to store lengths of common subsequences
    m, n = len(str1), len(str2)
    # Add 1 to dimensions to account for empty string
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Find all possible subsequences with maximum length
    max_subsequences = []
    max_length = 0
    
    # Build the dynamic programming table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                # If characters match, extend previous subsequence
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # If characters don't match, take max of previous subsequences
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the longest common subsequence
    def backtrack(i, j, current_subsequence):
        # If we've reached the top or left of the matrix, return current sequence
        if i == 0 or j == 0:
            current_subsequence.reverse()
            subsequence_str = ''.join(current_subsequence)
            nonlocal max_length, max_subsequences
            
            # Update max subsequences based on certain conditions
            if len(subsequence_str) > max_length:
                max_length = len(subsequence_str)
                max_subsequences = [subsequence_str]
            elif len(subsequence_str) == max_length:
                max_subsequences.append(subsequence_str)
            
            current_subsequence.reverse()  # restore original order for backtracking
            return
        
        if str1[i-1] == str2[j-1]:
            # If characters match, include in subsequence
            current_subsequence.append(str1[i-1])
            backtrack(i-1, j-1, current_subsequence)
            current_subsequence.pop()
        else:
            # Move in direction of larger subsequence
            if dp[i-1][j] >= dp[i][j-1]:
                backtrack(i-1, j, current_subsequence)
            if dp[i][j-1] >= dp[i-1][j]:
                backtrack(i, j-1, current_subsequence)
    
    # Start backtracking
    backtrack(m, n, [])
    
    # Return lexicographically first subsequence or empty string
    return min(max_subsequences) if max_subsequences else ""

def _case_sensitive_overlap(str1: str, str2: str) -> bool:
    """
    Check if two strings have any case-sensitive character overlap.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        bool: True if strings have any case-sensitive common characters, False otherwise
    """
    return any(c in str2 for c in str1)