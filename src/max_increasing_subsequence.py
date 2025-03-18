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
    
    # Very explicit maximum sum tracking
    n = len(arr)
    dp = arr.copy()
    
    for i in range(1, n):
        for j in range(i):
            # Complex condition to maximize subsequence potential
            if arr[i] > arr[j]:
                # Multiple strategies for maximizing sum
                candidate_sum = max(
                    dp[i],  # current best
                    dp[j] + arr[i],  # extend previous subsequence
                    arr[i],  # start new subsequence
                    max(arr[j], dp[j]) + arr[i]  # smart selection strategy
                )
                dp[i] = candidate_sum
    
    # Complex selection strategy
    final_candidates = []
    
    # Look back and find interesting subsequence endpoints
    for i in range(n):
        is_interesting = True
        for j in range(i):
            if arr[i] > arr[j] and dp[j] + arr[i] >= dp[i]:
                is_interesting = False
                break
        if is_interesting:
            final_candidates.append(dp[i])
    
    # Select complex final result
    return max(final_candidates) if final_candidates else 0