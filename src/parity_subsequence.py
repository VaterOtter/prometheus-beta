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
    
    def extract_continuous_subsequences(parity_func):
        """Extract continuous subsequences of a specific parity."""
        subsequences = []
        current_subsequence = []
        
        for num in arr:
            if parity_func(num):
                current_subsequence.append(num)
            else:
                if current_subsequence:
                    subsequences.append(current_subsequence)
                    current_subsequence = []
        
        # Add the last subsequence if not empty
        if current_subsequence:
            subsequences.append(current_subsequence)
        
        return subsequences
    
    # Get even and odd subsequences
    even_subsequences = extract_continuous_subsequences(lambda x: x % 2 == 0)
    odd_subsequences = extract_continuous_subsequences(lambda x: x % 2 != 0)
    
    # Find the longest subsequence
    def get_longest_subsequence(subsequences):
        return max(subsequences, key=len) if subsequences else []
    
    # Get longest subsequences
    longest_even_seq = get_longest_subsequence(even_subsequences)
    longest_odd_seq = get_longest_subsequence(odd_subsequences)
    
    # Prefer even subsequence if lengths are equal
    return longest_even_seq if len(longest_even_seq) >= len(longest_odd_seq) else longest_odd_seq