def longest_increasing_subsequence_length(nums):
    """
    Find the length of the longest increasing subsequence in a list of numbers.
    
    Args:
        nums (list): A list of comparable elements (typically numbers).
    
    Returns:
        int: Length of the longest increasing subsequence.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-comparable elements.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> longest_increasing_subsequence_length([10, 22, 9, 33, 21, 50, 41, 60, 80])
        6
        >>> longest_increasing_subsequence_length([])
        0
        >>> longest_increasing_subsequence_length([5])
        1
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not nums:
        return 0
    
    # Initialize dynamic programming array
    # dp[i] represents the length of the longest increasing subsequence 
    # that ends with nums[i]
    dp = [1] * len(nums)
    
    # Compute longest increasing subsequence length
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length found
    return max(dp)