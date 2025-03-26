def find_palindromic_substrings(s: str) -> list:
    """
    Find all palindromic substrings in a given string.
    
    A palindromic substring is a sequence of characters that reads the same 
    forwards and backwards. This function uses an expanded center approach 
    to efficiently find all palindromic substrings.
    
    Args:
        s (str): The input string to search for palindromic substrings.
    
    Returns:
        list: A list of all unique palindromic substrings found in the input string.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_palindromic_substrings("abc")
        ['a', 'b', 'c']
        >>> find_palindromic_substrings("racecar")
        ['r', 'a', 'c', 'e', 'racecar', 'aceca', 'cec']
    """
    # Handle edge cases
    if not s or not isinstance(s, str):
        return []
    
    # Set to store unique palindromic substrings
    palindromes = set()
    
    def expand_around_center(left: int, right: int) -> None:
        """
        Expand around a center to find palindromic substrings.
        
        Args:
            left (int): Left index to start expanding
            right (int): Right index to start expanding
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
    
    # Check palindromes with odd and even lengths
    for i in range(len(s)):
        # Odd length palindromes (single character center)
        expand_around_center(i, i)
        
        # Even length palindromes (two character center)
        expand_around_center(i, i+1)
    
    return sorted(list(palindromes), key=lambda x: (len(x), x))