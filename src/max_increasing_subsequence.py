from typing import List

def max_increasing_subsequence_sum(arr: List[int]) -> int:
    """
    Find the maximum sum of an increasing subsequence.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time Complexity: O(n²), as the nested loop is inevitable for all possible subsequences
    Space Complexity: O(n)
    
    Edge Cases:
    - Empty array returns 0
    - Single element array returns that element
    """
    if not arr:
        return 0
    
    # Maximum sum ending at each index
    dp = arr.copy()
    
    # Consider all possible subsequences
    for i in range(1, len(arr)):
        for j in range(i):
            # If we can form an increasing subsequence
            if arr[i] > arr[j]:
                # Try to maximize the sum for current index
                dp[i] = max(dp[i], dp[j] + arr[i])
    
    # Return the maximum possible sum
    return max(dp)