from typing import List
import bisect

def max_increasing_subsequence_sum(arr: List[int]) -> int:
    """
    Find the maximum sum of an increasing subsequence with O(n log n) time complexity.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Edge Cases:
    - Empty array returns 0
    - Single element array returns that element
    """
    if not arr:
        return 0
    
    # Store the best sequence sum for each length
    dp = [(0, float('-inf'))]  # (sum, max_element)
    
    for num in arr:
        # Find the best previous subsequence we can extend
        index = bisect.bisect(dp, (0, num)) - 1
        
        # Get the best previous sum and compute new sum
        prev_sum, prev_max = dp[index]
        new_sum = prev_sum + num
        
        # Extend or replace subsequence
        if index == len(dp) - 1:
            dp.append((new_sum, num))
        else:
            # Replace or extend existing subsequence
            dp[index + 1] = max(dp[index + 1], (new_sum, num), key=lambda x: x[0])
    
    # Return the maximum sum
    return max(sum_val for sum_val, _ in dp)