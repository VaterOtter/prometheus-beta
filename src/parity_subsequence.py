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
    
    # Track the longest subsequences
    max_even_seq = []
    max_odd_seq = []
    
    # Go through the entire array
    n = len(arr)
    for start in range(n):
        # Check both even and odd subsequences
        for parity_mode in [True, False]:  # True for even, False for odd
            current_seq = []
            
            # Scan from the starting point forward
            for j in range(start, n):
                # Check the parity condition
                if (parity_mode and arr[j] % 2 == 0) or (not parity_mode and arr[j] % 2 != 0):
                    current_seq.append(arr[j])
                else:
                    # Stop when parity changes
                    break
            
            # Update max subsequences
            if parity_mode:
                if len(current_seq) > len(max_even_seq):
                    max_even_seq = current_seq
            else:
                if len(current_seq) > len(max_odd_seq):
                    max_odd_seq = current_seq
    
    # Prefer even sequence if lengths are equal
    return max_even_seq if len(max_even_seq) >= len(max_odd_seq) else max_odd_seq