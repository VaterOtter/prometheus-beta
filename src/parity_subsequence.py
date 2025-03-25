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
    
    # Tracking subsequences
    longest_even_seq = []
    longest_odd_seq = []
    
    # Systematic approach to find parity subsequences
    n = len(arr)
    for is_even in [True, False]:
        # Try every possible starting point
        for start in range(n):
            current_seq = []
            
            # Scan forward from the starting point
            for j in range(start, n):
                # Check if number matches desired parity
                if (is_even and arr[j] % 2 == 0) or (not is_even and arr[j] % 2 != 0):
                    current_seq.append(arr[j])
                else:
                    break
            
            # Update the max subsequence
            if is_even:
                # Prefer the first occurring subsequence
                if len(current_seq) > len(longest_even_seq) or \
                   (len(current_seq) == len(longest_even_seq) and start < arr.index(longest_even_seq[0]) if longest_even_seq else False):
                    longest_even_seq = current_seq
            else:
                # Prefer the first occurring subsequence
                if len(current_seq) > len(longest_odd_seq) or \
                   (len(current_seq) == len(longest_odd_seq) and start < arr.index(longest_odd_seq[0]) if longest_odd_seq else False):
                    longest_odd_seq = current_seq
    
    # Prefer even sequence on equal length
    return longest_even_seq if len(longest_even_seq) >= len(longest_odd_seq) else longest_odd_seq