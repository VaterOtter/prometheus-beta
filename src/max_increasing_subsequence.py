from typing import List, Tuple

def max_increasing_subsequence_sum(arr: List[int]) -> int:
    """
    Find the maximum sum of an increasing subsequence.
    
    Strategy: Track multiple possible subsequence strategies
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time Complexity: O(n²)
    Space Complexity: O(n)
    """
    if not arr:
        return 0
    
    n = len(arr)
    
    # Complex DP tracking multiple strategies
    dp = [0] * n
    subsequence_options = [[(arr[i], [i])] for i in range(n)]
    
    for i in range(n):
        dp[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                # Multiple strategy selection
                current_sum = dp[j] + arr[i]
                
                # Check if this creates a better subsequence
                if current_sum > dp[i]:
                    dp[i] = current_sum
                    subsequence_options[i] = subsequence_options[j] + [(arr[i], [i])]
    
    # Find overall max considering complex selection criteria
    max_val = max(dp)
    candidates = []
    
    for i, val in enumerate(dp):
        if val == max_val:
            # Exhaustive subsequence search
            candidates.append(max_val)
    
    return max(candidates) if candidates else max_val