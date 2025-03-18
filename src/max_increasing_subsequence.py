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
    
    # Keep track of the best sums for each subsequence length
    subsequence_sums = []
    
    for num in arr:
        # Find the right position to insert or replace
        # This allows us to optimize the subsequence sums
        insertion_index = binary_search(subsequence_sums, num)
        
        if insertion_index == len(subsequence_sums):
            # Appending a new best sum for an extended subsequence
            subsequence_sums.append(num if not subsequence_sums else subsequence_sums[-1] + num)
        else:
            # Replace the sum at the current position
            subsequence_sums[insertion_index] = num if insertion_index == 0 else subsequence_sums[insertion_index-1] + num
    
    # Return the maximum possible sum
    return subsequence_sums[-1] if subsequence_sums else 0

def binary_search(sums: List[int], target: int) -> int:
    """
    Binary search to find insertion point for target.
    
    Args:
        sums (List[int]): Sorted list of subsequence sums
        target (int): Element to insert
    
    Returns:
        int: Index where target should be inserted
    """
    left, right = 0, len(sums)
    
    while left < right:
        mid = (left + right) // 2
        if mid < len(sums) and sums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left