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
    
    # Track best subsequences for even and odd numbers 
    max_even_seq = []
    max_odd_seq = []
    
    # Variables to help track the current sequences
    current_even_seq = []
    current_odd_seq = []
    
    for num in arr:
        # Check and handle even and odd subsequences
        if num % 2 == 0:
            # If the previous sequence was not even, reset
            if not current_even_seq or (current_even_seq and arr[arr.index(num)-1] % 2 != 0):
                current_even_seq = [num]
            else:
                current_even_seq.append(num)
            
            # Reset the odd sequence
            current_odd_seq = []
        else:
            # If the previous sequence was not odd, reset
            if not current_odd_seq or (current_odd_seq and arr[arr.index(num)-1] % 2 == 0):
                current_odd_seq = [num]
            else:
                current_odd_seq.append(num)
            
            # Reset the even sequence
            current_even_seq = []
        
        # Update max sequences
        max_even_seq = max(max_even_seq, current_even_seq, key=len)
        max_odd_seq = max(max_odd_seq, current_odd_seq, key=len)
    
    # Return the longer subsequence, preferring even if equal
    return max_even_seq if len(max_even_seq) >= len(max_odd_seq) else max_odd_seq