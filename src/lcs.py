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
    def get_lcs_candidates(matrix, s1, s2):
        """Generate all possible LCS with equal lengths."""
        def backtrack(i, j, current_lcs):
            # Backtracking stops
            if i == 0 or j == 0:
                return [current_lcs[::-1]]
            
            # Match found
            if s1[i-1] == s2[j-1]:
                candidates = backtrack(i-1, j-1, current_lcs + s1[i-1])
                
                # Also explore other paths if the current length is maintained
                if dp[i][j] == dp[i-1][j]:
                    candidates.extend(backtrack(i-1, j, current_lcs))
                if dp[i][j] == dp[i][j-1]:
                    candidates.extend(backtrack(i, j-1, current_lcs))
                
                return candidates
            
            # No match, explore paths maintaining length
            candidates = []
            if dp[i-1][j] > dp[i][j-1]:
                candidates.extend(backtrack(i-1, j, current_lcs))
            else:
                candidates.extend(backtrack(i, j-1, current_lcs))
            
            return candidates
        
        # Get all LCS candidates and filter to max length
        candidates = backtrack(len(s1), len(s2), '')
        max_length = len(max(candidates, key=len))
        return [lcs for lcs in candidates if len(lcs) == max_length]
    
    # Get all possible longest common subsequences and choose lexicographically first
    lcs_candidates = get_lcs_candidates(dp, str1, str2)
    return min(lcs_candidates) if lcs_candidates else ""