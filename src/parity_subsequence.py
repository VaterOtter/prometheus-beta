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
    
    # Track subsequences of different parities
    max_even_seq = []
    max_odd_seq = []
    
    # Scan the entire array to find parity subsequences
    for is_even in [True, False]:
        # Check each possible starting point 
        for start in range(len(arr)):
            # Temporary subsequence to track contiguous parity elements 
            temp_seq = []
            
            # Scan from the starting point
            for num in arr[start:]:
                # Condition for maintaining parity
                if (is_even and num % 2 == 0) or (not is_even and num % 2 != 0):
                    temp_seq.append(num)
                else:
                    break
            
            # Update max subsequence for even or odd 
            if is_even:
                max_even_seq = max(max_even_seq, temp_seq, key=len)
            else:
                max_odd_seq = max(max_odd_seq, temp_seq, key=len)
    
    # Prefer even subsequence if lengths are equal
    return max_even_seq if len(max_even_seq) >= len(max_odd_seq) else max_odd_seq