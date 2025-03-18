from typing import List, Tuple
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
    
    # Initialize lists to track subsequence state
    subsequence = []  # values in current subsequence
    subsequence_sums = []  # maximum sum up to each point
    
    for num in arr:
        # If first element or cannot extend current subsequence
        if not subsequence or num > subsequence[-1]:
            # Compute new sum
            new_sum = num if not subsequence_sums else subsequence_sums[-1] + num
            
            subsequence.append(num)
            subsequence_sums.append(new_sum)
        else:
            # Find the replacement index
            index = bisect.bisect_left(subsequence, num)
            
            # Update subsequence and its sums
            if index == 0:
                subsequence[index] = num
                subsequence_sums[index] = num
            else:
                subsequence[index] = num
                subsequence_sums[index] = subsequence_sums[index-1] + num
    
    # Return maximum possible subsequence sum
    return max(subsequence_sums)