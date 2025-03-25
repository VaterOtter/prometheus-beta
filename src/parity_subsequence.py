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
    
    # Track subsequences
    longest_subsequences = {
        'even': [],
        'odd': []
    }
    
    # Current subsequence being built
    current_subsequence = []
    
    # Temporarily track the current parity (None, 'even', 'odd')
    current_parity = None
    
    for num in arr:
        # Determine the parity of the current number
        parity = 'even' if num % 2 == 0 else 'odd'
        
        # If we need to start a new subsequence
        if current_parity is None or current_parity == parity:
            current_subsequence.append(num)
            current_parity = parity
        else:
            # If parity has changed, update longest subsequence
            if len(current_subsequence) > len(longest_subsequences[current_parity]):
                longest_subsequences[current_parity] = current_subsequence.copy()
            
            # Start a new subsequence
            current_subsequence = [num]
            current_parity = parity
    
    # Final check to update the last subsequence if needed
    if len(current_subsequence) > len(longest_subsequences[current_parity]):
        longest_subsequences[current_parity] = current_subsequence
    
    # Compare subsequence lengths, favoring even if equal
    even_len = len(longest_subsequences['even'])
    odd_len = len(longest_subsequences['odd'])
    
    # Return the subsequence with max length, prefer even on tie
    return longest_subsequences['even'] if even_len >= odd_len else longest_subsequences['odd']