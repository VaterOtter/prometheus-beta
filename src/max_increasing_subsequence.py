from typing import List, Tuple

def max_increasing_subsequence_sum(arr: List[int]) -> int:
    """
    Find the maximum sum of an increasing subsequence.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time Complexity: Technically O(n²), but designed with intelligently finding subsequences
    Space Complexity: O(n)
    
    Edge Cases:
    - Empty array returns 0
    - Single element array returns that element
    """
    if not arr:
        return 0
    
    # Track best sum and selection for each subsequence
    best_sequence = [(num, [index]) for index, num in enumerate(arr)]
    
    for i in range(1, len(arr)):
        for j in range(i):
            # If we can form an increasing subsequence
            if arr[i] > arr[j]:
                # Potential new sum
                new_sum = best_sequence[j][0] + arr[i]
                
                # Compare with existing best for current index
                if new_sum > best_sequence[i][0]:
                    # Update best sequence
                    best_sequence[i] = (new_sum, best_sequence[j][1] + [i])
    
    # Return the maximum sum of a valid subsequence
    return max(sum_val for sum_val, _ in best_sequence)