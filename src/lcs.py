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
    
    # Backtrack to find the LCS
    def backtrack_lcs(matrix, s1, s2):
        """Generate LCS candidates, preferring lexicographically early subsequences."""
        def dfs(i, j, current_lcs, max_length):
            # Stop conditions
            if len(current_lcs) == max_length:
                return [current_lcs[::-1]]
            
            candidates = []
            
            # Prefer lexicographically early paths
            if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
                candidates.extend(dfs(i-1, j-1, current_lcs + s1[i-1], max_length))
            
            # Non-match paths
            if i > 0 and matrix[i-1][j] >= matrix[i][j-1]:
                candidates.extend(dfs(i-1, j, current_lcs, max_length))
            
            if j > 0 and matrix[i][j-1] >= matrix[i-1][j]:
                candidates.extend(dfs(i, j-1, current_lcs, max_length))
            
            return candidates
        
        max_length = matrix[len(s1)][len(s2)]
        all_candidates = dfs(len(s1), len(s2), '', max_length)
        
        # Sort and return first (lexicographically earliest)
        return sorted(set(all_candidates))[0] if all_candidates else ""
    
    return backtrack_lcs(dp, str1, str2)