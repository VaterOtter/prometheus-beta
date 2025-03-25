def find_longest_parity_subsequence(arr):
    """
    Find the longest subsequence with the same parity (all even or all odd) in the given array.
    
    Args:
        arr (list): A list of integers to search for the longest parity subsequence.
    
    Returns:
        list: The longest subsequence with consistent parity (either all even or all odd).
               If multiple subsequences of the same max length exist, returns the first one.
    
    Examples:
        >>> find_longest_parity_subsequence([1, 2, 3, 4, 5, 6, 7, 8])
        [2, 4, 6, 8]
        >>> find_longest_parity_subsequence([1, 3, 5, 7])
        [1, 3, 5, 7]
        >>> find_longest_parity_subsequence([])
        []
    """
    # Handle empty array case
    if not arr:
        return []
    
    # Track subsequences of even and odd numbers
    max_length = 0
    max_subsequence = []
    
    # Try generating subsequences starting from each index
    for start in range(len(arr)):
        # Check even and odd subsequences
        for parity_func in [lambda x: x % 2 == 0, lambda x: x % 2 != 0]:
            subsequence = []
            # Attempt to generate a subsequence
            for num in arr[start:]:
                if parity_func(num):
                    subsequence.append(num)
                else:
                    break
            
            # Update max subsequence if current is longer
            if len(subsequence) > max_length:
                max_length = len(subsequence)
                max_subsequence = subsequence
    
    return max_subsequence