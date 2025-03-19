from typing import List, Tuple

def get_unique_pairs(integers: List[int]) -> List[Tuple[int, int]]:
    """
    Generate all unique pairs of elements from the given list of integers.
    
    Args:
        integers (List[int]): Input list of integers
    
    Returns:
        List[Tuple[int, int]]: List of unique pairs of integers
    
    Notes:
    - Pairs are unique regardless of order (e.g., (1,2) is the same as (2,1))
    - Returns an empty list if input list has fewer than 2 elements
    - Does not modify the original list
    
    Examples:
        >>> get_unique_pairs([1, 2, 3])
        [(1, 2), (1, 3), (2, 3)]
        >>> get_unique_pairs([])
        []
        >>> get_unique_pairs([5])
        []
    """
    # Handle edge cases
    if len(integers) < 2:
        return []
    
    # Generate unique pairs using list comprehension
    unique_pairs = []
    for i in range(len(integers)):
        for j in range(i+1, len(integers)):
            unique_pairs.append((integers[i], integers[j]))
    
    return unique_pairs