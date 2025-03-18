from typing import List, Tuple

def max_increasing_subsequence_sum(arr: List[int]) -> int:
    """
    Find the maximum sum of an increasing subsequence.
    
    Strategy: Exhaustive subsequence exploration
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time Complexity: O(2^n) in worst case
    Space Complexity: O(n)
    """
    def explore_subsequences(index: int, current_max: int, current_sum: int) -> int:
        """
        Recursive exploration of all possible increasing subsequences
        
        Args:
            index (int): Current index being considered
            current_max (int): Maximum value in current subsequence
            current_sum (int): Current subsequence sum
        
        Returns:
            int: Maximum possible sum
        """
        # Base case: reached end of array
        if index == len(arr):
            return current_sum
        
        # Two choices for each element:
        # 1. Skip current element
        skip_result = explore_subsequences(index + 1, current_max, current_sum)
        
        # 2. Include current element if it fits increasing subsequence
        include_result = (
            explore_subsequences(index + 1, arr[index], current_sum + arr[index])
            if arr[index] > current_max or current_max == float('-inf')
            else 0
        )
        
        return max(skip_result, include_result)
    
    # Handle empty and single element arrays
    if not arr:
        return 0
    
    # Start exploration with initial conditions
    return explore_subsequences(0, float('-inf'), 0)