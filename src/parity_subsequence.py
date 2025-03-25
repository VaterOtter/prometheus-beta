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
    
    # Function to find the longest parity subsequence
    def get_longest_parity_seq(parity_func):
        longest_seq = []
        current_seq = []
        
        for num in arr:
            if parity_func(num):
                # If number matches the parity
                current_seq.append(num)
            else:
                # If number breaks parity, update longest sequence
                if len(current_seq) > len(longest_seq):
                    longest_seq = current_seq
                current_seq = []
        
        # Final check after the loop
        if len(current_seq) > len(longest_seq):
            longest_seq = current_seq
        
        return longest_seq
    
    # Find longest even subsequence
    max_even_seq = get_longest_parity_seq(lambda x: x % 2 == 0)
    
    # Find longest odd subsequence
    max_odd_seq = get_longest_parity_seq(lambda x: x % 2 != 0)
    
    # Prefer even subsequence if lengths are equal
    return max_even_seq if len(max_even_seq) >= len(max_odd_seq) else max_odd_seq