from typing import List

def max_increasing_subsequence_sum(arr: List[int]) -> int:
    """
    Find the maximum sum of an increasing subsequence.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time Complexity: O(n²)
    Space Complexity: O(n)
    
    Edge Cases:
    - Empty array returns 0
    - Single element array returns that element
    """
    if not arr:
        return 0
    
    # Maximum sum that ends with each element
    dp = arr.copy()
    
    # Keep track of the index of the best previous element
    prev_best = [None] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(i):
            # If current element can extend a subsequence
            if arr[i] > arr[j] and dp[j] + arr[i] > dp[i]:
                dp[i] = dp[j] + arr[i]
                prev_best[i] = j
    
    # Find the index of maximum sum
    max_sum_index = dp.index(max(dp))
    
    return max(dp)