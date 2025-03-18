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
    
    # Track potential subsequence endpoints and their maximum possible sum
    subsequence_states = []
    
    for num in arr:
        # If no subsequences or number is greater than last endpoint
        if not subsequence_states or num > subsequence_states[-1][0]:
            # Add a new subsequence state
            if not subsequence_states:
                subsequence_states.append([num, num])
            else:
                subsequence_states.append([num, subsequence_states[-1][1] + num])
        else:
            # Binary search to find replacement point
            index = binary_search(subsequence_states, num)
            
            # Compute sum based on previous subsequence
            if index == 0:
                # First subsequence: just the number
                subsequence_states[index] = [num, num]
            else:
                # Add to previous subsequence's max sum
                subsequence_states[index] = [num, subsequence_states[index-1][1] + num]
    
    # Return the maximum possible subsequence sum
    return max(sum_val for _, sum_val in subsequence_states)

def binary_search(states: List[List[int]], target: int) -> int:
    """
    Binary search to find insertion point in subsequence states.
    
    Args:
        states (List[List[int]]): List of [endpoint_value, max_sum]
        target (int): Value to insert
    
    Returns:
        int: Insertion index
    """
    left, right = 0, len(states)
    
    while left < right:
        mid = (left + right) // 2
        if states[mid][0] < target:
            left = mid + 1
        else:
            right = mid
    
    return left