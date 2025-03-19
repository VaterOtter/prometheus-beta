def find_odd_occurrences(numbers):
    """
    Find the smallest number that appears an odd number of times in the list using bitwise XOR.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The smallest number that appears an odd number of times
    
    Raises:
        ValueError: If no number appears an odd number of times or input is empty
    """
    # Handle edge cases
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Use a dictionary to track odd occurrence numbers
    odd_occurrences = {}
    
    # Use bitwise XOR to find numbers with odd occurrences
    for num in numbers:
        # XOR current number with its count to toggle between even/odd
        odd_occurrences[num] = odd_occurrences.get(num, 0) ^ 1
    
    # Filter numbers with odd occurrences
    odd_nums = [num for num, count in odd_occurrences.items() if count == 1]
    
    # If no odd occurrence numbers found
    if not odd_nums:
        raise ValueError("No number appears an odd number of times")
    
    # Return the smallest number with odd occurrences
    return min(odd_nums)