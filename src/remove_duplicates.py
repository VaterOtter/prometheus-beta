def remove_duplicates(arr):
    """
    Remove duplicate elements from an array while maintaining O(n) time complexity.
    
    This function uses a set to track unique elements, preserving the original order
    of first occurrence for each unique element.
    
    Args:
        arr (list): Input list that may contain duplicate elements
    
    Returns:
        list: A new list with duplicates removed, preserving the order of first occurrence
    
    Raises:
        TypeError: If the input is not a list
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates([])
        []
        >>> remove_duplicates(['a', 'b', 'a', 'c'])
        ['a', 'b', 'c']
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use dict to preserve order in Python 3.7+ while tracking unique elements
    seen = {}
    for item in arr:
        # Only add first occurrence of each item
        if item not in seen:
            seen[item] = None
    
    # Return list of unique items in order of first appearance
    return list(seen.keys())