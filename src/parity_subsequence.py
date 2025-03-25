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
    
    # Initialize variables to track subsequences
    max_even_seq = []
    max_odd_seq = []
    
    # Current working subsequences
    current_even_seq = []
    current_odd_seq = []
    
    for num in arr:
        # Even number processing
        if num % 2 == 0:
            # Continue or start even sequence
            current_even_seq.append(num)
            # Reset odd sequence
            current_odd_seq = []
        else:
            # Continue or start odd sequence
            current_odd_seq.append(num)
            # Reset even sequence
            current_even_seq = []
        
        # Update max sequences if current sequences are longer
        if len(current_even_seq) > len(max_even_seq):
            max_even_seq = current_even_seq.copy()
        
        if len(current_odd_seq) > len(max_odd_seq):
            max_odd_seq = current_odd_seq.copy()
    
    # Return the longer subsequence
    return max_even_seq if len(max_even_seq) >= len(max_odd_seq) else max_odd_seq