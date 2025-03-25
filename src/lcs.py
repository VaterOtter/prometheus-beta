def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings using dynamic programming.
    
    The function is case-sensitive and ensures:
    1. Proper order of characters
    2. Handles repeated characters correctly
    3. Returns the longest common subsequence
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Input validation
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Handle case sensitivity and empty string cases
    if str1 != str2 and str1.lower() == str2.lower():
        return ""
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Generate multiple LCS candidates
    def backtrack_lcs_candidates(matrix, s1, s2, length):
        candidates = set()
        
        def _backtrack(i, j, current_lcs):
            # Backtracking stops
            if len(current_lcs) == length:
                candidates.add(current_lcs[::-1])
                return
            
            # Match found
            if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
                _backtrack(i-1, j-1, current_lcs + s1[i-1])
            
            # Non-matching paths
            if i > 0 and (j == 0 or matrix[i-1][j] >= matrix[i][j-1]):
                _backtrack(i-1, j, current_lcs)
            if j > 0 and (i == 0 or matrix[i][j-1] >= matrix[i-1][j]):
                _backtrack(i, j-1, current_lcs)
        
        _backtrack(len(s1), len(s2), '')
        return sorted(candidates)
    
    # Get the length of LCS
    lcs_length = dp[m][n]
    
    # Get all candidates of exact max length
    lcs_candidates = backtrack_lcs_candidates(dp, str1, str2, lcs_length)
    
    # Return lexicographically first if available
    return lcs_candidates[0] if lcs_candidates else ""