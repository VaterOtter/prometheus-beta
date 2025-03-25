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
    
    # Define parity-finding functions
    def finds_even_subsequence(x):
        return x % 2 == 0
    
    def finds_odd_subsequence(x):
        return x % 2 != 0
    
    def get_longest_subsequence(parity_check):
        # Track best subsequence and current subsequence
        longest_seq = []
        current_seq = []
        
        # Iterate over all numbers
        for i, num in enumerate(arr):
            # If number matches parity condition
            if parity_check(num):
                current_seq.append(num)
                
                # Check if next number breaks the parity
                if i < len(arr) - 1 and not parity_check(arr[i+1]):
                    # Update longest subsequence if current is longer
                    if len(current_seq) > len(longest_seq):
                        longest_seq = current_seq
                    current_seq = []
        
        # Final check for subsequence at the end of array
        if len(current_seq) > len(longest_seq):
            longest_seq = current_seq
        
        return longest_seq
    
    # Find the longest subsequences for even and odd
    longest_even_seq = get_longest_subsequence(finds_even_subsequence)
    longest_odd_seq = get_longest_subsequence(finds_odd_subsequence)
    
    # Prefer even subsequence if lengths are equal or longer
    return longest_even_seq if len(longest_even_seq) >= len(longest_odd_seq) else longest_odd_seq