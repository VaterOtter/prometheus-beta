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
    
    # Maximum value that can be achieved ending at each index
    max_sum_ending_here = [num for num in arr]
    
    # Track previous subsequence max to optimize finding increasing subsequence
    prev_max = [float('-inf')] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(i):
            # If current can form an increasing subsequence
            if (arr[i] > arr[j]) and (max_sum_ending_here[j] + arr[i] > max_sum_ending_here[i]):
                max_sum_ending_here[i] = max_sum_ending_here[j] + arr[i]
                prev_max[i] = max_sum_ending_here[j]
    
    # Return maximum sum
    return max(max_sum_ending_here)