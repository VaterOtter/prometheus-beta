from typing import List

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
    
    # Tracking subsequence endpoints and their maximum sums
    dp = []  # dp will contain [end_value, max_sum_ending_with_this_value]
    
    for num in arr:
        if not dp or num > dp[-1][0]:
            # Extending an existing subsequence with a new largest value
            if not dp:
                dp.append([num, num])
            else:
                dp.append([num, dp[-1][1] + num])
        else:
            # Find the correct position to insert/replace
            index = binary_search(dp, num)
            
            # Update the subsequence endpoint
            if index == 0:
                # Replace the first endpoint
                dp[index] = [num, num]
            else:
                # Extend the previous subsequence
                dp[index] = [num, dp[index-1][1] + num]
    
    # Return the maximum subsequence sum
    return max(sum_val for _, sum_val in dp) if dp else 0

def binary_search(dp: List[List[int]], target: int) -> int:
    """
    Binary search to find the insertion point for a new subsequence endpoint.
    
    Args:
        dp (List[List[int]]): List of [endpoint_value, max_sum]
        target (int): New value to insert
    
    Returns:
        int: Index where the new value should be inserted
    """
    left, right = 0, len(dp)
    
    while left < right:
        mid = (left + right) // 2
        if dp[mid][0] < target:
            left = mid + 1
        else:
            right = mid
    
    return left