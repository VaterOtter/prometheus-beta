def edit_distance(str1: str, str2: str) -> int:
    """
    Calculate the minimum number of operations to transform str1 into str2.
    
    Operations allowed:
    1. Insert a character
    2. Delete a character
    3. Replace a character
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        int: Minimum number of operations to transform str1 into str2
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Create a matrix to store edit distances
    m, n = len(str1), len(str2)
    
    # Initialize the dynamic programming matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Compute edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters are the same, no operation needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Choose minimum of insert, delete, or replace
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # deletion
                    dp[i][j-1],    # insertion
                    dp[i-1][j-1]   # replacement
                )
    
    return dp[m][n]